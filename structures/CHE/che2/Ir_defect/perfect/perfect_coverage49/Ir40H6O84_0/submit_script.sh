#!/bin/bash -l
#SBATCH --job-name=jperfect_coverage49-Ir40H6O84_0
#SBATCH -A acetyl
#SBATCH -p cascadelake
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=96
#SBATCH --time=24:00:00
# bp HPC, cascadelake whole node (2x Xeon Platinum 9242, 96 cores, 4 NUMA x 24).
# Adapted from bear.skylake.vasp.relax.1.pbs (vasp-relax_isif3). Use with cgenerate_submit_all_oswalk.py.
# ==========================================
#          ENVIRONMENT CONFIGURATION
# ==========================================
export PYTHON_EXE="/otherdata/2912je/conda/envs/mat/bin/python"
export ENCUT_STAGE1="400"
export ENCUT_STAGE2="520"
export NCORE_MIN="4"
export NCORE_TARGET="12"
export TARGET_KPT_STAGE1="1 1 1"
export N_MPI=96

# --- CPU Environment: VASP 6.6.0, ifort 2023 + Intel MPI + MKL, AVX-512 ---
module purge
module load icompilers/production-2023 impi/production-2023
export I_MPI_HYDRA_BOOTSTRAP=slurm
export OMP_NUM_THREADS=1
export VASP_EXE_LOW="/otherdata/2912je/apps/vasp/6.6.0/intel2023_impi_omp_avx512/bin/vasp_gam"
export VASP_EXE_HIGH="/otherdata/2912je/apps/vasp/6.6.0/intel2023_impi_omp_avx512/bin/vasp_std"
export VASP_LAUNCHER="mpirun -np $N_MPI "



# ==========================================
#          INITIALIZATION
# ==========================================
echo "========================================" >> status.txt
echo "$(date) INFO: Job initiated." >> status.txt

if [ -s CONTCAR ]; then
    cp CONTCAR POSCAR
    echo "$(date) INFO: Restored POSCAR from existing CONTCAR." >> status.txt
fi

# --- LATTICE_CONSTRAINTS guard ---
# 旧版 pymatgen / custodian 重写 INCAR 时会把 ".TRUE. .TRUE. .FALSE." 改成 "True"。
# 这里记下原始行 (lc.line), 在每次运行 VASP 前后恢复它。
if [ ! -s lc.line ]; then
    grep -iE '^[[:space:]]*LATTICE_CONSTRAINTS[[:space:]]*=' INCAR | head -1 | sed 's/[[:space:]]*$//' > lc.line
    if [ -s lc.line ] && ! grep -qiE '=[[:space:]]*(\.?[TF][A-Za-z]*\.?[[:space:]]+){2}\.?[TF][A-Za-z]*\.?$' lc.line; then
        echo "$(date) ERROR: LATTICE_CONSTRAINTS in INCAR is not 3 logicals: $(cat lc.line). Exit." >> status.txt
        rm -f lc.line
        exit 1
    fi
fi

restore_lc() {
    [ -s lc.line ] || return 0
    if ! grep -qxF "$(cat lc.line)" INCAR; then
        sed -i '/^[[:space:]]*LATTICE_CONSTRAINTS[[:space:]]*=/Id' INCAR
        [ -n "$(tail -c1 INCAR)" ] && echo >> INCAR
        cat lc.line >> INCAR
        echo "$(date) INFO: LATTICE_CONSTRAINTS restored in INCAR." >> status.txt
    fi
}

# --- Parameter Parsing ---
cat << 'EOF' > parse_inputs.py
import os
import sys
from pymatgen.io.vasp import Incar, Kpoints

