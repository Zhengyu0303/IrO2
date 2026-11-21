import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

# Load the vasprun.xml file
vasprun = Vasprun("vasprun.xml")

# Get the band structure and Fermi energy
band_structure = vasprun.get_band_structure()
fermi_energy = vasprun.efermi  # Fermi level in eV

# Extract CBM and VBM
cbm = band_structure.get_cbm()["energy"]
vbm = band_structure.get_vbm()["energy"]

# Print the results
print(f"Fermi Energy (E_f): {fermi_energy:.3f} eV")
print(f"Valence Band Maximum (VBM): {vbm:.3f} eV")
print(f"Conduction Band Minimum (CBM): {cbm:.3f} eV")

