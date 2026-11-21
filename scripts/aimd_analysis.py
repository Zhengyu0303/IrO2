"""
Check AIMD equilibration by tracking the running (cumulative) average
of total energy and temperature vs. simulation time.

Assumption: "the average" = running average of energy/temperature used to
spot where the trajectory stops drifting and settles into a plateau
(i.e. equilibration), as discussed. If you actually meant something else
(e.g. average structure, RDF, MSD), let me know and I'll adjust.

Requires: pymatgen, numpy, matplotlib
    pip install pymatgen --break-system-packages   (if not already installed)

Usage:
    python aimd_equilibration.py
(edit the CONFIG block below to point at your files)
"""

import re
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun

# ----------------------------- CONFIG -----------------------------------
VASPRUN_PATH = "vasprun.xml"
OSZICAR_PATH = "OSZICAR"
POTIM_FS = 1.0          # your MD time step in fs, for the x-axis in time units
EQUIL_CUTOFF_STEP = 500  # discard steps before this index when computing the
                          # final "equilibrated" average -- set based on where
                          # the running average visually flattens out
OUT_PLOT = "aimd_equilibration.png"
OUT_CSV = "aimd_equilibration.csv"
# --------------------------------------------------------------------------


def get_energy_series(vasprun_path):
    """Total (free) energy per ionic step, from vasprun.xml via pymatgen."""
    vr = Vasprun(
        vasprun_path,
        parse_dos=False,
        parse_eigen=False,
        parse_projected_eigen=False,
    )
    energies = [step["e_fr_energy"] for step in vr.ionic_steps]
    return np.array(energies)


def get_temperature_series(oszicar_path):
    """
    Instantaneous temperature per ionic step, parsed from OSZICAR.
    VASP AIMD OSZICAR lines look like:
        1 T=  300.12 E= -1234.5678 F= -1234.5678 E0= -1234.5671 EK= 0.0321 SP= 0.00 SK= 0.00
    so we just grab the number after "T=".
    """
    pattern = re.compile(r"T=\s*([\-\d.]+)")
    temps = []
    with open(oszicar_path) as f:
        for line in f:
            m = pattern.search(line)
            if m:
                temps.append(float(m.group(1)))
    return np.array(temps)


def running_average(values):
    return np.cumsum(values) / np.arange(1, len(values) + 1)


def main():
    energies = get_energy_series(VASPRUN_PATH)
    temps = get_temperature_series(OSZICAR_PATH)

    n = min(len(energies), len(temps))
    if len(energies) != len(temps):
        print(
            f"Warning: {len(energies)} energy steps vs {len(temps)} temperature "
            f"steps parsed -- truncating both to {n}. Check for a restarted run "
            f"or mismatched files."
        )
    energies, temps = energies[:n], temps[:n]

    steps = np.arange(n)
    time_fs = steps * POTIM_FS

    run_avg_E = running_average(energies)
    run_avg_T = running_average(temps)

    # --- save raw + running-average data ---
    header = "step,time_fs,energy_eV,temperature_K,running_avg_energy_eV,running_avg_temperature_K"
    data = np.column_stack([steps, time_fs, energies, temps, run_avg_E, run_avg_T])
    np.savetxt(OUT_CSV, data, delimiter=",", header=header, comments="", fmt="%.6f")
    print(f"Wrote per-step data + running averages to {OUT_CSV}")

    # --- equilibrated averages (past the cutoff) ---
    if EQUIL_CUTOFF_STEP >= n:
        print(
            f"EQUIL_CUTOFF_STEP ({EQUIL_CUTOFF_STEP}) >= number of steps ({n}); "
            f"lower it or extend the trajectory."
        )
    else:
        eq_E = energies[EQUIL_CUTOFF_STEP:]
        eq_T = temps[EQUIL_CUTOFF_STEP:]
        print(
            f"Equilibrated average (steps {EQUIL_CUTOFF_STEP}-{n}, "
            f"{len(eq_E)} steps):"
        )
        print(f"  Energy      = {eq_E.mean():.6f} +/- {eq_E.std():.6f} eV")
        print(f"  Temperature = {eq_T.mean():.2f} +/- {eq_T.std():.2f} K")

    # --- plot raw values + running average, energy and temperature ---
    fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

    axes[0].plot(time_fs, energies, lw=0.5, alpha=0.4, label="instantaneous")
    axes[0].plot(time_fs, run_avg_E, lw=1.8, label="running average")
    axes[0].axvline(EQUIL_CUTOFF_STEP * POTIM_FS, color="k", ls="--", lw=1,
                     label="equilibration cutoff")
    axes[0].set_ylabel("Total energy (eV)")
    axes[0].legend()

    axes[1].plot(time_fs, temps, lw=0.5, alpha=0.4, label="instantaneous")
    axes[1].plot(time_fs, run_avg_T, lw=1.8, label="running average")
    axes[1].axvline(EQUIL_CUTOFF_STEP * POTIM_FS, color="k", ls="--", lw=1)
    axes[1].set_ylabel("Temperature (K)")
    axes[1].set_xlabel("Time (fs)")
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(OUT_PLOT, dpi=150)
    print(f"Wrote plot to {OUT_PLOT}")


if __name__ == "__main__":
    main()