#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 20:49:11 2025

@author: zhengyuliu
"""

from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np

# Step 1: Load bulk structure from a CIF or POSCAR file
bulk_structure = Structure.from_file("POSCAR.vasp")  # You can replace with a CIF file

# Step 2: Define slab parameters
miller_index = (1, 1, 0)  # Change as needed
slab_thickness = 40  # Thickness in angstroms
vacuum_thickness = 20  # Vacuum thickness in angstroms
lattice_tol = 0.1  # Tolerance for finding symmetric slabs

# Step 3: Generate slab
slabgen = SlabGenerator(
    bulk_structure,
    miller_index=miller_index,
    min_slab_size=slab_thickness,
    min_vacuum_size=vacuum_thickness,
    lll_reduce=True,
    reorient_lattice=True,
    center_slab=True # Ensures symmetric slab
    )

slabs = slabgen.get_slabs()

# Select the first generated slab
slab = slabs[1]*[2,2,1]

# Step 4: Identify middle layer atoms
z_coords = [site.coords[2] for site in slab]
z_mean = np.mean(z_coords)

# Define a tolerance for middle layer selection (adjust if needed)
tol = 2
middle_atoms = [i for i, site in enumerate(slab) if abs(site.coords[2] - z_mean) < tol]

# Step 5: Apply Selective Dynamics (Fix middle layer)
selective_dynamics = [[False, False, False] if i in middle_atoms else [True, True, True] for i in range(len(slab))]

# Step 6: Write the POSCAR with constraints
poscar = Poscar(slab, selective_dynamics=selective_dynamics)
poscar.write_file("../defect/slab.vasp")

print(f"Slab with Miller index {miller_index} created and middle layer fixed.")