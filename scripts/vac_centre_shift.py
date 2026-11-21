#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:59:44 2026

@author: zhengyuliu
"""

from pymatgen.core import Structure

# Load your structure
struct = Structure.from_file("IrO2_O1.vasp")

# 1. Identify the current slab center (as we did before)
z_coords = [site.frac_coords[2] for site in struct]
min_z = min(z_coords)
max_z = max(z_coords)
slab_center = (min_z + max_z) / 2

# 2. Calculate the shift to move the slab center to 0.0 (or 1.0)
# This will push the slab to the edge, placing the vacuum in the center
shift = 0.0 - slab_center

# 3. Apply the shift
struct.translate_sites(list(range(len(struct))), [0, 0, shift], frac_coords=True, to_unit_cell=True)

struct.to(fmt="POSCAR", filename="IrO2_O1_centred.vasp")

from pymatgen.io.xyz import XYZ

struct2 = Structure.from_file("IrO2_O1_centred.vasp")

XYZ(struct2).write_file("IrO2_O1_centred.xyz")