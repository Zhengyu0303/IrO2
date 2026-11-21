#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:42:29 2026

@author: zhengyuliu
"""

from pymatgen.core import Structure, Molecule
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
import os

# 1. Load your IrO2 surface slab
# Replace 'POSCAR_slab' with the actual name of your file
print("Loading surface slab...")
slab = Structure.from_file("POSCAR.vasp")

# 2. Define the Water Molecule
# We define the local coordinates of an H2O molecule. 
# The Oxygen is placed at the origin [0,0,0] so pymatgen knows exactly what atom 
# to "anchor" to the surface binding site.
water_coords = [
    [0.000000,  0.000000,  0.000000],  # O atom at the origin
    [0.763239,  0.477047,  0.000000],  # H atom
    [-0.763239, 0.477047,  0.000000]   # H atom
]
water = Molecule(["O", "H", "H"], water_coords)

# 3. Initialize the Site Finder
print("Running Delaunay triangulation to find adsorption sites...")
asf = AdsorbateSiteFinder(slab)

# 4. Generate all the unique starting structures
# This takes the water molecule and places it on all symmetry-inequivalent 
# atop, bridge, and hollow sites. 
# 'distance=2.0' places the Oxygen atom 2.0 Ångstroms above the site.
adsorbed_structures = asf.generate_adsorption_structures(
    water, 
    repeat=[1, 1, 1],     # Do not make a larger supercell
    find_args={"distance": 2.0} 
)

print(f"Found {len(adsorbed_structures)} unique binding configurations!")

# 5. Output the POSCAR files
# Create a folder to keep things clean
output_dir = "water_configs"
os.makedirs(output_dir, exist_ok=True)

for index, struct in enumerate(adsorbed_structures):
    filename = f"{output_dir}/POSCAR_water_{index+1}"
    struct.to(fmt="poscar", filename=filename)
    print(f"Saved: {filename}")

print("Done! You can now visualize these in VESTA.")


## We need to rotate that to get the bottom fixed with water molecules, at least get the sites!


# from pymatgen.core.operations import SymmOp

# def rotate_slab_180(slab):
#     """
#     Rotates a Pymatgen Structure 180 degrees around the x-axis.
#     Modifies the structure in-place and returns it.
#     """
#     rotate_180_op = SymmOp.from_rotation_and_translation(
#         rotation_matrix=[
#             [ 1,  0,  0], 
#             [ 0, -1,  0], 
#             [ 0,  0, -1]
#         ],
#         translation_vec=[0, 1, 1]
#     )
    
#     slab.apply_operation(rotate_180_op, fractional=True)
#     return slab


# slab_rotated = rotate_slab_180(slab)
# asf2 = AdsorbateSiteFinder(slab)

# sites = asf.find_adsorption_sites()
# sites2 = asf2.find_adsorption_sites()









