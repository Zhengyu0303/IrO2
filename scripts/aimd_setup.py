"""
generate_aimd_inputs.py
=======================
Generates VASP INCAR, POTCAR, and KPOINTS for an AIMD simulation
of an IrO2 slab with water, using pymatgen.

Supports two modes (set FUNCTIONAL below):
  - "PBE-D3"    : Fast, good for initial testing / long runs
  - "r2SCAN-D3" : More accurate, recommended for production runs

Usage:
    python generate_aimd_inputs.py

Requirements:
    pip install pymatgen
    PMG_VASP_PSP_DIR must be set in ~/.config/pymatgen/config.yaml
    (or set VASP_PSP_DIR env variable)
"""

import os
from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet, MPScanRelaxSet
from pymatgen.io.vasp.inputs import Incar, Kpoints, Potcar

# ─────────────────────────────────────────────
# USER SETTINGS — edit these
# ─────────────────────────────────────────────

CIF_FILE    = "water_packed.vasp"       # Path to your IrO2+water CIF
OUTPUT_DIR  = "water_bulk/"         # Where to write input files
FUNCTIONAL  = "PBE-D3"              # "PBE-D3" or "r2SCAN-D3"

# MD parameters
NSW    = 2500    # Number of MD steps (5000 steps × 0.5 fs = 2.5 ps — good for testing)
POTIM  = 0.5     # Timestep in fs (0.5 fs recommended when H is present)
TEBEG  = 300     # Starting temperature in K (slightly above 300 to aid equilibration)
TEEND  = 300     # Target temperature in K
SMASS  = 0       # Nosé–Hoover NVT thermostat

# ─────────────────────────────────────────────
# LOAD STRUCTURE
# ─────────────────────────────────────────────

print(f"Reading structure from: {CIF_FILE}")
structure = Structure.from_file(CIF_FILE)
print(f"  Elements : {structure.composition.formula}")
print(f"  Num sites: {len(structure)}")
print(f"  Cell     : {structure.lattice.abc}\n")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# SHARED MD INCAR OVERRIDES
# These apply regardless of functional choice
# ─────────────────────────────────────────────

md_settings = {
    # --- MD control ---
    "IBRION" : 0,       # Activate molecular dynamics
    "NSW"    : NSW,
    "POTIM"  : POTIM,
    "TEBEG"  : TEBEG,
    "TEEND"  : TEEND,
    "SMASS"  : SMASS,   # 0 = Nosé–Hoover NVT
    "MDALGO" : 2,

    # --- SCF convergence (looser is fine for MD) ---
    "EDIFF"  : 1e-5,
    "NELM"   : 100,
    "NELMIN" : 4,

    # --- Performance (critical for large slab+water cells) ---
    "LREAL"  : "Auto",  # Real-space projection; essential for large cells
    "ALGO"   : "Fast",  # RMM-DIIS; stable for most AIMD
    "PREC"   : "Normal",

    # --- Output (minimise I/O — these files get huge) ---
    "LWAVE"  : True,   # Don't write WAVECAR every step
    "LCHARG" : True,   # Don't write CHGCAR every step
    "NWRITE" : 1,       # Minimal OUTCAR verbosity
    "NBLOCK" : 1,       # Write XDATCAR every step
    "KBLOCK" : 100,     # Write averages every 100 steps

    # --- Dispersion (non-negotiable for water/oxide interface) ---
    "IVDW"   : 12,      # DFT-D3 (Becke-Johnson damping)

    # --- IrO2-specific: no Hubbard U needed (metallic rutile phase) ---
    # "LDAU" is intentionally omitted
}

# ─────────────────────────────────────────────
# FUNCTIONAL-SPECIFIC SETTINGS
# ─────────────────────────────────────────────

if FUNCTIONAL == "PBE-D3":
    print("Setting up PBE-D3 inputs (fast testing mode)")

    pbe_extra = {
        "GGA"   : "PE",   # PBE functional
        "ISPIN" : 1,      # IrO2 rutile is non-magnetic
        "ENCUT" : 520,    # Sufficient for PBE; raise to 520 for production
    }
    all_settings = {**md_settings, **pbe_extra}

    # Use MPRelaxSet as base (sets sensible PAW potentials etc.)
    vis = MPRelaxSet(
        structure,
        user_incar_settings=all_settings,
        user_kpoints_settings={"reciprocal_density": 1},  # Will be overridden below
        force_gamma=True,
    )

