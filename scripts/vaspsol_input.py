from pymatgen.core.structure import Structure
from pymatgen.alchemy.transmuters import PoscarTransmuter
import os
import numpy as np
from pymatgen.io.vasp.sets import MVLScanRelaxSet, MVLGBSet, MPRelaxSet
from pymatgen.io.vasp.inputs import Kpoints

incar_slab = {
    "ADDGRID": False,
    "ENCUT": 520,
    "EDIFF": 1e-4, #Loosened for convergence issues with IrO2 slab
    "EDIFFG": -0.01,
    "NSW": 150,
    "NCORE": 1,
    "LPLANE": "True",
    "NSIM": 4, # NSIM=8 cause memory overflow
    "NELMIN": 6,
    "ISPIN": 1,
    "ICHARG": 2,
    "LASPH": False,
    "LORBIT": 11,
    "ISYM": 0,
    "ISMEAR": 0,
    "SIGMA": 0.2, #Changed for convergence issues with IrO2 slab
    "ALGO": "All",
    "PREC": "Normal",
    "ISIF": 2,
    "LCHARG": False,
    "LVHAR": True,
    "PREC": "Normal",

    "LSOL": True,
    "ISOL": 1,

#Solvent specification

    "EB_K": 78.4, #This is default value for water at 298K, but can be changed if needed
    "LNLDIEL": False, #Use linear one for testing, but can be changed to .TRUE. for more accurate results
    "EPSILON_INF": 1.78, #Bulk optical dielectric constant of the solvent
    "N_MOL": 0.0335, #Density of solvent molecules in the bulk (Å-3)
    "P_MOL": 0.50, #Dipole moment of a solvent molecule (e-Å)
    "R_SOLV": 1.40, # (default)
    #Solvent radius (Å) for constructing the solvent cavity
    "R_DIEL": 1.00, # (default)
    #Dielectric radius (Å) for constructing the dielectric cavity
    "R_B": 1.00, # (default)
    #Smearing length (Å) for the bound charge, used to reduce FFT truncation error


#Solvent specification
    "LNLION": False, #Use linear one for testing, but can be changed to .TRUE. for more accurate results
    "C_MOLAR": 0.1,

    "ZION": 1.0, # (default) Electrolyte valency
    #"D_ION": 25/6*1.40, # (default) Packing diameter of the ions (Å), defaults to the close-packed diameter corresponding to R_ION
    "R_ION": 1.40, # (default) Ionic radius (Å) for constructing the ionic cavity


    # #"R_ION": 4.0,
    # "ZION": 1.0,
    # "EB_K": 78.4,
    # "SOLTEMP": 298

}

NET_CHARGE = 0  # +2 charge for IrO2: #Ir*9 + #O*6 - 2

for poscar in os.listdir("."):
    try:
        # Read structure and compute neutral NELECT from POTCAR ZVAL
        structure = Structure.from_file(poscar)
        nelect_neutral = MPRelaxSet(structure).nelect

        incar_slab_charged = {
            **incar_slab,
            "NELECT": nelect_neutral - NET_CHARGE,  # remove electrons for +ve charge
        }

        t = PoscarTransmuter.from_filenames([poscar])
        t.write_vasp_input(
            vasp_input_set=MPRelaxSet,
            user_incar_settings=incar_slab_charged,
            output_dir=poscar.split(".")[0],
            create_directory=True,
            subfolder=None,
            include_cif=True,
            force_gamma=True
        )
        print(f"Done: {poscar} | NELECT_neutral={nelect_neutral} | NELECT={nelect_neutral - NET_CHARGE}")

    except Exception as e:
        print(f"fail reading on {poscar} due to {e}")