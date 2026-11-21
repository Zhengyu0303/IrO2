#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 09:15:33 2025

@author: zhengyuliu
"""

import os
from pymatgen.core import Structure
import numpy as np
from pymatgen.io.vasp import Poscar

# Load the bulk structure from a POSCAR file
bulk_structure = Structure.from_file("POSCAR.vasp")

from pymatgen.core.surface import SlabGenerator
from pymatgen.analysis.local_env import CutOffDictNN

# Define the Miller index for the surface you want
miller_index = (1, 0, 0)  # Example: (1, 1, 1) plane

for i in np.linspace(30, 30, 1):
    for j in np.linspace(10, 40, 7):
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
        #supercell.to(fmt = "poscar", filename=f"supercell{i:.0f}.vasp")

        

        # Define nearest neighbor cutoffs for Mg and O atoms (adjust these based on your structure)
        cutoff_nn = CutOffDictNN({("Mg", "O"): 2.5, ("O", "Mg"): 2.5})
        supercell2 = supercell.copy()
        distances = {}
        
        print(f"{i}, \n")
        
        remove1 = 0
        
        for k, site in enumerate(supercell):
            coord_number = cutoff_nn.get_cn(supercell, k)
            if site.species_string == "O" and coord_number == 5:
                remove1 = k
                #supercell2.remove(site)
                print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}\n")
                for l, site2 in enumerate(supercell):
                    if site2.species_string == "O" and cutoff_nn.get_cn(supercell, l) == 5:
                        distances[l] = supercell.get_distance(k,l)
                        
                break  

        same_surface = sorted(distances.values())[len(distances)//2-1]
        different_surface = sorted(distances.values())[len(distances)-1]

        for key in distances.keys():
            if distances[key] == different_surface:
                print(f"{key}, \n")
                #supercell2.remove_sites([key, remove1]) #Here we remove 2 atoms on difference surfaces
                supercell2.remove_sites([remove1])
                
                break
        
        # z_coords = [site.coords[2] for site in supercell2]
        # z_coords = np.array(z_coords)

        # # Define a cutoff distance from top/bottom to identify surface atoms
        # z_min, z_max = z_coords.min(), z_coords.max()
        # surface_tol = 1.0  # Å
        
        # surface_atoms = []
        # for k, z in enumerate(z_coords):
        #     if z > z_max - surface_tol or z < z_min + surface_tol:
        #         print(k,"\n")
        #         surface_atoms.append(k)
        #         #slabs[0].to(fmt="poscar", filename=f"mgo{i:.0f}_{j:.0f}_POSCAR_slab.vasp")
        # selective_dynamics = []
        
        # for s in range(len(supercell2)):
        #     if s in surface_atoms:
        #         selective_dynamics.append([True, True, True])  # Surface atoms can relax
        #     else:
        #         selective_dynamics.append([False, False, False])
        
        
        z_coords = [site.coords[2] for site in supercell2]
        
        l = len(z_coords)
        
        if l % 2 == 1:
            z_middle = sorted(z_coords)[l//2]
        else:
            z_middle = sorted(z_coords)[l//2]/2 + sorted(z_coords)[l//2 - 1]/2

        # Define a tolerance for middle layer selection (adjust if needed)
        tol = 1.2
        middle_atoms = [s for s, site in enumerate(supercell2) if abs(site.coords[2] - z_middle) < tol]
        print("middle atoms:", middle_atoms, "\n")
        # Step 5: Apply Selective Dynamics (Fix middle layer)
        selective_dynamics = [[False, False, False] if mm in middle_atoms else [True, True, True] for mm in range(len(supercell2))]
        #supercell2.to(fmt="poscar", filename = "2_defects.vasp")
        
        poscar = Poscar(supercell2, selective_dynamics=selective_dynamics)
        
        poscar.write_file(f"charged{j:.0f}.vasp")
        
        
        
        
        
        
        
        