elif FUNCTIONAL == "r2SCAN-D3":
    print("Setting up r2SCAN-D3 inputs (accurate production mode)")

    scan_extra = {
        "METAGGA" : "R2SCAN",  # Meta-GGA functional
        "LASPH"   : True,      # Required for meta-GGA (non-spherical corrections)
        "ISPIN"   : 1,
        "ENCUT"   : 520,       # r2SCAN needs a higher cutoff
        # GGA tag must NOT be present when using METAGGA
    }
    all_settings = {**md_settings, **scan_extra}

    # MPScanRelaxSet is the correct base for r2SCAN (uses appropriate POTCARs)
    vis = MPScanRelaxSet(
        structure,
        user_incar_settings=all_settings,
        user_kpoints_settings={"reciprocal_density": 1},
        force_gamma=True,
    )

else:
    raise ValueError(f"Unknown functional: {FUNCTIONAL}. Choose 'PBE-D3' or 'r2SCAN-D3'.")

# ─────────────────────────────────────────────
# KPOINTS — Gamma-point only for large slab
# ─────────────────────────────────────────────
# For AIMD with a large slab+water supercell, Gamma-point is standard.
# The cell is large enough that k-point sampling beyond Gamma gives
# negligible improvement at significant cost.

kpoints = Kpoints.gamma_automatic(kpts=(1, 1, 1), shift=(0, 0, 0))

# ─────────────────────────────────────────────
# WRITE INPUT FILES
# ─────────────────────────────────────────────

# Write INCAR
incar = vis.incar
# Clean up any tags that shouldn't be present for AIMD
tags_to_remove = ["IOPT", "EDIFFG", "MAGMOM"]#, "NSW"]  # NSW is set via md_settings already
for tag in tags_to_remove:
    incar.pop(tag, None)

incar_path = os.path.join(OUTPUT_DIR, "INCAR")
incar.write_file(incar_path)
print(f"\nWrote INCAR  → {incar_path}")

# Write KPOINTS
kpoints_path = os.path.join(OUTPUT_DIR, "KPOINTS")
kpoints.write_file(kpoints_path)
print(f"Wrote KPOINTS → {kpoints_path}")

# Write POSCAR
poscar = vis.poscar
poscar_path = os.path.join(OUTPUT_DIR, "POSCAR")
poscar.write_file(poscar_path)
print(f"Wrote POSCAR  → {poscar_path}")

# Write POTCAR
# Requires VASP pseudopotential library configured in pymatgen
# Set via: pmg config --add PMG_VASP_PSP_DIR /path/to/your/pseudopotentials
try:
    potcar = vis.potcar
    potcar_path = os.path.join(OUTPUT_DIR, "POTCAR")
    potcar.write_file(potcar_path)
    print(f"Wrote POTCAR  → {potcar_path}")
    print(f"  POTCAR symbols: {[p.symbol for p in potcar]}")
except Exception as e:
    print(f"\n[WARNING] Could not write POTCAR: {e}")
    print("  Set up your VASP PSP directory with:")
    print("    pmg config --add PMG_VASP_PSP_DIR /path/to/vasp/pps")
    print("  Then rerun, or manually concatenate POTCARs for your elements.")

# ─────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────

print(f"""
╔══════════════════════════════════════════╗
  AIMD Input Generation Complete
  Functional : {FUNCTIONAL}
  Timestep   : {POTIM} fs
  Steps      : {NSW}  ({NSW * POTIM / 1000:.1f} ps)
  Temp       : {TEBEG}→{TEEND} K (NVT)
  Thermostat : Nosé–Hoover (SMASS=0)
  Dispersion : DFT-D3 (IVDW=11)
  Output dir : {OUTPUT_DIR}/
╚══════════════════════════════════════════╝

Next steps:
  1. Check POSCAR element order matches your POTCAR
  2. Pre-relax your structure first (IBRION=2, NSW=200)
  3. Run a short 0.5 ps equilibration before production
  4. Monitor OSZICAR to check SCF converges at each step
""")