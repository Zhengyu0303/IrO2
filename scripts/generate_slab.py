import os
from pymatgen.core import Structure
import numpy as np

# Load the bulk structure from a POSCAR file
bulk_structure = Structure.from_file("POSCAR.vasp")

from pymatgen.core.surface import SlabGenerator

# Define the Miller index for the surface you want
miller_index = (1, 0, 0)  # Example: (1, 1, 1) plane

# Set up the slab generator
slabgen = SlabGenerator(
    initial_structure=bulk_structure,
    miller_index=miller_index,
    min_slab_size=5,  # Thickness of the slab in Å
    min_vacuum_size=35,  # Thickness of the vacuum layer in Å
)

# Generate the slabs
slabs = slabgen.get_slabs()
slabs[0].to(fmt="poscar", filename="POSCAR_slab.vasp")

for i in np.linspace(5, 45, 1):
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
        slabs[0].to(fmt="poscar", filename=f"mgo{i:.0f}_{j:.0f}_POSCAR_slab.vasp")