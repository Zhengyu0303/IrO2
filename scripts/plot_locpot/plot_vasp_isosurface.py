"""
3D Isosurface Plotter for VASP LOCPOT and CHGCAR/RHOB
------------------------------------------------------
Requirements:
    pip install pymatgen plotly numpy

Usage:
    python plot_vasp_isosurface.py --file LOCPOT --isovalue 0.5
    python plot_vasp_isosurface.py --file CHGCAR --isovalue 0.02 --mode rhob
    python plot_vasp_isosurface.py --file LOCPOT --auto   # auto-pick isovalue
"""

import argparse
import numpy as np
import plotly.graph_objects as go
from pymatgen.io.vasp.outputs import Locpot, Chgcar


# ─────────────────────────────────────────────
# Loaders
# ─────────────────────────────────────────────

def load_locpot(filepath: str) -> tuple[np.ndarray, object]:
    """Load LOCPOT and return (3-D data array, structure)."""
    loc = Locpot.from_file(filepath)
    data = loc.data["total"]          # shape: (nx, ny, nz)
    return np.array(data), loc.structure


def load_chgcar(filepath: str) -> tuple[np.ndarray, np.ndarray | None, object]:
    """
    Load CHGCAR (or RHOB).
    Returns (charge_density, spin_density_or_None, structure).
    Charge density is divided by the cell volume to give e/Å³.
    """
    chg = Chgcar.from_file(filepath)
    volume = chg.structure.volume           # Å³
    total = np.array(chg.data["total"]) / volume
    diff  = (np.array(chg.data["diff"]) / volume
             if "diff" in chg.data else None)
    return total, diff, chg.structure


# ─────────────────────────────────────────────
# Isosurface builder
# ─────────────────────────────────────────────

