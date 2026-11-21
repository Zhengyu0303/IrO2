#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 09:09:47 2026

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
slab_thickness = 25
vacuum_thickness = 10

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



##Now the PRISTINE slab has been created. 

#----Add-Defects-------------


def oxygen_vacancy_index(slab, cutoff_nn, surface = "top"):
    
    ##Returns a copy of the slab with the oxygen vacancy created at the top surface.
    ##Maybe we can reuse it a few times to create more oxygen vacancies
    ##Returns a different slab
    
    
    z_coords = [site.frac_coords[2] for site in slab]
    bridge_oxygens = []
    
    if surface == "top":
        z_ref = max(z_coords)
    elif surface == "bottom":
        z_ref = min(z_coords)
    
    for k, site in enumerate(slab):
        coord_number = cutoff_nn.get_cn(slab, k)
        if site.species_string == "O" and coord_number == 2 and abs(site.frac_coords[2] - z_ref)<= 0.005: 
            #This is to make sure that the oxygen removed is undercoordinated and thus at the bridge positions
            #Also, we made sure that the oxygen removed here sits on the top surface
            remove1 = k
            bridge_oxygens.append(remove1)
            print("*******************")
            print(f"Bridge Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
            #break
    
    
    return bridge_oxygens



#These are the 2 oxygen atoms to be removed
slab_supercell = slab*[2, 2, 1].copy()

pristine = slab_supercell = slab*[2, 2, 1]

slab_supercell.to(fmt = "poscar", filename = 'slab_supercell.vasp')


#----Find--the-Inversion-Centre----

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def find_inversion_centres(structure:Structure):
    
    centres = []
    
    analyzer = SpacegroupAnalyzer(structure)
    symops = analyzer.get_symmetry_operations()

    for op in symops:
        # Inversion has a rotation matrix of -I
        if (op.rotation_matrix == -np.eye(3)).all():
            # Translation vector gives the inversion centre at t/2
            inversion_centre = op.translation_vector / 2
            centres.append(inversion_centre)
            print("--------------------------")
            print(f"Inversion centre at fractional coords: {inversion_centre}\n")
    
    return centres

inv_centres = find_inversion_centres(slab_supercell)

frac_positions = np.array([site.frac_coords for site in slab_supercell])

bridge_oxygens_top = oxygen_vacancy_index(slab_supercell, cutoff_nn)

bridge_oxygens_bottom = oxygen_vacancy_index(slab_supercell, cutoff_nn, "bottom")



#symm_defect = slab_supercell.copy()
asymm_defect = slab_supercell.copy()

##Manually removed the sites we picked!!

#symm_defect.remove_sites([82,233])
asymm_defect.remove_sites([bridge_oxygens_top[0]])


#symm_defect.to(fmt = "poscar", filename = "symm_defected_slab.vasp")


#----Add-Selective-Dynamics-------

#This is to add selective dynamics
def freeze_middle_layer(structure: Structure, filename, write_struc = True, tol = 1.2):
    
    z_coords = [site.coords[2] for site in structure]
    
    unique_list = list(dict.fromkeys(round(x, 4) for x in z_coords))
                       
    l = len(unique_list)

    if l % 2 == 1:
        z_middle = sorted(unique_list)[l//2]
    else:
        z_middle = sorted(unique_list)[l//2]/2 + sorted(unique_list)[l//2 - 1]/2
        
    
    tol = 1.2
    middle_atoms = [s for s, site in enumerate(structure) if abs(site.coords[2] - z_middle) < tol]
    print("middle atoms:", middle_atoms, "\n")
    # Step 5: Apply Selective Dynamics (Fix middle layer)
    selective_dynamics = [[False, False, False] if mm in middle_atoms else [True, True, True] for mm in range(len(structure))]
    
    structure_sdy = Poscar(structure, selective_dynamics=selective_dynamics)
    
    #return structure_sdy
    if write_struc:
        structure_sdy.write_file(f"./{filename}.vasp")
    else:
        return structure_sdy
    
    
#freeze_middle_layer(symm_defect, "symm_defect")
freeze_middle_layer(asymm_defect, "asymm_defect")
freeze_middle_layer(slab_supercell, "pristine")

pristine_slab = freeze_middle_layer(slab_supercell, "asymm_defect", 0)

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




#Reaction---coordiantes------

import numpy as np
from pymatgen.core import Molecule
from pymatgen.analysis.adsorption import AdsorbateSiteFinder

def find_ir_cus(slab, target_cn=5, cutoff=2.3):
    """Indices of Ir atoms coordinated to exactly `target_cn` O atoms
    within `cutoff` Angstrom (bulk-like Ir in rutile IrO2 is 6-fold;
    surface Ir_cus drops to 5-fold)."""
    out = []
    for i, site in enumerate(slab):
        if site.species_string != "Ir":
            continue
        n_o = sum(1 for nb in slab.get_neighbors(site, r=cutoff) if nb.species_string == "O")
        if n_o == target_cn:
            out.append(i)
    return out

def add_oh_on_ir(slab, ir_index=None, distance=2.0, target_cn=5, cutoff=2.3):
    """
    Place *OH on a 5-fold-coordinated Ir (Ir_cus) site.

    ir_index : specific site to use; if None, picks the highest-z
               Ir among those matching `target_cn`
    """
    if ir_index is None:
        candidates = find_ir_cus(slab, target_cn, cutoff)
        assert candidates, f"no Ir site found with O coordination == {target_cn}"
        ir_index = max(candidates, key=lambda i: slab[i].coords[2])
    else:
        n_o = sum(1 for nb in slab.get_neighbors(slab[ir_index], r=cutoff) if nb.species_string == "O")
        assert slab[ir_index].species_string == "Ir", f"site {ir_index} is not Ir"
        assert n_o == target_cn, f"site {ir_index} has O coordination {n_o}, expected {target_cn}"

    ads_coord = slab[ir_index].coords + [0,0,distance]
    
    OH = Molecule(["O", "H"], [[0, 0, 0], [0, 0, 0.97]])
    O   = Molecule(["O"], [[0, 0, 0]])
    OOH = Molecule(["O", "O", "H"], [[0, 0, 0], [0, 0, 1.44], [0, 0.85, 1.99]])
    
    asf = AdsorbateSiteFinder(slab)
    return asf.add_adsorbate(OOH, ads_coord, reorient=True)


#add_OOH = add_oh_on_ir(slab_supercell)

#freeze_middle_layer(add_oh_on_ir(slab_supercell), "OOH_attached")

#Ir_cuss = find_ir_cus(asymm_defect, target_cn=5, cutoff=2.3)



def find_upper_cus_ir(slab, cus_cn = 5, cutoff=2.3):
    """Indices of all coordinatively unsaturated (cus) Ir atoms on the
    upper surface of the slab (i.e. Ir with fewer than bulk_cn O
    neighbors, restricted to the top half of the slab by z-height)."""
    all_z = [site.coords[2] for site in slab]
    mid_z = (max(all_z) + min(all_z)) / 2

    cus_ir = []
    for i, site in enumerate(slab):
        if site.species_string != "Ir":
            continue
        if site.coords[2] <= mid_z:
            continue  # lower surface, skip
        n_o = sum(1 for nb in slab.get_neighbors(site, r=cutoff) if nb.species_string == "O")
        #if n_o < bulk_cn:
        if n_o == cus_cn:
            cus_ir.append(i)
    return cus_ir


def find_ir_not_bonded_to_bridge_o(slab, bridge_o_indices, cutoff=2.3):
    """Indices of Ir atoms that are NOT bonded (within `cutoff` Å) to
    any of the given bridging-O sites."""
    bridge_coords = [slab[i].coords for i in bridge_o_indices]
    result = []
    for i, site in enumerate(slab):
        if site.species_string != "Ir":
            continue
        o_neighbors = [nb.coords for nb in slab.get_neighbors(site, r=cutoff) if nb.species_string == "O"]
        bonded_to_bridge = any(
            any(np.allclose(nc, bc, atol=1e-3) for bc in bridge_coords)
            for nc in o_neighbors
        )
        if not bonded_to_bridge:
            result.append(i)
    return result

def filter_not_bridge_bonded(slab, ir_indices, bridge_o_indices, cutoff=2.3):
    """From a list of Ir indices, keep only those with ZERO bonds
    (within `cutoff`) to any of the given bridging-O site indices —
    if there's even one connection, that Ir is dropped."""
    bridge_set = set(bridge_o_indices)
    result = []
    for i in ir_indices:
        neighbor_indices = {nb.index for nb in slab.get_neighbors(slab[i], r=cutoff)}
        if neighbor_indices.isdisjoint(bridge_set):
            result.append(i)
    return result


def unique_by_symmetry(slab, ir_indices, threshold=0.1):
    """Reduce a list of Ir site indices down to symmetrically distinct
    representatives, using the slab's own symmetry operations."""
    if not ir_indices:
        return []
    asf = AdsorbateSiteFinder(slab)
    coords = np.array([slab[i].coords for i in ir_indices])
    reduced_coords = asf.symm_reduce(coords, threshold=threshold)
    unique_indices = []
    for rc in reduced_coords:
        i_match = min(ir_indices, key=lambda i: np.linalg.norm(slab[i].coords - rc))
        unique_indices.append(i_match)
    return unique_indices


def find_upper_cus_ir(slab, cus_cn = 5, cutoff=2.3):
    """Indices of all coordinatively unsaturated (cus) Ir atoms on the
    upper surface of the slab (i.e. Ir with fewer than bulk_cn O
    neighbors, restricted to the top half of the slab by z-height)."""
    all_z = [site.coords[2] for site in slab]
    mid_z = (max(all_z) + min(all_z)) / 2

    cus_ir = []
    for i, site in enumerate(slab):
        if site.species_string != "Ir":
            continue
        if site.coords[2] <= mid_z:
            continue  # lower surface, skip
        n_o = sum(1 for nb in slab.get_neighbors(site, r=cutoff) if nb.species_string == "O")
        #if n_o < bulk_cn:
        if n_o == cus_cn:
            cus_ir.append(i)
    return cus_ir



Ir_cuss = find_upper_cus_ir(asymm_defect)

bridge_oxygens_left = oxygen_vacancy_index(asymm_defect, cutoff_nn)

ir_not_bridge_bonded = filter_not_bridge_bonded(asymm_defect, Ir_cuss, bridge_oxygens_left)

unique_ir = unique_by_symmetry(asymm_defect, ir_not_bridge_bonded)

print(unique_ir)


Ir_cus_sites = find_upper_cus_ir(pristine)
O_bridge_sites = oxygen_vacancy_index(pristine, cutoff_nn)

memory = {1:[[-1], [0], [1]]}

def generate_occupation_string(length, memory):
    
    if length in memory:
        
        return memory[length]
    
    else:
        last_one = generate_occupation_string(length - 1, memory)
        results = []
        
        for occupancy_list in last_one:
            results.append(occupancy_list + [-1])
            results.append(occupancy_list + [0])
            results.append(occupancy_list + [1])
        
        memory[length] = results
        
        return results

length = len(Ir_cus_sites)

Ir_occupacy_string = generate_occupation_string(length, memory)

#Get bridge oxygen occupation string. Be careful of the max number of vacancy sites

max_num_vac = 1
O_occupancy_string = []

for occupancy in Ir_occupacy_string:
    count = 0
    for o in occupancy:
        if o == -1:
            count += 1
    
    if count <= max_num_vac:
        O_occupancy_string.append(occupancy)
    
#Now we have got the all the possible occupancy needed and we need to
#!!! FILTER THE REPEAT ONES ACCORDING TO SYMMETRY
#We can either do it with structure matcher or we can 


OH = Molecule(["O", "H"], [[0, 0, 0], [0, 0, 0.97]])
O   = Molecule(["O"], [[0, 0, 0]])
OOH = Molecule(["O", "O", "H"], [[0, 0, 0], [0, 0, 1.44], [0, 0.85, 1.99]])

def add_adsorpent(slab, ir_coord, adsorpent=O, distance=2.0):
    ads_coord = np.array(ir_coord) + [0, 0, distance]# * slab.normal

    return AdsorbateSiteFinder(asymm_defect).add_adsorbate(adsorpent, ads_coord, reorient=True)


def get_adsorpent_positions(Ir_occupancy, Ir_cus, O_occupancy, O_bri):
    
    OH_sites = []
    O_sites = []
    H_sites = []
    vac_sites = []
    
    for i in range(len(Ir_cus)):
        if Ir_occupancy[i] == 1:
            OH_sites.append(Ir_cus[i])
        elif Ir_occupancy[i] == -1:
            O_sites.append(Ir_cus[i])
    
    for i in range(len(O_bri)):
        if O_occupancy[i] == 1:
            H_sites.append(O_bri[i])
        elif O_occupancy[i] == -1:
            vac_sites.append(O_bri[i])
    
    return OH_sites, O_sites, H_sites, vac_sites


Ir_test =Ir_occupacy_string[23]
O_test = O_occupancy_string[13]

test_sites = get_adsorpent_positions(Ir_test, Ir_cus_sites, O_test, O_bridge_sites)



# oh_structures = {}
# for idx, Ir_idx in enumerate(unique_ir):
#     oh_structures[idx] = add_adsorpent(asymm_defect, asymm_defect[Ir_idx].coords, O)
#     oh_structures[idx].to(fmt="poscar", filename=f"IrO2_O{idx}.vasp")

test_struc = {}
for idx, Ir_idx in enumerate(test_sites[0]):
    test_struc[idx] = add_adsorpent(pristine, pristine[Ir_idx].coords, OH)
    test_struc[idx].to(fmt="poscar", filename=f"test{idx}.vasp")