def analyze():
    if not os.path.exists("INCAR"):
        print("ERROR: INCAR not found.")
        sys.exit(1)
        
    incar = Incar.from_file("INCAR")
    isif = int(incar.get("ISIF", 2))
    encut = str(incar.get("ENCUT", "")).strip()
    
    encut_stage1_target = os.environ.get("ENCUT_STAGE1", "400")
    
    is_gamma_target = False
    if os.path.exists("KPOINTS"):
        try:
            kpts = Kpoints.from_file("KPOINTS")
            if kpts.kpts and len(kpts.kpts[0]) == 3:
                grid = [int(round(float(x))) for x in kpts.kpts[0]]
                target = [int(x) for x in os.environ.get("TARGET_KPT_STAGE1", "1 1 1").split()]
                if grid == target:
                    is_gamma_target = True
        except Exception:
            pass

    has_precise = os.path.exists("KPOINTS.precise")
    try:
        encut_val = float(incar.get("ENCUT", 0))
        encut_target_val = float(encut_stage1_target)
        encut_match = abs(encut_val - encut_target_val) < 1.0
    except (ValueError, TypeError):
        encut_match = False

    do_stage1 = "true" if (encut_match and is_gamma_target and has_precise) else "false"
    
    with open("job_params.txt", "w") as f:
        f.write(f"JOB_ISIF={isif}\n")
        f.write(f"CURRENT_ENCUT={encut}\n")
        f.write(f"IS_GAMMA={str(is_gamma_target).lower()}\n")
        f.write(f"HAS_PRECISE={str(has_precise).lower()}\n")
        f.write(f"DO_STAGE1={do_stage1}\n")
        
    ncore_min = int(os.environ.get("NCORE_MIN", 4))
    ncore_target = int(os.environ.get("NCORE_TARGET", 16))

    if os.path.exists("INCAR"):
        try:
            incar = Incar.from_file("INCAR")
            ncore = incar.get("NCORE")
            if ncore is None or int(ncore) < ncore_min or (int(os.environ.get("N_MPI", 32)) % int(ncore) != 0):
                incar["NCORE"] = ncore_target
                incar.write_file("INCAR")
        except Exception:
            pass

if __name__ == "__main__":
    analyze()
EOF

${PYTHON_EXE} parse_inputs.py
if [ $? -ne 0 ]; then
    echo "$(date) ERROR: Failed to parse input files. Exit." >> status.txt
    exit 1
fi
restore_lc
source job_params.txt

# --- Execution Plan Logging ---
echo "$(date) INFO: --- Job Analysis Report ---" >> status.txt
echo "$(date) INFO: Detected ISIF: $JOB_ISIF" >> status.txt
echo "$(date) INFO: Current ENCUT: $CURRENT_ENCUT (Target Low: $ENCUT_STAGE1, Target High: $ENCUT_STAGE2)" >> status.txt
echo "$(date) INFO: Target KPOINTS matched: $IS_GAMMA" >> status.txt
echo "$(date) INFO: KPOINTS.precise exists: $HAS_PRECISE" >> status.txt
if [ "$DO_STAGE1" == "true" ]; then
    echo "$(date) INFO: Plan: Execute Stage 1 (Low Precision) -> Execute Final Stage (High Precision)." >> status.txt
else
    echo "$(date) INFO: Plan: Skip Stage 1 -> Execute Final Stage (High Precision) directly." >> status.txt
fi
echo "$(date) INFO: ---------------------------" >> status.txt

# ==========================================
#          FUNCTIONS
# ==========================================
check_poscar_exists() {
    if [ ! -s POSCAR ]; then
        echo "$(date) ERROR: POSCAR is empty or does not exist. Terminating." >> status.txt
        exit 1
    fi
}

