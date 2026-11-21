from pymatgen.core import Structure

structure = Structure.from_file("O_vacuum_centred.cif")
structure.to(filename="O_vacuum_centred.vasp", fmt="poscar")