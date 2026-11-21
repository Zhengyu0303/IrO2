from pymatgen.core.structure import Structure
from pymatgen.alchemy.transmuters import PoscarTransmuter,PoscarTransmuter
import os
import numpy as np
from pymatgen.io.vasp.sets import MVLScanRelaxSet,MVLGBSet, MPRelaxSet
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.alchemy.transmuters import PoscarTransmuter
from pymatgen.core.structure import Structure
 

incar_slab = {
    "ADDGRID": False,
    "ENCUT": 520,
    "EDIFF": 1e-5,
    "EDIFFG": -0.01,
    #"GGA": "RP",
    "NSW": 250,
    "NCORE": 10,
    "LPLANE": "True",
    "NSIM": 4, # NSIM=8 cause memory overflow
    "NELMIN": 6,
    "ISPIN": 2,
    "ICHARG": 2,
    "LASPH": False,
    "IBRION": 2,
    "ISMEAR": 0,
    "LORBIT": 11,
    "ISYM": 0,
    "ISPIN": 2,
    "ISMEAR": 0,
    "SIGMA": 0.6, #instead of 0.2, changed because this is the default for Vaspsol linear model
    "ALGO": "All",
    "PREC": "Normal",
    "ISIF": 2,
    "LCHARG": False,
    "LVHAR": True,
    "PREC": "Normal",
    "LSOL": True,
    "LDIPOL": True,
    "IDIPOL": 3,
    "TAU": 0.0,
    "ISOL": 1,
}
 
for poscar in os.listdir("."):
    try:
  
  
        t=PoscarTransmuter.from_filenames([poscar])
        t.write_vasp_input(
    vasp_input_set=MPRelaxSet,

    user_incar_settings=incar_slab,
    output_dir=poscar.split(".")[0],
    create_directory=True,
    subfolder=None,
    include_cif=True,
    force_gamma=True
)
    except Exception as e:
        print(f"fail reading on {poscar} due to {e}") 
