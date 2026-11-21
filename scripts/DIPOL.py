from pymatgen.core import Structure
import numpy as np

def calculate_periodic_dipol(poscar_path="POSCAR"):
    structure = Structure.from_file(poscar_path)
    
    # Extract fractional coordinates along z-axis and masses
    z_fracs = structure.frac_coords[:, 2]
    masses = np.array([site.species.weight for site in structure])
    
    # Convert fractional coordinates to phase angles (0 to 2*pi)
    angles = 2 * np.pi * z_fracs
    
    # ---------------------------------------------------------
    # 1. Periodic Geometric Center (Unweighted)
    # ---------------------------------------------------------
    cos_mean_geom = np.mean(np.cos(angles))
    sin_mean_geom = np.mean(np.sin(angles))
    
    z_center_geom = np.arctan2(sin_mean_geom, cos_mean_geom) / (2 * np.pi)
    z_center_geom = z_center_geom % 1.0  # Ensure it stays in [0, 1)
    
    # ---------------------------------------------------------
    # 2. Periodic Center of Mass (Mass-weighted)
    # ---------------------------------------------------------
    total_mass = np.sum(masses)
    cos_mean_com = np.sum(masses * np.cos(angles)) / total_mass
    sin_mean_com = np.sum(masses * np.sin(angles)) / total_mass
    
    z_center_com = np.arctan2(sin_mean_com, cos_mean_com) / (2 * np.pi)
    z_center_com = z_center_com % 1.0    # Ensure it stays in [0, 1)
    
    # ---------------------------------------------------------
    # Output formatted for INCAR
    # ---------------------------------------------------------
    print("--- INCAR Tags ---")
    print(f"IDIPOL = 3")
    print(f"LDIPOL = .TRUE.")
    print(f"# Periodic Geometric Center:")
    print(f"DIPOL  = 0.5 0.5 {z_center_geom:.4f}")
    print(f"# Periodic Center of Mass:")
    print(f"DIPOL  = 0.5 0.5 {z_center_com:.4f}")

if __name__ == "__main__":
    calculate_periodic_dipol("asymm_defect.vasp")