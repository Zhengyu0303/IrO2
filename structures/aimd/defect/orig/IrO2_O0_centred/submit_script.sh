#!/bin/bash
#SBATCH --job-name=vaspsol_job
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --partition=hbm
module purge
module load ucl-stack/2025-12
source ~/setvars.sh

# 使用 <<-'EOF'，这样你可以在文件里用 Tab 而不报错
cat <<-'EOF' > run_custodian.py
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
EOF

python run_custodian.py
