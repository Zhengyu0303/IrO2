#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:12:10 2026

@author: zhengyuliu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 12:10:22 2025

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
    min_slab_size=30,  # Thickness of the slab in Å
    min_vacuum_size=30,  # Thickness of the vacuum layer in Å
    lll_reduce=True,
    reorient_lattice=True,
    center_slab=True
    
)

slabs = slabgen.get_slabs()
slab = slabs[1]*[2,2,1]

supercell = slab.copy()





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

#supercell.remove_sites([remove1])

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

sites = asf.find_adsorption_sites(distance=2.3)

adsorbed_structures = asf.generate_adsorption_structures(
    water, 
    repeat=[1, 1, 1],     # Do not make a larger supercell
    find_args={"distance": 2.3} 
)


output_dir = "water_pristine"
os.makedirs(output_dir, exist_ok=True)

for index, struct in enumerate(adsorbed_structures):
    filename = f"{output_dir}/POSCAR_water_{index+1}"
    struct.to(fmt="poscar", filename=filename)
    print(f"Saved: {filename}")

#poscar.write_file(f"test.vasp")





