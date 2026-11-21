from pymatgen.analysis.surface_analysis import WorkFunctionAnalyzer
from pymatgen.io.vasp import Vasprun

locpot_folder = "."
a = WorkFunctionAnalyzer.from_files(locpot_folder+"/CONTCAR",locpot_folder+"/LOCPOT",locpot_folder+"/OUTCAR",shift=0,blength=2.3)

# print(a.is_converged(), "\n")
# print("Vacuum level = ", a.vacuum_locpot,"\n")

vasprun = Vasprun("vasprun.xml", parse_dos=True)
dos = vasprun.complete_dos


vasprun = Vasprun("vasprun.xml", parse_projected_eigen=True)
band_structure = vasprun.get_band_structure()

print(a.is_converged(), "\n")
print("Vacuum level = ", a.vacuum_locpot,"\n")

print("Fermi level = ", band_structure.efermi,"\n")
print("Fermi level = ",dos.efermi, "\n")

print("VBM = ", band_structure.get_vbm()['energy'], "\n", "CBM = ", band_structure.get_cbm()['energy'])