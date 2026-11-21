#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:43:58 2026

@author: zhengyuliu
"""

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Slab
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np

from pymatgen.analysis.local_env import CutOffDictNN


#Here are all the parameters for this structure

bulk_structure = Structure.from_file("POSCAR.vasp")
cutoff_nn = CutOffDictNN({("Ir", "O"): 2.7, ("O", "Ir"): 2.7})
miller_index = (1, 1, 0)
slab_thickness = 20
vacuum_thickness = 20

#----------------

#This is to create the slab

slabgen = SlabGenerator(
    bulk_structure,
    miller_index=miller_index,
    min_slab_size=slab_thickness,  # Thickness of the slab in Å
    min_vacuum_size=vacuum_thickness,  # Thickness of the vacuum layer in Å
    lll_reduce=True,
    reorient_lattice=True,
    center_slab=True
    
)

slabs = slabgen.get_slabs()

#-----------Symmetry-------------
#There might be many slabs generated and we need to select the one with inversion symmetry

#Here is also how we deal with the inversion symmetry.
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

slab_candidates = []

for index, slab in enumerate(slabs):

    #Initialize the SpacegroupAnalyzer. Symprec is the tolerance for finding symmetry operations
    analyzer = SpacegroupAnalyzer(slab, symprec=0.01)
    has_inversion = analyzer.is_laue()
    if has_inversion:
        slab_candidates.append(slab)
        print(f"Slab #{index} has inversion symmetry. Added")
    else:
        print(f"Slab #{index} doesn't have inversion symmetry. Removed")
    
slab = slab_candidates[0]
slab.to(fmt="poscar", filename="slab.vasp")




##Now the PRISTINE slab has been created. 

#----Add-Defects-------------


def oxygen_vacancy_index(slab, cutoff_nn):
    
    ##Returns a copy of the slab with the oxygen vacancy created at the top surface.
    ##Maybe we can reuse it a few times to create more oxygen vacancies
    ##Returns a different slab
    
    #slab_copy = slab.copy()
    
    z_coords = [site.frac_coords[2] for site in slab]
    #z_mean = (max(z_coords) + min(z_coords))/2#np.mean(z_coords)
    bridge_oxygens = []
    
    for k, site in enumerate(slab):
        coord_number = cutoff_nn.get_cn(slab, k)
        if site.species_string == "O" and coord_number == 2 and abs(site.frac_coords[2] - max(z_coords))<= 0.005: 
            #This is to make sure that the oxygen removed is undercoordinated and thus at the bridge positions
            #Also, we made sure that the oxygen removed here sits on the top surface
            remove1 = k
            bridge_oxygens.append(remove1)
            print(f"Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
            #break
    
    #slab_copy.remove_sites([remove1])
    
    return bridge_oxygens
##Return the site so it is easier to find the inversion spot, yayyy

def find_inversion_partner(structure: Structure, site_index: int, tol=0.1):
    
    frac_positions = np.array([site.frac_coords for site in structure])
    centre_frac = frac_positions.mean(axis=0)
    
    site_frac = np.array([0, 0.125, 0])#frac_positions[site_index]
    inv_frac = 2 * centre_frac - site_frac
    inv_frac %= 1.0  # keep in [0,1) — usually not needed for slab interior
    
    for i, site in enumerate(structure):
        if i == site_index:
            continue
        if site.specie.symbol == "O" or site.specie.symbol == "Ir":
            this_site = site.frac_coords
            
            diff = site.frac_coords - inv_frac
            diff -= np.round(diff)  # minimal image
            dist = np.linalg.norm(structure.lattice.get_cartesian_coords(diff))
            if dist < tol:
                print("Inversion site found", site.frac_coords)
                return i #Returns the site index
                #return i, site
    return None


def find_inversion_partners(structure: Structure, site_indices: int, tol=0.1):
    
    inv_indices = []
    
    for index in site_indices:
        
        inv_index = find_inversion_partner(structure, index)
        inv_indices.append(inv_index)
        
    return inv_indices
    


###We should find the inversion site first before removing anything!!!!!

#These are the 2 oxygen atoms to be removed
slab_supercell = slab*[2, 2, 1]
slab_supercell.to(fmt = "poscar", filename = 'supercell.vasp')


#----Find--the-Inversion-Centre----

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


analyzer = SpacegroupAnalyzer(slab_supercell)
symops = analyzer.get_symmetry_operations()

for op in symops:
    # Inversion has a rotation matrix of -I
    if (op.rotation_matrix == -np.eye(3)).all():
        # Translation vector gives the inversion centre at t/2
        inversion_centre = op.translation_vector / 2
        print(f"Inversion centre at fractional coords: {inversion_centre}")






bridge_oxygens = oxygen_vacancy_index(slab_supercell, cutoff_nn)
inv_oxygens = find_inversion_partners(slab_supercell, bridge_oxygens)

#Then select those with the smallest distance, considering PBC

# distances = []

# for i in range(len(bridge_oxygens)):
#     d = slab_supercell.get_distance(bridge_oxygens[i], inv_oxygens[i])
#     distances.append(d)
    
# max_val = max(distances)
# max_idx = distances.index(max_val)

supercell = slab_supercell.copy()
#supercell.remove_sites([bridge_oxygens[max_idx], inv_oxygens[max_idx]])

supercell.to(fmt = "poscar", filename = "symm_defected_slab.vasp")


#----Add-Selective-Dynamics-------

#In this case, we will freeze the middle 2 layers to ensure symmetry

z_coords = [site.coords[2] for site in supercell if site.specie.symbol == "Ir"]

unique_list = list(dict.fromkeys(round(x, 4) for x in z_coords))
                   
l = len(unique_list)

if l % 2 == 1:
    z_middle = sorted(unique_list)[l//2]
else:
    z_middle = sorted(unique_list)[l//2]/2 + sorted(unique_list)[l//2 - 1]/2

# Define a tolerance for middle layer selection (adjust if needed)

tol = 1.2
middle_atoms = [s for s, site in enumerate(supercell) if abs(site.coords[2] - z_middle) < tol]
print("middle atoms:", middle_atoms, "\n")
# Step 5: Apply Selective Dynamics (Fix middle layer)
selective_dynamics = [[False, False, False] if mm in middle_atoms else [True, True, True] for mm in range(len(supercell))]


#supercell2.to(fmt="poscar", filename = "2_defects.vasp")

def freeze_middle_layer(structure: Structure, tol = 1.2):
    
    z_coords = [site.coords[2] for site in structure]
    
    
    





#--------Add---Water-----

from pymatgen.core import Structure, Molecule
from pymatgen.analysis.adsorption import AdsorbateSiteFinder


water_coords = [
    [0.000000,  0.000000,  0.000000],  # O atom at the origin
    [0.763239,  0.477047,  0.000000],  # H atom
    [-0.763239, 0.477047,  0.000000]   # H atom
]
water = Molecule(["O", "H", "H"], water_coords)

# print("Running Delaunay triangulation to find adsorption sites...")
# asf = AdsorbateSiteFinder(supercell)