run_custodian_calc() {
    local exe=$1
    export VASP_CURRENT_EXE=$exe
    echo "$(date) INFO: Running Custodian with $exe ..." >> status.txt

    cat << 'EOF' > run_custodian.py
import os
import sys
import shlex
from custodian.custodian import Custodian
from custodian.vasp.handlers import VaspErrorHandler, UnconvergedErrorHandler
from custodian.vasp.jobs import VaspJob

vasp_launcher = shlex.split(os.environ.get("VASP_LAUNCHER", ""))
vasp_exe = os.environ.get("VASP_CURRENT_EXE", "vasp_std")
vasp_cmd = vasp_launcher + [vasp_exe] if vasp_launcher else [vasp_exe]

import re

def restore_lattice_constraints(directory="."):
    lc_file = os.path.join(directory, "lc.line")
    incar = os.path.join(directory, "INCAR")
    if not (os.path.isfile(lc_file) and os.path.isfile(incar)):
        return
    with open(lc_file) as fh:
        want = fh.read().strip()
    if not want:
        return
    with open(incar) as fh:
        lines = fh.read().splitlines()
    out, seen, changed = [], False, False
    for ln in lines:
        if re.match(r"\s*LATTICE_CONSTRAINTS\s*=", ln, re.I):
            seen = True
            if ln.strip() != want:
                ln, changed = want, True
        out.append(ln)
    if not seen:
        out.append(want)
        changed = True
    if changed:
        with open(incar, "w") as fh:
            fh.write("\n".join(out) + "\n")
        with open(os.path.join(directory, "status.txt"), "a") as fh:
            fh.write("INFO: LATTICE_CONSTRAINTS restored in INCAR (before VASP launch).\n")

class LCVaspJob(VaspJob):
    def run(self, *args, **kwargs):
        d = kwargs.get("directory", args[0] if args else ".")
        restore_lattice_constraints(d)
        return super().run(*args, **kwargs)

jobs = [LCVaspJob(vasp_cmd)]
handlers = [VaspErrorHandler(), UnconvergedErrorHandler()]
c = Custodian(handlers, jobs, max_errors=20)

import traceback
try:
    c.run()
    restore_lattice_constraints()
except Exception as e:
    traceback.print_exc()
    print(e)
    sys.exit(1)
EOF

    restore_lc
    ${PYTHON_EXE} run_custodian.py > custodian.log 2>&1
    local custodian_status=$?
    restore_lc
    
    if [ -f custodian.log ]; then
        echo "=== Custodian Log Appended at $(date) ===" >> vasp.out.total
        cat custodian.log >> vasp.out.total
    fi
    
    if [ -f vasp.out ]; then
        echo "=== VASP Out Appended at $(date) ===" >> vasp.out.total
        cat vasp.out >> vasp.out.total
        mv vasp.out vasp.out.last
    fi

    if [ $custodian_status -ne 0 ]; then
        echo "$(date) ERROR: Custodian run failed. Halting script." >> status.txt
        exit 1
    fi
}

check_and_fix_symmetry() {
    if grep -q "Inconsistent Bravais lattice" OUTCAR 2>/dev/null; then
        if ! grep -q "SYMPREC" INCAR; then
            echo "$(date) INFO: Symmetry error detected. Adding SYMPREC=1e-08 to INCAR." >> status.txt
            echo "SYMPREC = 1e-08" >> INCAR
        fi
        return 0
    fi
    return 1
}

# --- 严格检查运算收敛性 (vasprun.xml) ---
check_vasprun_convergence() {
    local stage_name=$1
    echo "$(date) INFO: Validating convergence for ${stage_name} using vasprun.xml..." >> status.txt
    
    cat << 'EOF_CONV' > check_vasp_conv.py
import sys
import warnings
warnings.filterwarnings("ignore")
from pymatgen.io.vasp.outputs import Vasprun

try:
    v = Vasprun("vasprun.xml", parse_potcar_file=False, exception_on_bad_xml=True)
except Exception as e:
    print(f"XML Parsing Error: {e}")
    sys.exit(1)

incar = v.incar
nsw = incar.get("NSW", 0)
ibrion = incar.get("IBRION", 0)

# 判断是否为不改变原子位置的静态计算
is_static = (nsw <= 1) or (ibrion == -1)

if is_static:
    if v.converged_electronic:
        sys.exit(0)
    else:
        sys.exit(1)
else:
    # 结构弛豫，要求电子步和离子步双重收敛
    if v.converged_electronic and v.converged_ionic:
        sys.exit(0)
    else:
        sys.exit(1)
EOF_CONV

    ${PYTHON_EXE} check_vasp_conv.py
    local conv_status=$?
    
    if [ $conv_status -eq 0 ]; then
        echo "$(date) INFO: ${stage_name} convergence validated." >> status.txt
        return 0
    else
        echo "$(date) ERROR: ${stage_name} failed convergence criteria. Aborting job for recalculation." >> status.txt
        exit 1
    fi
}

