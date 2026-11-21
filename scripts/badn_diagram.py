from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

# Load the band structure from VASP output
vasprun = Vasprun("vasprun.xml", parse_projected_eigen=True)
band_structure = vasprun.get_band_structure()

# Use BSPlotter to plot the band structure
plotter = BSPlotter(band_structure)
plotter.show()

