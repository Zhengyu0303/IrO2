"""
Planar Average Plotter for VASP LOCPOT and CHGCAR/RHOB
-------------------------------------------------------
Averages the volumetric data over two directions and plots
it along the third (typically z, the surface normal).

Requirements:
    pip install pymatgen matplotlib numpy

Usage:
    python plot_vasp_planar_avg.py --file LOCPOT
    python plot_vasp_planar_avg.py --file CHGCAR --axis z
    python plot_vasp_planar_avg.py --file LOCPOT --axis x --macroscopic --period 2.46
    python plot_vasp_planar_avg.py --file CHGCAR --spin
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Locpot, Chgcar


# ─────────────────────────────────────────────
# Loaders
# ─────────────────────────────────────────────

def load_locpot(filepath: str):
    loc = Locpot.from_file(filepath)
    return np.array(loc.data["total"]), loc.structure


def load_chgcar(filepath: str):
    chg = Chgcar.from_file(filepath)
    vol = chg.structure.volume
    total = np.array(chg.data["total"]) / vol
    diff  = np.array(chg.data["diff"]) / vol if "diff" in chg.data else None
    return total, diff, chg.structure


# ─────────────────────────────────────────────
# Planar average
# ─────────────────────────────────────────────

AXIS_MAP = {"x": 0, "y": 1, "z": 2}

def planar_average(data: np.ndarray, axis: int = 2) -> np.ndarray:
    """Average data over the two axes perpendicular to `axis`."""
    axes = tuple(i for i in range(3) if i != axis)
    return data.mean(axis=axes)


def macroscopic_average(planar_avg: np.ndarray, period: float,
                        lattice_param: float) -> np.ndarray:
    """
    Compute the macroscopic average by convolving the planar average
    with a rectangular window of width = one lattice period.

    Parameters
    ----------
    planar_avg   : 1-D array (planar average along the chosen axis)
    period       : physical period length in Å (e.g. interlayer spacing)
    lattice_param: total cell length along the axis in Å
    """
    n = len(planar_avg)
    # Number of grid points spanning one period
    npts = max(1, int(round(n * period / lattice_param)))
    window = np.ones(npts) / npts
    # Use 'wrap' padding for periodic systems
    padded = np.concatenate([planar_avg[-npts//2:],
                             planar_avg,
                             planar_avg[:npts//2]])
    macro = np.convolve(padded, window, mode="valid")
    # Trim to original length
    start = (len(macro) - n) // 2
    return macro[start:start + n]


# ─────────────────────────────────────────────
# Plot
# ─────────────────────────────────────────────

def plot_planar_avg(
    data: np.ndarray,
    structure,
    axis: int = 2,
    title: str = "Planar Average",
    ylabel: str = "Value",
    period: float = None,
    show_atoms: bool = True,
    output: str = None,
    figsize: tuple = (8, 4),
):
    latt   = structure.lattice.matrix
    label  = ["x", "y", "z"][axis]
    length = np.linalg.norm(latt[axis])          # cell length along axis (Å)

    avg = planar_average(data, axis)
    z   = np.linspace(0, length, len(avg), endpoint=False)

    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(z, avg, color="#4c72b0", lw=1.8, label="Planar average")

    if period is not None:
        macro = macroscopic_average(avg, period, length)
        ax.plot(z, macro, color="#dd8452", lw=2.0,
                ls="--", label=f"Macroscopic avg (T={period:.2f} Å)")

    # Atom positions projected onto the chosen axis
    if show_atoms:
        frac_coords = np.array([s.frac_coords[axis] for s in structure])
        cart_coords = frac_coords * length
        ymin, ymax  = ax.get_ylim()
        # Re-query after data is drawn
        ymin = avg.min() - 0.05 * abs(avg.ptp())
        ymax = avg.max() + 0.05 * abs(avg.ptp())
        species = [s.species_string for s in structure]
        unique  = list(dict.fromkeys(species))   # preserve order, deduplicate
        colors  = plt.cm.Set1(np.linspace(0, 0.8, len(unique)))
        sp_color = {sp: colors[i] for i, sp in enumerate(unique)}
        for pos, sp in zip(cart_coords, species):
            ax.axvline(pos, color=sp_color[sp], alpha=0.5, lw=0.8, ls=":")
        # Legend patches for atom species
        from matplotlib.lines import Line2D
        handles = [Line2D([0], [0], color=sp_color[sp], lw=1.5, ls=":",
                          label=sp) for sp in unique]
        ax.add_artist(ax.legend(handles=handles, title="Atoms",
                                loc="upper right", fontsize=8))

    ax.set_xlabel(f"Distance along {label} (Å)", fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13)
    ax.set_xlim(0, length)
    ax.legend(loc="upper left", fontsize=9)
    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150, bbox_inches="tight")
        print(f"Saved to {output}")
    else:
        plt.show()

    return fig, ax


# ─────────────────────────────────────────────
# Convenience wrappers
# ─────────────────────────────────────────────

def plot_locpot_avg(filepath, axis="z", **kwargs):
    data, structure = load_locpot(filepath)
    ax_idx = AXIS_MAP[axis.lower()]
    return plot_planar_avg(
        data, structure, axis=ax_idx,
        title=f"LOCPOT – Planar Average along {axis.upper()}",
        ylabel="Electrostatic Potential (eV)",
        **kwargs,
    )


def plot_chgcar_avg(filepath, axis="z", spin=False, **kwargs):
    total, diff, structure = load_chgcar(filepath)
    data  = diff if (spin and diff is not None) else total
    label = "Spin" if spin else "Charge"
    ax_idx = AXIS_MAP[axis.lower()]
    return plot_planar_avg(
        data, structure, axis=ax_idx,
        title=f"CHGCAR – {label} Density Planar Average along {axis.upper()}",
        ylabel=f"{label} Density (e/Å³)",
        **kwargs,
    )


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Planar average of VASP LOCPOT / CHGCAR"
    )
    parser.add_argument("--file", required=True)
    parser.add_argument("--type", choices=["locpot", "chgcar"], default=None)
    parser.add_argument("--axis", choices=["x", "y", "z"], default="z",
                        help="Axis to plot along (default: z)")
    parser.add_argument("--spin", action="store_true",
                        help="Plot spin (diff) channel for CHGCAR")
    parser.add_argument("--macroscopic", action="store_true",
                        help="Overlay the macroscopic average")
    parser.add_argument("--period", type=float, default=None,
                        help="Lattice period in Å for macroscopic average "
                             "(required if --macroscopic is set)")
    parser.add_argument("--no-atoms", action="store_true",
                        help="Hide atom position markers")
    parser.add_argument("--output", default=None,
                        help="Save figure to file (e.g. avg.png)")
    args = parser.parse_args()

    ftype = args.type or ("locpot" if "LOCPOT" in args.file.upper() else "chgcar")

    if ftype == "locpot":
        print(f"Loading LOCPOT: {args.file}")
        data, structure = load_locpot(args.file)
        title  = f"LOCPOT – Planar Average along {args.axis.upper()}"
        ylabel = "Electrostatic Potential (eV)"
    else:
        print(f"Loading CHGCAR/RHOB: {args.file}")
        total, diff, structure = load_chgcar(args.file)
        data   = diff if (args.spin and diff is not None) else total
        label  = "Spin" if args.spin else "Charge"
        title  = f"CHGCAR – {label} Density Planar Average along {args.axis.upper()}"
        ylabel = f"{label} Density (e/Å³)"

    ax_idx = AXIS_MAP[args.axis]
    period = args.period if args.macroscopic else None

    if args.macroscopic and period is None:
        parser.error("--macroscopic requires --period <value_in_angstrom>")

    plot_planar_avg(
        data, structure,
        axis=ax_idx,
        title=title,
        ylabel=ylabel,
        period=period,
        show_atoms=not args.no_atoms,
        output=args.output,
    )


if __name__ == "__main__":
    main()
    