get_ion_steps() {
    if [ -f OSZICAR ]; then
        local steps=$(grep -v '^$' OSZICAR | tail -n 1 | awk '{print $1}')
        echo "$steps" | grep -o '[0-9]\+'
    else
        echo "999"
    fi
}

backup_xdatcar() {
    local prefix=$1
    if [ -f XDATCAR ]; then
        local count=$(ls XDATCAR.${prefix}.* 2>/dev/null | grep -E "XDATCAR\.${prefix}\.[0-9]+$" | sed "s/XDATCAR.${prefix}.//" | sort -n | tail -1)
        [ -z "$count" ] && count=0
        local next_count=$((count + 1))
        cp XDATCAR "XDATCAR.${prefix}.${next_count}"
    fi
}

run_stage() {
    local exe=$1
    local prefix=$2
    local stage_name=$3

    echo "$(date) INFO: Executing ${stage_name}." >> status.txt

    if [ "$JOB_ISIF" == "3" ]; then
        while true; do
            run_custodian_calc "$exe"
            check_and_fix_symmetry
            backup_xdatcar "$prefix"
            
            # 使用vasprun.xml进行严格收敛检查
            check_vasprun_convergence "${stage_name} iteration"
            
            local rel=$(get_ion_steps)
            echo "$(date) INFO: ${stage_name} iteration completed. Ion steps: $rel" >> status.txt
            check_poscar_exists

            if [ "$rel" -le 10 ]; then
                echo "$(date) INFO: ${stage_name} volume convergence achieved (steps <= 10)." >> status.txt
                break
            else
                cp CONTCAR POSCAR
                rm -f WAVECAR CHG*
                echo "$(date) INFO: Restarting ${stage_name} for Pulay Stress elimination." >> status.txt
            fi
        done
    else
        run_custodian_calc "$exe"
        check_and_fix_symmetry
        backup_xdatcar "$prefix"
        
        # 使用vasprun.xml进行严格收敛检查
        check_vasprun_convergence "${stage_name}"
        
        local rel=$(get_ion_steps)
        echo "$(date) INFO: ${stage_name} relaxation complete. Ion steps: $rel" >> status.txt
    fi
}

# ==========================================
#          MAIN WORKFLOW
# ==========================================
check_poscar_exists

if [ -f vasprun.xml.relaxed.gz ] || [ -f vasprun.xml.relaxed ]; then
    echo "$(date) INFO: Job already fully relaxed. Exit." >> status.txt
    exit 0
fi

[ ! -s POSCAR.orig ] && cp POSCAR POSCAR.orig

if [ "$DO_STAGE1" == "true" ]; then
    run_stage "$VASP_EXE_LOW" "low" "Stage 1"
    
    echo "$(date) INFO: Stage 1 completed. Upgrading INCAR ENCUT to ${ENCUT_STAGE2}." >> status.txt
    sed -i "s/ENCUT = .*/ENCUT = ${ENCUT_STAGE2}/" INCAR
    cp KPOINTS.precise KPOINTS
    cp CONTCAR POSCAR
    rm -f WAVECAR CHG*
fi

run_stage "$VASP_EXE_HIGH" "high" "Final Stage"

restore_lc

# --- Post-processing ---
for f in CONTCAR DOSCAR EIGENVAL IBZKPT INCAR KPOINTS OSZICAR OUTCAR POSCAR PROCAR vasprun.xml vasp.out.total run_custodian.py parse_inputs.py check_vasp_conv.py job_params.txt custodian.log vasp.out.last; do
    [ -f $f ] && mv $f ${f}.relaxed
done

gzip -f *.relaxed
echo "$(date) INFO: Job post-processing complete." >> status.txt