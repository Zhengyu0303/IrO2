#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:21:11 2026

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
slab_thickness = 15
vacuum_thickness = 15

#----------------

#This is to create the slab

slabgen = SlabGenerator(
    bulk_structure,
    miller_index=miller_index,
    min_slab_size=slab_thickness,  # Thickness of the slab in Å
    min_vacuum_size=vacuum_thickness,  # Thickness of the vacuum layer in Å
    lll_reduce=True,
    reorient_lattice=True,
    #center_slab=True
    
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

pristine = slab_supercell.copy()

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
memory2 = {1:[[0], [1]]}


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
    
    
def generate_occupation_string2(length, memory):
    
    if length in memory:
        
        return memory[length]
    
    else:
        last_one = generate_occupation_string2(length - 1, memory)
        results = []
        
        for occupancy_list in last_one:
            for m in memory[1]:
                results.append(occupancy_list + m)
        
        memory[length] = results
        
        return results

length = len(Ir_cus_sites)

Ir_occupacy_string = generate_occupation_string2(length, memory2)
O_occupacy_string0 = generate_occupation_string(length, memory)

#Get bridge oxygen occupation string. Be careful of the max number of vacancy sites

max_num_vac = 1
O_occupancy_string = []

for occupancy in O_occupacy_string0:
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


def modify_slab(slab, O_sites=(), OH_sites=(), H_sites=(), vacancies=(),
                d_IrO_O=1.70, d_IrO_OH=1.95, d_OH=0.98):
    """
    All indices refer to the ORIGINAL `slab` (pymatgen 0-based).

    O_sites   : Ir indices that get O*
    OH_sites  : Ir indices that get OH*
    H_sites   : indices of atoms (e.g. O_bri) that get an H on top
    vacancies : indices of atoms to delete

    Order of operations: add adsorbates first (appended to the end),
    then delete vacancies last. Positions are always read from the original slab.

    Returns
    -------
    new        : modified Structure
    added      : {"O": {site: [new idx]}, "OH": {site: [O idx, H idx]}, "H": {site: [new idx]}}
                 (indices are in `new`, i.e. after vacancies are removed)
    old_to_new : dict mapping every surviving original/added index -> index in `new`
    """
    O_sites, OH_sites, H_sites, vacancies = map(list, (O_sites, OH_sites, H_sites, vacancies))
    N = len(slab)

    # --- sanity checks ---
    for name, lst in [("O_sites", O_sites), ("OH_sites", OH_sites),
                      ("H_sites", H_sites), ("vacancies", vacancies)]:
        bad = [i for i in lst if not 0 <= i < N]
        if bad:
            raise IndexError(f"{name} {bad} out of range (slab has {N} atoms)")
        if len(set(lst)) != len(lst):
            raise ValueError(f"{name} contains duplicates: {lst}")
    if set(O_sites) & set(OH_sites):
        raise ValueError(f"Ir sites {sorted(set(O_sites) & set(OH_sites))} given both O and OH")
    used = set(O_sites) | set(OH_sites) | set(H_sites)
    if used & set(vacancies):
        raise ValueError(f"sites {sorted(used & set(vacancies))} get an adsorbate but are also vacancies")
    for i in O_sites + OH_sites:
        if slab[i].species_string != "Ir":
            raise ValueError(f"site {i} is {slab[i].species_string}, not Ir")

    # --- outward surface normal ---
    a, b, c = slab.lattice.matrix
    n = np.cross(a, b)
    n /= np.linalg.norm(n)
    if np.dot(n, c) < 0:
        n = -n

    # fill existing site properties (e.g. selective_dynamics) for new atoms
    defaults = {"selective_dynamics": [True, True, True], "magmom": 0.0}
    props = {k: defaults.get(k) for k in slab.site_properties} or None

    new = slab.copy()
    added = {"O": {}, "OH": {}, "H": {}}

    def add(species, xyz):
        new.append(species, xyz, coords_are_cartesian=True, properties=props)
        return len(new) - 1

    # --- 1. add adsorbates (appended -> original indices unchanged) ---
    for i in O_sites:
        added["O"][i] = [add("O", slab[i].coords + d_IrO_O * n)]
    for i in OH_sites:
        o = slab[i].coords + d_IrO_OH * n
        added["OH"][i] = [add("O", o), add("H", o + d_OH * n)]
    for i in H_sites:
        added["H"][i] = [add("H", slab[i].coords + d_OH * n)]

    # --- 2. remove vacancies last, and track the index shift ---
    vac = set(vacancies)
    keep = [j for j in range(len(new)) if j not in vac]
    old_to_new = {old: k for k, old in enumerate(keep)}
    if vacancies:
        new.remove_sites(sorted(vacancies))

    added = {kind: {site: [old_to_new[j] for j in idx] for site, idx in d.items()}
             for kind, d in added.items()}
    return new, added, old_to_new


##One test case

Ir_test =Ir_occupacy_string[1]
O_test = O_occupancy_string[1]



test_sites = get_adsorpent_positions(Ir_test, Ir_cus_sites, O_test, O_bridge_sites)

new, added, old_to_new = modify_slab(
    pristine,
    O_sites   = test_sites[0],
    OH_sites  = test_sites[1],
    H_sites   = test_sites[2],     # e.g. O_bri -> O_bri-H
    vacancies = test_sites[3],         # e.g. remove an O_bri
)
new.to(filename="test_case.vasp", fmt="poscar")

print(added)              # where the new atoms ended up in `new`
print(old_to_new[12])     # where original Ir 12 is now


import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def modify_slab(slab, O_sites=(), OH_sites=(), H_sites=(), vacancies=(),
                d_IrO_O=1.70, d_IrO_OH=1.95, d_OH=0.98):
    """All indices refer to the original clean slab (0-based)."""
    a, b, c = slab.lattice.matrix
    n = np.cross(a, b); n /= np.linalg.norm(n)
    if np.dot(n, c) < 0:
        n = -n
    defaults = {"selective_dynamics": [True, True, True], "magmom": 0.0}
    props = {k: defaults.get(k) for k in slab.site_properties} or None

    new = slab.copy()
    add = lambda sp, xyz: new.append(sp, xyz, coords_are_cartesian=True, properties=props)
    for i in O_sites:
        add("O", slab[i].coords + d_IrO_O * n)
    for i in OH_sites:
        o = slab[i].coords + d_IrO_OH * n
        add("O", o); add("H", o + d_OH * n)
    for i in H_sites:
        add("H", slab[i].coords + d_OH * n)
    if vacancies:
        new.remove_sites(sorted(vacancies))          # done last
    return new

##-----



def get_adsorpent_positions2(Ir_occupancy, Ir_cus, O_occupancy, O_bri):
    
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
    
    #return OH_sites, O_sites, H_sites, vac_sites
    return dict(O_sites=O_sites, OH_sites=OH_sites, H_sites=H_sites,vacancies=vac_sites)


#


import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def unique_configs(slab, site_groups, configs, symprec=0.1, tol=0.3):
    """Returns keep, counts, orbit, groups.
    keep   : index of the representative config of each unique group
    counts : how many configs in YOUR list fall in that group
    orbit  : true number of symmetry-equivalent configs (independent of your list)
    groups : all config indices in each group"""
    all_idx = [i for g in site_groups for i in g]
    pos = {i: k for k, i in enumerate(all_idx)}
    group_of = [k for k, g in enumerate(site_groups) for _ in g]
    frac = slab.frac_coords[all_idx]

    # symmetry ops of the clean slab -> permutations of the sites
    perms = set()
    for op in SpacegroupAnalyzer(slab, symprec=symprec).get_symmetry_operations(cartesian=False):
        moved, perm = op.operate_multi(frac), []
        for a, f in enumerate(moved):
            cand = [b for b in range(len(all_idx)) if group_of[b] == group_of[a]]
            d = frac[cand] - f; d -= np.round(d)
            dist = np.linalg.norm(slab.lattice.get_cartesian_coords(d), axis=1)
            j = int(np.argmin(dist))
            if dist[j] > tol:
                break
            perm.append(cand[j])
        else:
            if len(set(perm)) == len(perm):
                perms.add(tuple(perm))
    inv = [[p.index(b) for b in range(len(all_idx))] for p in perms]

    found, orbit_of = {}, {}                      # key -> [config indices]
    for k, cfg in enumerate(configs):
        lab = ["-"] * len(all_idx)
        for tag in ("O_sites", "OH_sites", "H_sites", "vacancies"):
            for i in cfg.get(tag, ()):
                lab[pos[i]] = tag
        images = {tuple(lab[q[b]] for b in range(len(lab))) for q in inv}
        key = min(images)
        if key not in found:
            found[key] = []
            orbit_of[key] = len(images)           # number of distinct equivalent configs
        found[key].append(k)

    groups = list(found.values())
    keep   = [g[0] for g in groups]
    counts = [len(g) for g in groups]
    orbit  = [orbit_of[key] for key in found]
    return keep, counts, orbit, groups



occupancy_dict = get_adsorpent_positions2(Ir_occupacy_string[1], Ir_cus_sites, O_occupancy_string[1], O_bridge_sites)
#There is one occupancy_dict for each occupancy configuration

all_site_configurations = []

for occupancy1 in Ir_occupacy_string:
    for occupancy2 in O_occupancy_string:
        occupancy_dict = get_adsorpent_positions2(occupancy1, Ir_cus_sites, occupancy2, O_bridge_sites)
        all_site_configurations.append(occupancy_dict)

Ir_cus = Ir_cus_sites.copy()
O_bri = O_bridge_sites.copy()


keep, counts, orbit, groups = unique_configs(pristine, [Ir_cus, O_bri], all_site_configurations)

for k, c, o in zip(keep, counts, orbit):
    print(f"config {k}: {c} in my list, degeneracy {o}")

keep_list = [all_site_configurations[k] for k in keep]
filtered_structs = [modify_slab(pristine, **all_site_configurations[k]) for k in keep]

##This is for writing the labels.txt file

##--------

KEYS = ['O_sites', 'OH_sites', 'H_sites', 'vacancies']

def site_counts(d):
    """{'O_sites': [], 'OH_sites': [], 'H_sites': [115], 'vacancies': [112]} -> '0 0 1 1'"""
    return ' '.join(str(len(d.get(k, []))) for k in KEYS)

def site_counts_list(dicts):
    """Apply site_counts to every dict in a list."""
    return [site_counts(d) for d in dicts]


site_indices = site_counts_list(keep_list)

with open('labels.txt', 'w') as f:
    
    for idx, struct in enumerate(filtered_structs):
    
        struct.to(filename=f"coverage{idx}.vasp", fmt="poscar")
        f.write(f"coverage{idx}"+" "+site_indices[idx]+f"{counts[idx]} "+"\n")

###--------







###Filter again with pymatgen

# import warnings
# from pymatgen.analysis.structure_matcher import StructureMatcher

# def matcher_filter(structs, ltol=0.2, stol=0.3, angle_tol=5):
#     """structs: list of Structures.
#     Returns (unique_structs, groups) where groups are lists of indices into `structs`;
#     the first index in each group is the one kept."""
#     sm = StructureMatcher(ltol=ltol, stol=stol, angle_tol=angle_tol,
#                           primitive_cell=False, scale=False, attempt_supercell=False)
#     id_to_idx = {id(s): i for i, s in enumerate(structs)}
#     with warnings.catch_warnings():
#         warnings.simplefilter("ignore")
#         groups = sm.group_structures(structs)
#     groups = sorted([sorted(id_to_idx[id(s)] for s in g) for g in groups])
#     unique = [structs[g[0]] for g in groups]
#     return unique, groups

# unique, groups = matcher_filter(filtered_structs)          # structs = your list
# print(f"{len(filtered_structs)} -> {len(unique)} unique")

# #Unique is the list of unique structures

# for idx, unique_struc in enumerate(unique):
#     unique_struc.to(fmt="poscar", filename=f"coverage{idx}.vasp")










