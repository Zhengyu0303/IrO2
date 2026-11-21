"""
Pre-DFT sanity check for a packmol-generated slab+water structure, using pymatgen.

Checks:
  1. water O-H bond lengths / H-O-H angles are physically sane
  2. the net water-layer dipole moment, computed per-molecule via minimum-image
     O-H vectors -- this is well-defined even when the cell has NO vacuum
     (unlike a naive whole-cell point-charge sum, which breaks down under
     periodic wraparound for a fully-solvated slab like this one).

Usage: python3 check_water_dipole_pymatgen.py POSCAR
"""
import sys
import numpy as np
from pymatgen.core import Structure

DEBYE_PER_EA = 4.8032          # 1 e*Angstrom = 4.8032 Debye
Q_H = 0.4238                    # SPC/E hydrogen charge (O = -2*Q_H, cancels out of the calc)
WATER_OH_CUTOFF = 1.3           # Angstrom - used only to identify water O (has bonded H)


def mic_vector(structure, i, j):
    """Minimum-image Cartesian vector from site i to site j."""
    frac_diff = structure[j].frac_coords - structure[i].frac_coords
    frac_diff -= np.round(frac_diff)          # wrap each component to [-0.5, 0.5)
    return structure.lattice.get_cartesian_coords(frac_diff)


def main(path):
    structure = Structure.from_file(path)
    species = np.array([str(sp) for sp in structure.species])

    o_idx = np.where(species == "O")[0]
    h_idx = np.where(species == "H")[0]
    if len(h_idx) == 0:
        sys.exit("No hydrogens found in this structure - nothing to check.")

    dmat = structure.distance_matrix  # pymatgen applies minimum-image convention here
    water_o = [i for i in o_idx if dmat[i, h_idx].min() < WATER_OH_CUTOFF]
    print(f"Identified {len(water_o)} water O (H-bearing) out of {len(o_idx)} total O.")

    bond_lengths, angles, mol_dipoles, bad = [], [], [], []
    for oi in water_o:
        d_to_h = dmat[oi, h_idx]
        order = np.argsort(d_to_h)[:2]
        h_pair = h_idx[order]
        bl = d_to_h[order]
        bond_lengths.extend(bl)

        v1 = mic_vector(structure, oi, h_pair[0])
        v2 = mic_vector(structure, oi, h_pair[1])
        cos_ang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        ang = np.degrees(np.arccos(np.clip(cos_ang, -1, 1)))
        angles.append(ang)

        # neutral-molecule dipole (relative to O; independent of absolute position,
        # and independent of the periodic wraparound problem that affects a whole-cell sum)
        mol_dipoles.append(Q_H * v1 + Q_H * v2)

        if not (0.85 < bl.min() < 1.15) or not (95 < ang < 115):
            bad.append((oi, bl, ang))

    bond_lengths = np.array(bond_lengths)
    angles = np.array(angles)
    mol_dipoles = np.array(mol_dipoles)

    print(f"\nO-H bond length: mean {bond_lengths.mean():.4f} A (expect ~0.96-1.00 A), "
          f"std {bond_lengths.std():.4f}, min {bond_lengths.min():.4f}, max {bond_lengths.max():.4f}")
    print(f"H-O-H angle:      mean {angles.mean():.2f} deg (expect ~104-109 deg), "
          f"std {angles.std():.2f}")

    if bad:
        print(f"\n!! {len(bad)}/{len(water_o)} molecules fall outside a sane bond-length/angle "
              f"window -- fix the input geometry before running any DFT on this structure.")
    else:
        print("\nGeometry looks physically reasonable.")

    mag = np.linalg.norm(mol_dipoles, axis=1) * DEBYE_PER_EA
    net = mol_dipoles.sum(axis=0) * DEBYE_PER_EA
    full_alignment = mag.sum()

    print(f"\nPer-molecule |mu|: mean {mag.mean():.3f} D, std {mag.std():.3f} D "
          f"(SPC/E monomer ~2.35 D at correct geometry)")
    print(f"Net water-layer dipole vector (Debye): {net}")
    print(f"Net |mu| = {np.linalg.norm(net):.2f} D out of a fully-aligned max of "
          f"{full_alignment:.1f} D ({np.linalg.norm(net) / full_alignment * 100:.1f}%)")
    print(f"z-component (surface-normal, if c is your slab normal): {net[2]:.2f} D")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pristine_packed.vasp")