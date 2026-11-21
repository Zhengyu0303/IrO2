import numpy as np

def get_dipol(structure):
    """Mass-weighted center of mass (fractional coords) for VASP's DIPOL tag."""
    coords = np.array([site.frac_coords for site in structure])
    masses = np.array([site.specie.atomic_mass for site in structure], dtype=float)
    return np.average(coords, axis=0, weights=masses)

# from pymatgen.core import Structure
# dipol = get_dipol(Structure.from_file("asymm_defect.vasp"))
# print(dipol)

import glob
from pymatgen.core import Structure

# for path in sorted(glob.glob("*.vasp")):
#     structure = Structure.from_file(path)
#     dipol = get_dipol(structure)
#     print(f"{path}: DIPOL = {dipol[0]:.5f} {dipol[1]:.5f} {dipol[2]:.5f}")

import os
import numpy as np
from pymatgen.core import Structure

def get_dipol(structure):
    coords = np.array([site.frac_coords for site in structure])
    masses = np.array([site.specie.atomic_mass for site in structure], dtype=float)
    return np.average(coords, axis=0, weights=masses)

for root, dirs, files in os.walk("."):
    if "POSCAR" not in files:
        continue
    poscar_path = os.path.join(root, "POSCAR")
    incar_path = os.path.join(root, "INCAR")
    if not os.path.isfile(incar_path):
        print(f"skipping {root}: no INCAR found")
        continue

    structure = Structure.from_file(poscar_path)
    dipol = get_dipol(structure)
    dipol_line = f"DIPOL = {dipol[0]:.5f} {dipol[1]:.5f} {dipol[2]:.5f}\n"

    with open(incar_path) as f:
        lines = f.readlines()

    lines = [l for l in lines if not l.strip().upper().startswith("DIPOL")]
    lines.append(dipol_line)

    with open(incar_path, "w") as f:
        f.writelines(lines)

    print(f"{incar_path}: {dipol_line.strip()}")

import os

for root, dirs, files in os.walk("."):
    if "INCAR" not in files:
        continue
    incar_path = os.path.join(root, "INCAR")

    with open(incar_path) as f:
        lines = f.readlines()

    kept = [l for l in lines if not l.strip().upper().startswith("MAGMOM")]

    if len(kept) != len(lines):
        with open(incar_path, "w") as f:
            f.writelines(kept)
        print(f"{incar_path}: removed {len(lines) - len(kept)} MAGMOM line(s)")