import matplotlib.pyplot as plt
import numpy as np
from pymatgen.core.structure import Structure
from pymatgen.analysis.surface_analysis import WorkFunctionAnalyzer

wf = WorkFunctionAnalyzer.from_files("./CONTCAR", "./LOCPOT", "./OUTCAR", shift = 0.5)
wf.get_locpot_along_slab_plot()
plt.savefig("./aaa.pdf")