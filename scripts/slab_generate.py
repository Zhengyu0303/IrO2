#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:49:05 2025

@author: zhengyuliu
"""

from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np

bulk_structure = Structure.from_file("CONTCAR.vasp")  # You can replace with a CIF file

# # Step 2: Define slab parameters
miller_index = (1, 1, 0) 

for i in np.linspace(15,60,1):#(5, 60, 12):
    for j in np.linspace(15,50,1):#(5, 50, 10):
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
        slab = slabs[1]*[2, 2, 1]

        # Step 4: Identify middle layer atoms
        z_coords = [site.coords[2] for site in slab]
        z_mean = np.mean(z_coords)

        # Define a tolerance for middle layer selection (adjust if needed)
        tol = 1.9
        middle_atoms = [i for i, site in enumerate(slab) if abs(site.coords[2] - z_mean) < tol]

        # Step 5: Apply Selective Dynamics (Fix middle layer)
        selective_dynamics = [[False, False, False] if i in middle_atoms else [True, True, True] for i in range(len(slab))]

        # Step 6: Write the POSCAR with constraints
        poscar = Poscar(slab, selective_dynamics=selective_dynamics)
        poscar.write_file(f"./slab{i:.0f}_{j:.0f}.vasp")

# slab_thickness = 5  # Thickness in angstroms
# vacuum_thickness = 15  # Vacuum thickness in angstroms
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
# slab = slabs[1]

# poscar = Poscar(slab)
# poscar.write_file("../slab/slab_test.vasp")