def build_isosurface_figure(
    data: np.ndarray,
    structure,
    isovalue: float,
    title: str = "3-D Isosurface",
    colorscale: str = "RdBu",
    opacity: float = 0.4,
) -> go.Figure:
    """
    Create a Plotly Figure with a volumetric isosurface and the unit-cell box.

    Parameters
    ----------
    data       : 3-D numpy array (nx, ny, nz) in fractional grid coords
    structure  : pymatgen Structure (for lattice vectors)
    isovalue   : iso-level value; can be a single float or [min, max] pair
    """
    nx, ny, nz = data.shape

    # Fractional grid → Cartesian coordinates
    latt = structure.lattice.matrix          # (3,3) in Å
    fx = np.linspace(0, 1, nx, endpoint=False)
    fy = np.linspace(0, 1, ny, endpoint=False)
    fz = np.linspace(0, 1, nz, endpoint=False)
    FX, FY, FZ = np.meshgrid(fx, fy, fz, indexing="ij")
    frac = np.stack([FX.ravel(), FY.ravel(), FZ.ravel()], axis=1)
    cart = frac @ latt                       # (N, 3) Cartesian

    X = cart[:, 0].reshape(nx, ny, nz)
    Y = cart[:, 1].reshape(nx, ny, nz)
    Z = cart[:, 2].reshape(nx, ny, nz)

    # Isomin / isomax
    if isinstance(isovalue, (list, tuple)) and len(isovalue) == 2:
        isomin, isomax = float(isovalue[0]), float(isovalue[1])
    else:
        half = abs(float(isovalue))
        isomin, isomax = -half, half

    vol = go.Volume(
        x=X.ravel(), y=Y.ravel(), z=Z.ravel(),
        value=data.ravel(),
        isomin=isomin,
        isomax=isomax,
        opacity=opacity,
        surface_count=5,           # number of iso-levels between min and max
        colorscale=colorscale,
        caps=dict(x_show=False, y_show=False, z_show=False),
        name="isosurface",
    )

    # Unit-cell box edges
    def cell_edges(latt):
        """Return line traces for the parallelepiped unit cell."""
        a, b, c = latt[0], latt[1], latt[2]
        origin = np.zeros(3)
        corners = [
            origin, a, b, c,
            a+b, a+c, b+c, a+b+c,
        ]
        edges = [
            (0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)
        ]
        traces = []
        for i, j in edges:
            p, q = corners[i], corners[j]
            traces.append(go.Scatter3d(
                x=[p[0], q[0]], y=[p[1], q[1]], z=[p[2], q[2]],
                mode="lines",
                line=dict(color="black", width=2),
                showlegend=False,
                hoverinfo="skip",
            ))
        return traces

    # Atom spheres
    atom_x = [s.coords[0] for s in structure]
    atom_y = [s.coords[1] for s in structure]
    atom_z = [s.coords[2] for s in structure]
    atom_labels = [str(s.species_string) for s in structure]
    atoms = go.Scatter3d(
        x=atom_x, y=atom_y, z=atom_z,
        mode="markers+text",
        text=atom_labels,
        textposition="top center",
        marker=dict(size=6, color="grey", opacity=0.9,
                    line=dict(width=1, color="black")),
        name="atoms",
    )

    fig = go.Figure(data=[vol, atoms] + cell_edges(latt))
    fig.update_layout(
        title=dict(text=title, font=dict(size=18)),
        scene=dict(
            xaxis_title="x (Å)",
            yaxis_title="y (Å)",
            zaxis_title="z (Å)",
            aspectmode="data",
        ),
        margin=dict(l=0, r=0, b=0, t=50),
    )
    return fig


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def auto_isovalue(data: np.ndarray, sigma: float = 1.5) -> tuple[float, float]:
    """Return ±sigma * std around the mean as a sensible default isovalue pair."""
    mean, std = data.mean(), data.std()
    return mean - sigma * std, mean + sigma * std


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Plot VASP LOCPOT / CHGCAR isosurface")
    parser.add_argument("--file", required=True,
                        help="Path to LOCPOT or CHGCAR/RHOB file")
    parser.add_argument("--type", choices=["locpot", "chgcar"], default=None,
                        help="File type; auto-detected from filename if omitted")
    parser.add_argument("--isovalue", type=float, default=None,
                        help="Iso-level value (absolute). If omitted, --auto is used.")
    parser.add_argument("--isorange", type=float, nargs=2, default=None,
                        metavar=("MIN", "MAX"),
                        help="Explicit [min max] range for iso-levels")
    parser.add_argument("--auto", action="store_true",
                        help="Auto-select isovalue from mean ± 1.5 σ")
    parser.add_argument("--spin", action="store_true",
                        help="Plot spin-density (diff channel) for CHGCAR")
    parser.add_argument("--opacity", type=float, default=0.4,
                        help="Isosurface opacity (0–1)")
    parser.add_argument("--colorscale", default=None,
                        help="Plotly colorscale name (default: RdBu for LOCPOT, "
                             "Viridis for CHGCAR)")
    parser.add_argument("--output", default=None,
                        help="Save HTML to this path instead of opening browser")
    args = parser.parse_args()

    # ── Detect file type ──────────────────────────────────────────────────
    ftype = args.type
    if ftype is None:
        lower = args.file.upper()
        if "LOCPOT" in lower:
            ftype = "locpot"
        else:
            ftype = "chgcar"

    # ── Load data ─────────────────────────────────────────────────────────
    if ftype == "locpot":
        print(f"Loading LOCPOT: {args.file}")
        data, structure = load_locpot(args.file)
        title = "LOCPOT – Electrostatic Potential (eV)"
        colorscale = args.colorscale or "RdBu"
    else:
        print(f"Loading CHGCAR/RHOB: {args.file}")
        total, diff, structure = load_chgcar(args.file)
        if args.spin and diff is not None:
            data = diff
            title = "CHGCAR – Spin Density (e/Å³)"
            colorscale = args.colorscale or "RdBu"
        else:
            data = total
            title = "CHGCAR – Charge Density (e/Å³)"
            colorscale = args.colorscale or "Viridis"

    print(f"  Grid shape : {data.shape}")
    print(f"  Data range : [{data.min():.4g}, {data.max():.4g}]")
    print(f"  Mean ± std : {data.mean():.4g} ± {data.std():.4g}")

    # ── Isovalue ─────────────────────────────────────────────────────────
    if args.isorange:
        isovalue = args.isorange
        print(f"  Iso-range  : {isovalue}")
    elif args.isovalue is not None:
        isovalue = args.isovalue
        print(f"  Iso-level  : ±{isovalue}")
    else:
        isovalue = list(auto_isovalue(data))
        print(f"  Auto iso   : {isovalue[0]:.4g} → {isovalue[1]:.4g}")

    # ── Plot ──────────────────────────────────────────────────────────────
    fig = build_isosurface_figure(
        data, structure, isovalue,
        title=title,
        colorscale=colorscale,
        opacity=args.opacity,
    )

    if args.output:
        fig.write_html(args.output)
        print(f"Saved to {args.output}")
    else:
        fig.show()


# ─────────────────────────────────────────────
# Importable API (use in notebooks / scripts)
# ─────────────────────────────────────────────

def plot_locpot(filepath, isovalue=None, **kwargs):
    """Convenience wrapper for LOCPOT."""
    data, structure = load_locpot(filepath)
    iso = isovalue if isovalue is not None else list(auto_isovalue(data))
    return build_isosurface_figure(
        data, structure, iso,
        title="LOCPOT – Electrostatic Potential (eV)",
        colorscale="RdBu",
        **kwargs,
    )


def plot_chgcar(filepath, spin=False, isovalue=None, **kwargs):
    """Convenience wrapper for CHGCAR/RHOB."""
    total, diff, structure = load_chgcar(filepath)
    data = diff if (spin and diff is not None) else total
    iso = isovalue if isovalue is not None else list(auto_isovalue(data))
    label = "Spin" if spin else "Charge"
    return build_isosurface_figure(
        data, structure, iso,
        title=f"CHGCAR – {label} Density (e/Å³)",
        colorscale="RdBu" if spin else "Viridis",
        **kwargs,
    )


if __name__ == "__main__":
    main()