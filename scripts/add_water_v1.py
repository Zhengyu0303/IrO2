#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:07:34 2026

@author: zhengyuliu
"""

from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np
from pymatgen.core import Structure, Molecule
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
import os

from pymatgen.analysis.local_env import CutOffDictNN

bulk_structure = Structure.from_file("POSCAR.vasp")  # You can replace with a CIF file

cutoff_nn = CutOffDictNN({("Ir", "O"): 2.7, ("O", "Ir"): 2.7})
# # Step 2: Define slab parameters
miller_index = (1, 1, 0) 



slabgen = SlabGenerator(
    bulk_structure,
    miller_index=miller_index,
    min_slab_size=40,  # Thickness of the slab in Å
    min_vacuum_size=30,  # Thickness of the vacuum layer in Å
    lll_reduce=True,
    reorient_lattice=True,
    center_slab=True
    
)

slabs = slabgen.get_slabs()
slab = slabs[1]*[2,2,1]

supercell = slab.copy() #This is for creating defects





#_____Create a vacancy on the top surface_____

z_coords = [site.frac_coords[2] for site in slab]
z_mean = (max(z_coords) + min(z_coords))/2#np.mean(z_coords)

# Add dynamics

seldyn = []
for site in slab:
    if site.frac_coords[2] < z_mean:
        seldyn.append([False, False, False])  # Bottom: frozen
    else:
        seldyn.append([True, True, True])     # Top: relaxed

for k, site in enumerate(slab):
    coord_number = cutoff_nn.get_cn(supercell, k)
    if site.species_string == "O" and coord_number == 2 and abs(site.frac_coords[2] - max(z_coords))<= 0.005:
        remove1 = k
        print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
        break
    
##Sort that into reusable functions

def create_oxygen_vacancy(slab):
    
    ##Returns a copy of the slab with the oxygen vacancy created at the top surface.
    ##Maybe we can reuse it a few times to create more oxygen vacancies
    
    slab_copy = slab.copy()
    
    z_coords = [site.frac_coords[2] for site in slab]
    #z_mean = (max(z_coords) + min(z_coords))/2#np.mean(z_coords)
    
    for k, site in enumerate(slab):
        coord_number = cutoff_nn.get_cn(supercell, k)
        if site.species_string == "O" and coord_number == 2 and abs(site.frac_coords[2] - max(z_coords))<= 0.005:
            remove1 = k
            print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
            break
    
    slab_copy.remove_sites([remove1])
    
    return slab_copy



supercell.remove_sites([remove1])

poscar = Poscar(supercell, selective_dynamics=seldyn)

#____________Add Water_________

water_coords = [
    [0.000000,  0.000000,  0.000000],  # O atom at the origin
    [0.763239,  0.477047,  0.000000],  # H atom
    [-0.763239, 0.477047,  0.000000]   # H atom
]
water = Molecule(["O", "H", "H"], water_coords)

print("Running Delaunay triangulation to find adsorption sites...")
asf = AdsorbateSiteFinder(supercell)

sites = asf.find_adsorption_sites()

# adsorbed_structures = asf.generate_adsorption_structures(
#     water, 
#     repeat=[1, 1, 1],     # Do not make a larger supercell
#     find_args={"distance": 2.3} 
# )

site_coords_list = sites['all']#[all_ir_cus_sites[0], all_ir_cus_sites[1], all_ir_cus_sites[2]]

#Or we can choose any combination from them lol

from itertools import combinations

all_sites = sites['all']
#site_coords_list = 

def add_adsporpents(slab, site_coords_list):
    
    modified_slab = slab.copy()
    
    for i, site_coord in enumerate(site_coords_list):
        
        # CRITICAL: Reinitialize AdsorbateSiteFinder after each addition
        asf_temp = AdsorbateSiteFinder(modified_slab)
        
        # Add water at this site
        modified_slab = asf_temp.add_adsorbate(water, ads_coord=site_coord)
    
    return modified_slab

def get_structures_with_adsorpents(all_sites, num_of_adsorpents, slab):
    
    #Maybe we can do the try thing later to avoid errors
    all_combinations = list(combinations(all_sites, num_of_adsorpents)) 
    
    adsorbed_structures = []
    for site_list in all_combinations:
        adsorbed_structures.append(add_adsporpents(slab, site_list))
    
    return adsorbed_structures

num_of_water = 2

modified_slabs = get_structures_with_adsorpents(all_sites, num_of_water, supercell)


output_dir = f"water_defect{num_of_water}"
os.makedirs(output_dir, exist_ok=True)

for index, struct in enumerate(modified_slabs):
    filename = f"{output_dir}/IrO2_water_{index+1}.vasp"
    struct.to(fmt="poscar", filename=filename)
    print(f"Saved: {filename}")






