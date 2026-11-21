#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:54:15 2026

@author: zhengyuliu
"""

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Slab
from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
import numpy as np
from pymatgen.analysis.molecule_structure_comparator import CovalentRadius
from pymatgen.core import Structure

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


def oxygen_bridge_index(slab, cutoff_nn, surface = "top"):
    
    ##Returns a copy of the slab with the oxygen vacancy created at the top surface.
    ##Maybe we can reuse it a few times to create more oxygen vacancies
    ##Returns a different slab
    
    
    z_coords = [site.coords[2] for site in slab]
    distinct = np.unique(np.round(z_coords, 4))
    
    bridge_oxygens = []
    
    
    if surface == "top":
        z_ref = distinct[-1]#max(z_coords)
    elif surface == "bottom":
        z_ref = distinct[0]#min(z_coords)
    
    for k, site in enumerate(slab):
        coord_number = cutoff_nn.get_cn(slab, k)
        if site.species_string == "O"  and abs(site.coords[2] - z_ref)<= 0.05:# and coord_number == 2: 
            #This is to make sure that the oxygen removed is undercoordinated and thus at the bridge positions
            #Also, we made sure that the oxygen removed here sits on the top surface
            remove1 = k
            bridge_oxygens.append(remove1)
            print("*******************")
            print(f"Bridge Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
            #break
    
    
    return bridge_oxygens

def get_all_ir(slab, cus_cn = 5, cutoff=2.3, surface = "top"):
    """Indices of all coordinatively unsaturated (cus) Ir atoms on the
    upper surface of the slab (i.e. Ir with fewer than bulk_cn O
    neighbors, restricted to the top half of the slab by z-height)."""
    
    all_z = [site.coords[2] for site in slab]
    mid_z = (max(all_z) + min(all_z)) / 2
    
    z_coords = [site.coords[2] for site in slab]
    distinct = np.unique(np.round(z_coords, 4))
    
    if surface == "top":
        z_ref = distinct[-2]#max(z_coords)
    elif surface == "bottom":
        z_ref = distinct[1]#min(z_coords)

    all_ir = []

    for k, site in enumerate(slab):
        coord_number = cutoff_nn.get_cn(slab, k)
        if site.species_string == "Ir"  and abs(site.coords[2] - z_ref)<= 0.05:# and coord_number == 2: 
            #This is to make sure that the oxygen removed is undercoordinated and thus at the bridge positions
        #Also, we made sure that the oxygen removed here sits on the top surface
            remove1 = k
            all_ir.append(remove1)
            print("*******************")
            print(f"Ir Atom {k} ({site.species_string}): Coordination Number = {coord_number}, z coord = {site.frac_coords[2]}\n")
        #break
    return all_ir



def find_cus_ir(slab, cus_cn = 5, cutoff=2.3, surface = "top"):
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

# Bond cutoffs (Å) for the IrO2 / water system. Order of the pair doesn't matter.
from pymatgen.analysis.molecule_structure_comparator import CovalentRadius
from pymatgen.core import Structure

# Bond cutoffs (Å) for the IrO2 / water system. Order of the pair doesn't matter.
DEFAULT_CUTOFFS = {
    ("Ir", "O"): 2.4,
    ("Ir", "Ir"): 2.9,  # excludes the 3.16 Å Ir–Ir along c in rutile
    ("Ir", "H"): 1.8,
    ("O", "O"): 1.6,    # keeps O–O in *OOH / peroxo species
    ("O", "H"): 1.2,    # covalent O–H only, not hydrogen bonds
    ("H", "H"): 0.9,
}


def get_connected_atoms(structure: Structure, indices, cutoffs=None, tol=1.2,
                        exclude_input=False):
    """Return a sorted list of the indices of atoms bonded to any atom in `indices`.

    Args:
        structure: pymatgen Structure.
        indices: list of atom indices (0-based).
        cutoffs: optional dict {("A", "B"): r_max} that overrides/extends
            DEFAULT_CUTOFFS. Pairs not listed anywhere use
            tol * (sum of covalent radii).
        tol: tolerance factor for the covalent-radii fallback.
        exclude_input: if True, drop atoms that are themselves in `indices`.
    """
    cut = {frozenset(k): v for k, v in DEFAULT_CUTOFFS.items()}
    if cutoffs:
        cut.update({frozenset(k): v for k, v in cutoffs.items()})

    def pair_cutoff(a, b):
        key = frozenset((a, b))
        if key in cut:
            return cut[key]
        return tol * (CovalentRadius.radius[a] + CovalentRadius.radius[b])

    elements = {site.specie.symbol for site in structure}
    r_max = max(pair_cutoff(a, b) for a in elements for b in elements)

    connected = set()
    for i in indices:
        a = structure[i].specie.symbol
        for nb in structure.get_neighbors(structure[i], r_max):
            if nb.nn_distance <= pair_cutoff(a, nb.specie.symbol):
                connected.add(int(nb.index))

    if exclude_input:
        connected -= {int(i) for i in indices}
    return sorted(connected)
#These are the 2 oxygen atoms to be removed
slab_supercell = slab*[2, 2, 1].copy()
pristine = slab_supercell.copy()
pristine.to(fmt = "poscar", filename = "pristine.vasp")

Ir_cus_sites = find_upper_cus_ir(pristine)

O_bridge_sites = oxygen_bridge_index(pristine, cutoff_nn, "top")

O_to_remove = O_bridge_sites[0]

##Finhe Ir atom connected to this bridge Oxygen

##Function to do that
import networkx as nx
from pymatgen.analysis.graphs import StructureGraph
from pymatgen.analysis.local_env import CutOffDictNN

# Max bond lengths (Å) for IrO2 slabs with O / OH / OOH adsorbates.
# Element pairs not listed here are never treated as bonded.
DEFAULT_CUTOFFS = {("Ir", "O"): 2.3, ("O", "H"): 1.2, ("O", "O"): 1.6}


def connected_atoms(structure, index, cutoffs=None, exclude=None, direct_only=False):
    """Return the sorted indices of atoms bonded to structure[index].

    structure   : pymatgen Structure (or Slab)
    index       : index of the starting atom
    cutoffs     : {(el1, el2): max bond length in Å}; defaults to DEFAULT_CUTOFFS
    exclude     : element symbols to leave out of the search, e.g. ["Ir"] to
                  separate an adsorbate from the slab (the starting atom is always kept)
    direct_only : True  -> only the first neighbours
                  False -> every atom reachable through a chain of bonds

    The starting atom itself is not included in the result.
    """
    nn = CutOffDictNN(cutoffs or DEFAULT_CUTOFFS)
    sg = StructureGraph.from_local_env_strategy(structure, nn)
    g = nx.Graph(sg.graph.to_undirected())

    if exclude:
        g.remove_nodes_from(
            [k for k, site in enumerate(structure)
             if site.specie.symbol in exclude and k != index]
        )

    if direct_only:
        found = set(g.neighbors(index))
    else:
        found = nx.node_connected_component(g, index)
    return sorted(found - {index})

###End of function 



#Occupation String

memory_Ir = {1:[[-1], [1]]}
memory_O = {1:[[0], [1]]}

def generate_occupation_string(length, memory):
    
    if length in memory:
        
        return memory[length]
    
    else:
        last_one = generate_occupation_string(length - 1, memory)
        results = []
        
        for occupancy_list in last_one:
            for m in memory[1]:
                results.append(occupancy_list + m)
        
        memory[length] = results
        
        return results

##

from pymatgen.core import Structure, Molecule
from pymatgen.analysis.adsorption import AdsorbateSiteFinder


OH = Molecule(["O", "H"], [[0, 0, 0], [0, 0, 0.97]])
O   = Molecule(["O"], [[0, 0, 0]])
OOH = Molecule(["O", "O", "H"], [[0, 0, 0], [0, 0, 1.44], [0, 0.85, 1.99]])


######

from pymatgen.core import Structure

Irs_to_remove = connected_atoms(pristine, O_to_remove, direct_only=True)   # only atoms directly bonded to 48

removes1 = [Irs_to_remove[0], O_to_remove]
removes0 = [Irs_to_remove[0]]

##
prototype0 = pristine.copy()
prototype1 = pristine.copy()


prototype0.remove_sites(removes0)
prototype1.remove_sites(removes1)

prototype0.to(fmt = "poscar", filename = "prototype0.vasp")
prototype1.to(fmt = "poscar", filename = "prototype1.vasp")

##Now add coverages

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
    
    #return OH_sites, O_sites, H_sites, vac_sites
    return dict(O_sites=O_sites, OH_sites=OH_sites, H_sites=H_sites,vacancies=vac_sites)

import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

import numpy as np
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def unique_configs(structure, configs, symprec=0.1):
    """Return (unique, degeneracy) for a list of coverage dicts on `structure`."""
    symbols = np.array([site.specie.symbol for site in structure])
    heavy = Structure.from_sites([site for site in structure if site.specie.symbol != "H"])
    ops = SpacegroupAnalyzer(heavy, symprec=symprec).get_symmetry_operations()

    # Turn each symmetry operation into an index mapping: perm[i] = j
    fcoords = structure.frac_coords
    perms = []
    for op in ops:
        new = op.operate_multi(fcoords)
        perm = np.empty(len(structure), dtype=int)
        for el in np.unique(symbols):
            idx = np.where(symbols == el)[0]
            d = structure.lattice.get_all_distances(new[idx], fcoords[idx])
            perm[idx] = idx[d.argmin(axis=1)]
            if len(set(perm[idx])) != len(idx):  # mapping not one-to-one: skip this operation
                break
        else:
            perms.append(perm)

    # Canonical key = smallest version of the config over all symmetry operations
    keys = sorted({k for c in configs for k in c})
    unique, degeneracy, seen = [], [], {}
    for c in configs:
        key = min(tuple(tuple(sorted(int(p[i]) for i in c.get(k, []))) for k in keys)
                  for p in perms)
        if key in seen:
            degeneracy[seen[key]] += 1
        else:
            seen[key] = len(unique)
            unique.append(c)
            degeneracy.append(1)
    return unique, degeneracy


from pymatgen.analysis.structure_matcher import StructureMatcher



def build_structure(template, config, h_pool=(), d_IrO=1.75, d_IrOH=1.95, d_OH=0.98):
    """Build the structure for one coverage dict.

    O_sites / OH_sites / vacancies can be metal (Ir_cus) indices or O indices:
        Ir index : the adsorbate goes ON TOP of that Ir.
                   O_sites   -> terminal O (added at d_IrO above the Ir if the Ir is bare)
                   OH_sites  -> terminal OH (O at d_IrOH above the Ir, H at d_OH above the O)
                   vacancies -> Ir left bare (its terminal O/OH is removed if present; the Ir stays)
        O index  : O_sites -> O kept, its H removed; OH_sites -> H added on that O;
                   vacancies -> that O (and its H) removed.
    H_sites: an O index (e.g. O_bri) is protonated; an H index is kept, and H atoms listed in
    other configs' H_sites (h_pool) but not in this one are removed.
    """
    s = template.copy()
    symbols = [site.specie.symbol for site in s]
    up = np.array([0.0, 0.0, 1.0])

    def bonded_H(o):
        return [int(nb.index) for nb in s.get_neighbors(s[o], 1.2) if nb.specie.symbol == "H"]

    def top_O(m):
        """Terminal O sitting on top of metal m in the template, or None."""
        for nb in s.get_neighbors(s[m], 2.3):
            v = nb.coords - s[m].coords
            if nb.specie.symbol == "O" and v[2] > 0.8 * np.linalg.norm(v):
                return int(nb.index)
        return None

    keep_H = {i for i in config.get("H_sites", []) if symbols[i] == "H"}
    remove = set(h_pool) - keep_H
    add = []  # (species, cartesian coords)

    def set_state(i, state):
        if symbols[i] == "H":
            return
        o = i if symbols[i] == "O" else top_O(i)
        if state == "empty":
            if o is not None:
                remove.add(o)
                remove.update(set(bonded_H(o)) - keep_H)
            return
        if o is None:  # bare Ir: add the adsorbate on top
            if state == "O":
                add.append(("O", s[i].coords + d_IrO * up))
            else:
                o_pos = s[i].coords + d_IrOH * up
                add.append(("O", o_pos))
                add.append(("H", o_pos + d_OH * up))
            return
        hs = set(bonded_H(o))
        if state == "O":
            remove.update(hs - keep_H)
        elif not hs - remove:  # OH wanted and no H left on this O
            add.append(("H", s[o].coords + d_OH * up))

    for i in config.get("O_sites", []):
        set_state(i, "O")
    for i in config.get("OH_sites", []):
        set_state(i, "OH")
    for i in config.get("vacancies", []):
        set_state(i, "empty")
    for i in config.get("H_sites", []):
        if symbols[i] == "O":
            set_state(i, "OH")
        elif symbols[i] != "H":
            raise ValueError(f"H_sites index {i} is {symbols[i]}; expected an O or H atom")

    # new atoms are free to move if the template has selective dynamics
    props = {"selective_dynamics": [True, True, True]} if "selective_dynamics" in s.site_properties else None
    for el, xyz in add:
        s.append(el, xyz, coords_are_cartesian=True, properties=props)
    s.remove_sites(sorted(remove))
    return s


def unique_configs(structure, configs, symprec=0.1):
    """Remove symmetry-equivalent coverage configurations.

    Args:
        structure: the slab the indices refer to (here: without the removed Ir).
        configs: list of dicts, e.g. {'O_sites': [], 'OH_sites': [36, 37], 'H_sites': [112], 'vacancies': []}
        symprec: symmetry tolerance in Å (try 0.2 if the slab is relaxed).

    Returns:
        unique: list of unique configs (first one of each equivalent set is kept).
        degeneracy: list of how many configs in the input are equivalent to each unique one.
    """
    symbols = np.array([site.specie.symbol for site in structure])
    heavy = Structure.from_sites([site for site in structure if site.specie.symbol != "H"])
    ops = SpacegroupAnalyzer(heavy, symprec=symprec).get_symmetry_operations()

    # Turn each symmetry operation into an index mapping: perm[i] = j
    fcoords = structure.frac_coords
    perms = []
    for op in ops:
        new = op.operate_multi(fcoords)
        perm = np.empty(len(structure), dtype=int)
        for el in np.unique(symbols):
            idx = np.where(symbols == el)[0]
            d = structure.lattice.get_all_distances(new[idx], fcoords[idx])
            perm[idx] = idx[d.argmin(axis=1)]
            if len(set(perm[idx])) != len(idx):  # mapping not one-to-one: skip this operation
                break
        else:
            perms.append(perm)
    print(f"{len(perms)} symmetry operations found")  # 1 means no symmetry, so nothing is merged

    # Canonical key = smallest version of the config over all symmetry operations
    keys = sorted({k for c in configs for k in c})
    unique, degeneracy, seen = [], [], {}
    for c in configs:
        key = min(tuple(tuple(sorted(int(p[i]) for i in c.get(k, []))) for k in keys)
                  for p in perms)
        if key in seen:
            degeneracy[seen[key]] += 1
        else:
            seen[key] = len(unique)
            unique.append(c)
            degeneracy.append(1)
    return unique, degeneracy


def build_structure(template, config, h_pool=(), d_IrO=1.75, d_IrOH=1.95, d_OH=0.98):
    """Build the structure for one coverage dict.

    O_sites / OH_sites / vacancies can be metal (Ir_cus) indices or O indices:
        Ir index : the adsorbate goes ON TOP of that Ir.
                   O_sites   -> terminal O (added at d_IrO above the Ir if the Ir is bare)
                   OH_sites  -> terminal OH (O at d_IrOH above the Ir, H at d_OH above the O)
                   vacancies -> Ir left bare (its terminal O/OH is removed if present; the Ir stays)
        O index  : O_sites -> O kept, its H removed; OH_sites -> H added on that O;
                   vacancies -> that O (and its H) removed.
    H_sites: an O index (e.g. O_bri) is protonated; an H index is kept, and H atoms listed in
    other configs' H_sites (h_pool) but not in this one are removed.
    """
    s = template.copy()
    symbols = [site.specie.symbol for site in s]
    up = np.array([0.0, 0.0, 1.0])

    def bonded_H(o):
        return [int(nb.index) for nb in s.get_neighbors(s[o], 1.2) if nb.specie.symbol == "H"]

    def top_O(m):
        """Terminal O sitting on top of metal m in the template, or None."""
        for nb in s.get_neighbors(s[m], 2.3):
            v = nb.coords - s[m].coords
            if nb.specie.symbol == "O" and v[2] > 0.8 * np.linalg.norm(v):
                return int(nb.index)
        return None

    keep_H = {i for i in config.get("H_sites", []) if symbols[i] == "H"}
    remove = set(h_pool) - keep_H
    add = []  # (species, cartesian coords)

    def set_state(i, state):
        if symbols[i] == "H":
            return
        o = i if symbols[i] == "O" else top_O(i)
        if state == "empty":
            if o is not None:
                remove.add(o)
                remove.update(set(bonded_H(o)) - keep_H)
            return
        if o is None:  # bare Ir: add the adsorbate on top
            if state == "O":
                add.append(("O", s[i].coords + d_IrO * up))
            else:
                o_pos = s[i].coords + d_IrOH * up
                add.append(("O", o_pos))
                add.append(("H", o_pos + d_OH * up))
            return
        hs = set(bonded_H(o))
        if state == "O":
            remove.update(hs - keep_H)
        elif not hs - remove:  # OH wanted and no H left on this O
            add.append(("H", s[o].coords + d_OH * up))

    for i in config.get("O_sites", []):
        set_state(i, "O")
    for i in config.get("OH_sites", []):
        set_state(i, "OH")
    for i in config.get("vacancies", []):
        set_state(i, "empty")
    for i in config.get("H_sites", []):
        if symbols[i] == "O":
            set_state(i, "OH")
        elif symbols[i] != "H":
            raise ValueError(f"H_sites index {i} is {symbols[i]}; expected an O or H atom")

    # new atoms are free to move if the template has selective dynamics
    props = {"selective_dynamics": [True, True, True]} if "selective_dynamics" in s.site_properties else None
    for el, xyz in add:
        s.append(el, xyz, coords_are_cartesian=True, properties=props)
    s.remove_sites(sorted(remove))
    return s


def unique_by_matcher(template, configs, degeneracy=None, ltol=0.2, stol=0.3, angle_tol=5):
    """Build every configuration and group identical structures with StructureMatcher.

    Args:
        template: slab the indices refer to (without the removed Ir).
        configs: list of coverage dicts.
        degeneracy: optional degeneracies of `configs` (e.g. from unique_configs); they are
            summed within each group. If None, every config counts as 1.

    Returns:
        unique: list of unique configs (lowest-index one of each group, input order kept).
        structures: list of the matching pymatgen Structures.
        degeneracy: list of degeneracies.
    """
    if degeneracy is None:
        degeneracy = [1] * len(configs)
    h_pool = {i for c in configs for i in c.get("H_sites", []) if template[i].specie.symbol == "H"}

    structures = []
    for n, c in enumerate(configs):
        st = build_structure(template, c, h_pool)
        st.properties["config_id"] = n
        structures.append(st)

    sm = StructureMatcher(ltol=ltol, stol=stol, angle_tol=angle_tol,
                          primitive_cell=False, scale=False, attempt_supercell=False)
    groups = [sorted(st.properties["config_id"] for st in g) for g in sm.group_structures(structures)]
    groups.sort(key=lambda g: g[0])

    unique = [configs[g[0]] for g in groups]
    unique_structs = [structures[g[0]] for g in groups]
    new_degeneracy = [sum(degeneracy[n] for n in g) for g in groups]
    return unique, unique_structs, new_degeneracy


Ir_cus_sites0 = find_upper_cus_ir(prototype0)
O_bridge_sites0 = oxygen_bridge_index(prototype0, cutoff_nn)


all_Ir0 = get_all_ir(prototype0, cutoff_nn)
Ir_connected_to_bridge0 = get_connected_atoms(prototype0, O_bridge_sites0)
#Ir_cus= = [Ir for Ir in all_Ir if Ir not in Ir_connected_to_bridge]

Ir_cus0 = []
for Ir in all_Ir0:
    if Ir not in Ir_connected_to_bridge0:
        Ir_cus0.append(Ir)
        
len_Ir_cus = len(Ir_cus0)
len_O_bri = len(O_bridge_sites0)

Ir_occupancy_string = generate_occupation_string(len_Ir_cus, memory_Ir)
O_occupancy_string = generate_occupation_string(len_O_bri, memory_O)

all_site_configurations = []

for occupancy1 in Ir_occupancy_string:
    for occupancy2 in O_occupancy_string:
        occupancy_dict = get_adsorpent_positions(occupancy1, Ir_cus0, occupancy2, O_bridge_sites0)
        all_site_configurations.append(occupancy_dict)

unique, structures, degeneracy = unique_by_matcher(prototype0, all_site_configurations)
#unique, degeneracy = unique_configs(prototype0, all_site_configurations)
#all_site_configurations is the dictionary of all O, OH, H and vac sites, yayyy


for idx, struct in enumerate(structures):
    struct.to(fmt="poscar", filename = f"proto0_coverage{idx}.vasp")
    
    






