#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:20:28 2025

@author: zhengyuliu
"""

import os
from pymatgen.core import Structure
import numpy as np

# Load the bulk structure from a POSCAR file
bulk_structure = Structure.from_file("POSCAR.vasp")

from pymatgen.core.surface import SlabGenerator

# Define the Miller index for the surface you want
miller_index = (1, 0, 0)  # Example: (1, 1, 1) plane

# Set up the slab generator
slabgen = SlabGenerator(
    initial_structure=bulk_structure,
    miller_index=miller_index,
    min_slab_size=40,  # Thickness of the slab in Å
    min_vacuum_size=20,  # Thickness of the vacuum layer in Å
    center_slab=True
)

# Generate the slabs
slabs = slabgen.get_slabs()
slabs[0].to(fmt="poscar", filename="mgo20_20_POSCAR_slab.vasp")

# ###Using different methods. First we have to generate a supercell

# structure = Structure.from_file(filename = "mgo20_20_POSCAR_slab.vasp")
# supercell = structure * [3, 3, 1]
# ##We find the O with lower cn and then delete it 
# supercell.to(fmt = "poscar", filename="supercell")

# from pymatgen.analysis.local_env import CutOffDictNN

# # Define nearest neighbor cutoffs for Mg and O atoms (adjust these based on your structure)
# cutoff_nn = CutOffDictNN({("Mg", "O"): 2.5, ("O", "Mg"): 2.5})
# supercell2 = supercell.copy()
# distances = {}

# for i, site in enumerate(supercell):
#     coord_number = cutoff_nn.get_cn(supercell, i)
#     if site.species_string == "O" and coord_number == 5:
#         supercell2.remove(site)
#         for j, site2 in enumerate(supercell):
#             if site2.species_string == "Mg" and cutoff_nn.get_cn(supercell, j) == 5:
#                 distances[j] = supercell.get_distance(i,j)
#             #print(f"Atom {i} ({site.species_string}): Coordination Number = {coord_number}\n")
#         break  

# same_surface = sorted(distances.values())[len(distances)//2-1]
# different_surface = sorted(distances.values())[len(distances)-1]

# for key in distances.keys():
#     if distances[key] == different_surface:
#         supercell2.remove_sites([key])
#         break
        
# supercell2.to(fmt="poscar", filename = "neutral_defect2.vasp")





# for i, site in enumerate(supercell):
#     coord_number = cutoff_nn.get_cn(supercell, i)
#     if site.species_string == "O" and coord_number == 5:
#         print(f"Atom {i} ({site.species_string}): Coordination Number = {coord_number}\n")
#         supercell2.remove(site)
#         break

# supercell2.to(fmt="poscar", filename = "Defected1.vasp")

# ##Now we have generated charged defect. It's time to use the 3 different methods to calculate the DFT energy
# flag = 0
# supercell3= supercell.copy()
# for i, site in enumerate(supercell):
#     coord_number = cutoff_nn.get_cn(supercell, i)
#     if flag == 1 :
#         supercell3.remove(site)
#         break
#     if site.species_string == "O" and coord_number == 5:
#         for j, site2 in enumerate(supercell):
#             coord_number2 = cutoff_nn.get_cn(supercell, j)
#             if site2.species_string == "O" and coord_number2 == 5 and supercell.get_distance(i,j) >= 18:
#                 flag = 1
#                 print(f"Atom {i} ({site.species_string}): Coordination Number = {coord_number}")
#                 print(f"Atom {j} ({site.species_string}): Coordination Number = {coord_number}")
                
#                 supercell3.remove(site2)
#                 break

# supercell3.to(fmt="poscar", filename = "Defected2.vasp")

                
