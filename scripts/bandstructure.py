from pymatgen.io.vasp import Vasprun
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import Spin
import numpy as np
from scipy.signal import find_peaks

# Load VASP DOS data from vasprun.xml
vasprun = Vasprun("vasprun.xml", parse_dos=True)
dos = vasprun.complete_dos  # Get total DOS

# Extract energy and DOS values
energies = dos.energies #- dos.efermi  # Shift energies relative to Fermi level
total_dos = dos.densities[Spin.up]  # Total DOS (Spin-up)

##Now we have to recognise the peaks and its corresponding IBAND
peaks, _ = find_peaks(total_dos, height=0.1, distance=2, prominence=0.05)

# Plot Total DOS
plt.figure(figsize=(8, 5))
plt.plot(energies, total_dos, label="Total DOS", color="blue")
plt.xlim(-10,10)
plt.ylim(-1,120)

plt.xlabel("Energy (eV)")
plt.ylabel("DOS (States/eV)")


plt.scatter(energies[peaks], total_dos[peaks], color='red', label="Peaks", zorder=3)

plt.axvline(dos.efermi, linestyle="--", color="black", label="Fermi Level")
plt.xlim(-10,5)
plt.ylim(-1,250)
plt.title("Density of States with Peaks")

plt.legend()
plt.savefig("DOS.pdf", dpi = 800)

peak_energies = []

for energy in energies[peaks]:
    if energy >= dos.efermi-2.1 and energy <= dos.efermi + 1.5:
        peak_energies.append(energy)
print(peak_energies)
band_structure = vasprun.get_band_structure()

matching_bands = []

tolerance = 0.1  # Energy tolerance for matching peaks to bands

for peak_energy in peak_energies:
    for iband, band_energies in enumerate(band_structure.bands[Spin.up]):
        if np.any((band_energies > peak_energy - tolerance) &
                  (band_energies < peak_energy + tolerance)):
            matching_bands.append((peak_energy, iband))

# Print results
for peak, band in matching_bands:
    print(f"Peak at {peak:.2f} eV corresponds to IBAND {band}")

