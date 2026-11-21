import os
from custodian.custodian import Custodian
from custodian.vasp.handlers import VaspErrorHandler, UnconvergedErrorHandler
from custodian.vasp.jobs import VaspJob
from pymatgen.io.vasp import Incar

if os.path.exists("INCAR"):
    try:
        incar = Incar.from_file("INCAR")
        ncore = incar.get("NCORE")
        
        # 统一使用空格缩进
        if ncore is None or int(ncore) < 4 or (32 % int(ncore) != 0):
            incar["NCORE"] = 16
            incar.write_file("INCAR")
            print(f"[*] Pre-check: NCORE updated to 16.")
        else:
            print(f"[*] Pre-check: NCORE is valid: {ncore}")
    except Exception as e:
        print(f"[!] Warning: Failed to update INCAR: {e}")

mpi_tasks = os.environ.get("SLURM_NTASKS", "1")
vasp_cmd = ["mpirun", "-np", mpi_tasks, "/lustre/scratch/mmm1514//app/vaspsol_632/bin/vasp_std"]

print(f"[*] Custodian is running with {mpi_tasks} tasks.")
jobs = [VaspJob(vasp_cmd)]
handlers = [VaspErrorHandler(), UnconvergedErrorHandler()]
c = Custodian(handlers, jobs, max_errors=20)
c.run()
