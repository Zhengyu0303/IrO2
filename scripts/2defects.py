#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:40:14 2025

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

for i in np.linspace(10, 100, 1):
    for j in np.linspace(15, 15, 1):
       # os.system(f"mkdir mgo{i:.0f}_{j:.0f}")
        slabgen = SlabGenerator(
            initial_structure=bulk_structure,
            miller_index=miller_index,
            min_slab_size=i,  # Thickness of the slab in Å
            min_vacuum_size=j,  # Thickness of the vacuum layer in Å
            center_slab=True
            
        )

        slabs = slabgen.get_slabs()
        structure = slabs[0]
        supercell = structure * [2, 2, 1]
        ##We find the O with lower cn and then delete it 
        supercell.to(fmt = "poscar", filename="supercell.vasp")

        from pymatgen.analysis.local_env import CutOffDictNN

        # Define nearest neighbor cutoffs for Mg and O atoms (adjust these based on your structure)
        cutoff_nn = CutOffDictNN({("Mg", "O"): 2.5, ("O", "Mg"): 2.5})
        supercell2 = supercell.copy()
        distances = {}
        
        for k, site in enumerate(supercell):
            coord_number = cutoff_nn.get_cn(supercell, k)
            if site.species_string == "O" and coord_number == 5:
                supercell2.remove(site)
                for l, site2 in enumerate(supercell):
                    if site2.species_string == "O" and cutoff_nn.get_cn(supercell, l) == 5:
                        distances[l] = supercell.get_distance(k,l)
                        print(f"Atom {l} ({site.species_string}): Coordination Number = {coord_number}\n")
                break  

        same_surface = sorted(distances.values())[len(distances)//2-1]
        different_surface = sorted(distances.values())[len(distances)-1]

        for key in distances.keys():
            if distances[key] == different_surface:
                supercell2.remove_sites([key])
                break
                
        supercell2.to(fmt="poscar", filename = "2_defects.vasp")
        
        
        
        
        
        
        
        
        
        
        
        