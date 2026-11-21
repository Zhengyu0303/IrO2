#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 12:10:22 2025

@author: zhengyuliu
"""

from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np

from pymatgen.analysis.local_env import CutOffDictNN

# # Step 1: Load bulk structure from a CIF or POSCAR file
# bulk_structure = Structure.from_file("POSCAR.vasp")  # You can replace with a CIF file

# # Step 2: Define slab parameters
# miller_index = (1, 1, 0)  # Change as needed
# slab_thickness = 10  # Thickness in angstroms
# vacuum_thickness = 10  # Vacuum thickness in angstroms
# lattice_tol = 0.1  # Tolerance for finding symmetric slabs

# # Step 3: Generate slab
# slabgen = SlabGenerator(
#     bulk_structure,
#     miller_index=miller_index,
#     min_slab_size=slab_thickness,
#     min_vacuum_size=vacuum_thickness,
#     lll_reduce=True,
#     reorient_lattice=True,
#     center_slab=True # Ensures symmetric slab
#     )

# slabs = slabgen.get_slabs()

# # Select the first generated slab
# slab= slabs[1]*[2,2,1]

# supercell = slab.copy()

# cutoff_nn = CutOffDictNN({("Ir", "O"): 2.7, ("O", "Ir"): 2.7})

# for k, site in enumerate(slab):
#     coord_number = cutoff_nn.get_cn(supercell, k)
#     if site.species_string == "O" and coord_number == 2:
#         remove1 = k
#         print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
#         break

# supercell.remove_sites([remove1])
    

# # Step 4: Identify middle layer atoms
# z_coords = [site.coords[2] for site in supercell]
# z_mean = np.mean(z_coords)

# # Define a tolerance for middle layer selection (adjust if needed)
# tol = 2
# middle_atoms = [i for i, site in enumerate(supercell) if abs(site.coords[2] - z_mean) < tol]

# # Step 5: Apply Selective Dynamics (Fix middle layer)
# selective_dynamics = [[False, False, False] if i in middle_atoms else [True, True, True] for i in range(len(supercell))]

# # Step 6: Write the POSCAR with constraints
# poscar = Poscar(supercell, selective_dynamics=selective_dynamics)
# poscar.write_file("../defect/test_with_defect.vasp")

# # print(f"Slab with Miller index {miller_index} created and middle layer fixed.")

bulk_structure = Structure.from_file("POSCAR.vasp")  # You can replace with a CIF file

cutoff_nn = CutOffDictNN({("Ir", "O"): 2.7, ("O", "Ir"): 2.7})
# # Step 2: Define slab parameters
miller_index = (1, 1, 0) 

for i in np.linspace(4,4,1):#(5, 60, 12):
    for j in np.linspace(13,13,1):#(5, 50, 10):
       # os.system(f"mkdir mgo{i:.0f}_{j:.0f}")
        slabgen = SlabGenerator(
            bulk_structure,
            miller_index=miller_index,
            min_slab_size=i,  # Thickness of the slab in Å
            min_vacuum_size=j,  # Thickness of the vacuum layer in Å
            lll_reduce=True,
            reorient_lattice=True,
            center_slab=True
            
        )

        slabs = slabgen.get_slabs()
        slab = slabs[1]*[2,2,1]
        
        supercell = slab.copy()
        
        for k, site in enumerate(slab):
            coord_number = cutoff_nn.get_cn(supercell, k)
            if site.species_string == "O" and coord_number == 2:
                remove1 = k
                print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
                break
        
        supercell.remove_sites([remove1])
        
        # Step 4: Identify middle layer atoms
        z_coords = [site.coords[2] for site in slab]
        z_mean = np.mean(z_coords)

        # Define a tolerance for middle layer selection (adjust if needed)
        tol = 1.9
        middle_atoms = [i for i, site in enumerate(supercell) if abs(site.coords[2] - z_mean) < tol]

        # Step 5: Apply Selective Dynamics (Fix middle layer)
        selective_dynamics = [[False, False, False] if i in middle_atoms else [True, True, True] for i in range(len(slab))]

        # Step 6: Write the POSCAR with constraints
        poscar = Poscar(supercell, selective_dynamics=selective_dynamics)
        poscar.write_file(f"../defect/vacancy_1/slab{i:.0f}_{j:.0f}.vasp")



