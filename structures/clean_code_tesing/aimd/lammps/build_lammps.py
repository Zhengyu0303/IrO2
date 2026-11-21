# print("loading environment")
# import os

# # =====================================================================
# # Settings  (mirrors the settings-block style of your friend's script:
# # everything you're likely to want to change lives here, up top)
# # =====================================================================

# packmol_xyz_file        = "bulk_water.xyz"          # Packmol output to convert
# lammps_data_file         = "water_tip3p.data"         # LAMMPS data file to write
# lammps_input_file        = "in.water_tip3p"           # LAMMPS input script to write

# # Simulation box (Angstrom). Packmol's plain xyz output carries no box info,
# # so this was derived from the coordinate bounding box of bulk_water.xyz
# # with a small safety pad -> gives density ~0.98 g/cm3, close to real water.
# # If you know the exact "inside box" region you gave Packmol, put those
# # numbers here instead.
# box_bounds = {
#     "xlo": -0.8, "xhi": 6.4,
#     "ylo": -0.1, "yhi": 12.95,
#     "zlo": -0.1, "zhi": 15.1,
# }

# # TIP3P parameters, per https://docs.lammps.org/Howto_tip3p.html
# atom_type_to_label = {1: "O", 2: "H"}
# atom_type_to_mass  = {1: 15.9994, 2: 1.008}
# atom_type_to_charge = {1: -0.834, 2: 0.417}
# lj_O_epsilon, lj_O_sigma = 0.1521, 3.1507     # kcal/mol, Angstrom (O-O only; H has no LJ)
# oh_bond_length  = 0.9572                       # Angstrom
# hoh_angle_deg   = 104.52                       # degrees

# # Run settings
# run_seed          = 12345
# target_temp_K     = 300.0
# softstart_temp_K  = 10.0
# softstart_dt_fs   = 0.1
# softstart_steps   = 2000
# softstart_limit_A = 0.05          # max per-atom displacement per step (nve/limit)
# production_dt_fs  = 1.0
# production_steps  = 20000
# nvt_damping_fs    = 100.0
# dump_every        = 500
# thermo_every      = 100


# # =====================================================================
# # Step 1: parse the Packmol xyz into a flat atom list
# # =====================================================================

# def parse_packmol_xyz(path):
#     with open(path) as f:
#         lines = f.readlines()
#     n = int(lines[0].strip())
#     atoms = []
#     for line in lines[2:2 + n]:
#         parts = line.split()
#         sym = parts[0]
#         x, y, z = map(float, parts[1:4])
#         atoms.append((sym, x, y, z))
#     if len(atoms) % 3 != 0:
#         raise ValueError(
#             f"{path} has {len(atoms)} atoms; expected a multiple of 3 "
#             "(one O + two H per water molecule, in that order)."
#         )
#     return atoms


# # =====================================================================
# # Step 2: write the LAMMPS data file (atom_style full: charges + bonds + angles)
# # =====================================================================

# def write_lammps_data(atoms, box, out_path):
#     nwater = len(atoms) // 3
#     label_to_type = {v: k for k, v in atom_type_to_label.items()}

#     atom_lines, bond_lines, angle_lines = [], [], []
#     aid = bid = anid = 0
#     for w in range(nwater):
#         o, h1, h2 = atoms[3 * w], atoms[3 * w + 1], atoms[3 * w + 2]
#         if o[0] != "O" or h1[0] != "H" or h2[0] != "H":
#             raise ValueError(
#                 f"Water #{w+1} isn't in O,H,H order (got {o[0]},{h1[0]},{h2[0]}) "
#                 "- check your Packmol structure order."
#             )
#         mol = w + 1

#         aid += 1; o_id = aid
#         atom_lines.append(
#             f"{aid} {mol} {label_to_type['O']} {atom_type_to_charge[1]:.3f} "
#             f"{o[1]:.6f} {o[2]:.6f} {o[3]:.6f}"
#         )
#         aid += 1; h1_id = aid
#         atom_lines.append(
#             f"{aid} {mol} {label_to_type['H']} {atom_type_to_charge[2]:.3f} "
#             f"{h1[1]:.6f} {h1[2]:.6f} {h1[3]:.6f}"
#         )
#         aid += 1; h2_id = aid
#         atom_lines.append(
#             f"{aid} {mol} {label_to_type['H']} {atom_type_to_charge[2]:.3f} "
#             f"{h2[1]:.6f} {h2[2]:.6f} {h2[3]:.6f}"
#         )

#         bid += 1; bond_lines.append(f"{bid} 1 {o_id} {h1_id}")
#         bid += 1; bond_lines.append(f"{bid} 1 {o_id} {h2_id}")
#         anid += 1; angle_lines.append(f"{anid} 1 {h1_id} {o_id} {h2_id}")

#     natoms, nbonds, nangles = len(atom_lines), len(bond_lines), len(angle_lines)

#     vol = (box["xhi"] - box["xlo"]) * (box["yhi"] - box["ylo"]) * (box["zhi"] - box["zlo"])
#     mass_g = nwater * 18.015 / 6.02214076e23
#     density = mass_g / (vol * 1e-24)
#     print(f"  {nwater} waters, box volume {vol:.1f} A^3, density {density:.3f} g/cm3")

#     with open(out_path, "w") as f:
#         f.write("LAMMPS data file for bulk TIP3P water, generated from Packmol output\n\n")
#         f.write(f"{natoms} atoms\n{nbonds} bonds\n{nangles} angles\n\n")
#         f.write("2 atom types\n1 bond types\n1 angle types\n\n")
#         f.write(f"{box['xlo']:.4f} {box['xhi']:.4f} xlo xhi\n")
#         f.write(f"{box['ylo']:.4f} {box['yhi']:.4f} ylo yhi\n")
#         f.write(f"{box['zlo']:.4f} {box['zhi']:.4f} zlo zhi\n\n")
#         f.write("Masses\n\n")
#         for t, label in atom_type_to_label.items():
#             f.write(f"{t} {atom_type_to_mass[t]}  # {label}\n")
#         f.write("\nAtoms # full\n\n")
#         f.write("\n".join(atom_lines) + "\n")
#         f.write("\nBonds\n\n")
#         f.write("\n".join(bond_lines) + "\n")
#         f.write("\nAngles\n\n")
#         f.write("\n".join(angle_lines) + "\n")

#     print(f"  wrote {out_path}: {natoms} atoms, {nbonds} bonds, {nangles} angles")


# # =====================================================================
# # Step 3: write the LAMMPS input script
# # (built with file.write() + f-strings, same pattern as your friend's
# #  prepare_relaxation_input()/prepare_phonopy_lammps_input() functions)
# # =====================================================================

# def write_lammps_input(out_path, data_file):
#     with open(out_path, "w") as f:
#         f.write(f"""# ---------------------------------------------------------------
# # Rigid TIP3P bulk water. Parameters per https://docs.lammps.org/Howto_tip3p.html
# # Generated by build_tip3p_lammps.py
# # ---------------------------------------------------------------

# units           real
# atom_style      full
# boundary        p p p

# read_data       {data_file}

# pair_style      lj/cut/coul/long 8.0
# kspace_style    pppm 1.0e-4

# pair_coeff      1 1 {lj_O_epsilon} {lj_O_sigma}      # O-O
# pair_coeff      2 2 0.0000 1.0000                    # H-H (no LJ)
# pair_coeff      1 2 0.0000 1.0000                    # O-H cross term irrelevant

# bond_style      zero
# bond_coeff      1 {oh_bond_length}

# angle_style     zero
# angle_coeff     1 {hoh_angle_deg}

# special_bonds   amber

# fix             fShake all shake 0.0001 20 0 b 1 a 1

# neighbor        2.0 bin
# neigh_modify    delay 0 every 1 check yes

# thermo          {thermo_every}
# thermo_style    custom step temp press pe ke etotal density

# # --- soft-start: fix shake is not compatible with "minimize", so relieve
# # any close contacts from Packmol packing via a displacement-capped run
# velocity        all create {softstart_temp_K} {run_seed} mom yes rot yes dist gaussian
# timestep        {softstart_dt_fs}
# fix             fLimit all nve/limit {softstart_limit_A}
# thermo          10
# run             {softstart_steps}
# unfix           fLimit

# # --- production NVT equilibration ---
# velocity        all create {target_temp_K} {run_seed} mom yes rot yes dist gaussian
# timestep        {production_dt_fs}
# fix             fNVT all nvt temp {target_temp_K} {target_temp_K} {nvt_damping_fs}

# dump            d1 all custom {dump_every} dump.water_tip3p.lammpstrj id mol type q x y z
# dump_modify     d1 sort id

# thermo          {thermo_every}
# run             {production_steps}

# write_data      water_tip3p_equilibrated.data
# """)
#     print(f"  wrote {out_path}")


# # =====================================================================
# # Main
# # =====================================================================

# if __name__ == "__main__":
#     assert os.path.exists(packmol_xyz_file), f"{packmol_xyz_file} not found"

#     print(f"parsing {packmol_xyz_file} ...")
#     atoms = parse_packmol_xyz(packmol_xyz_file)

#     print("writing LAMMPS data file ...")
#     write_lammps_data(atoms, box_bounds, lammps_data_file)

#     print("writing LAMMPS input script ...")
#     write_lammps_input(lammps_input_file, lammps_data_file)

#     print("done. Run with e.g.:")
#     print(f"  lmp -in {lammps_input_file} -log log.water_tip3p")

print("loading environment")
import os

# =====================================================================
# Settings  (mirrors the settings-block style of your friend's script:
# everything you're likely to want to change lives here, up top)
# =====================================================================

packmol_xyz_file        = "bulk_water.xyz"          # Packmol output to convert
lammps_data_file         = "water_tip3p.data"         # LAMMPS data file to write
lammps_input_file        = "in.water_tip3p"           # LAMMPS input script to write

# Simulation box (Angstrom). Packmol's plain xyz output carries no box info,
# so this was derived from the coordinate bounding box of bulk_water.xyz
# with a small safety pad -> gives density ~0.98 g/cm3, close to real water.
# If you know the exact "inside box" region you gave Packmol, put those
# numbers here instead.
box_bounds = {
    "xlo": -0.8, "xhi": 6.4,
    "ylo": -0.1, "yhi": 12.95,
    "zlo": -0.1, "zhi": 15.1,
}

# TIP3P parameters, per https://docs.lammps.org/Howto_tip3p.html
atom_type_to_label = {1: "O", 2: "H"}
atom_type_to_mass  = {1: 15.9994, 2: 1.008}
atom_type_to_charge = {1: -0.834, 2: 0.417}
lj_O_epsilon, lj_O_sigma = 0.1521, 3.1507     # kcal/mol, Angstrom (O-O only; H has no LJ)
oh_bond_length  = 0.9572                       # Angstrom
hoh_angle_deg   = 104.52                       # degrees

# Run settings
run_seed          = 12345
target_temp_K     = 300.0
softstart_temp_K  = 10.0
softstart_dt_fs   = 0.1
softstart_steps   = 2000
softstart_soft_max = 60.0          # final pair_style soft prefactor A (kcal/mol), ramped from 1.0
production_dt_fs  = 1.0
production_steps  = 20000
nvt_damping_fs    = 100.0
dump_every        = 500
thermo_every      = 100


# =====================================================================
# Step 1: parse the Packmol xyz into a flat atom list
# =====================================================================

def parse_packmol_xyz(path):
    with open(path) as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    atoms = []
    for line in lines[2:2 + n]:
        parts = line.split()
        sym = parts[0]
        x, y, z = map(float, parts[1:4])
        atoms.append((sym, x, y, z))
    if len(atoms) % 3 != 0:
        raise ValueError(
            f"{path} has {len(atoms)} atoms; expected a multiple of 3 "
            "(one O + two H per water molecule, in that order)."
        )
    return atoms


# =====================================================================
# Step 2: write the LAMMPS data file (atom_style full: charges + bonds + angles)
# =====================================================================

def write_lammps_data(atoms, box, out_path):
    nwater = len(atoms) // 3
    label_to_type = {v: k for k, v in atom_type_to_label.items()}

    atom_lines, bond_lines, angle_lines = [], [], []
    aid = bid = anid = 0
    for w in range(nwater):
        o, h1, h2 = atoms[3 * w], atoms[3 * w + 1], atoms[3 * w + 2]
        if o[0] != "O" or h1[0] != "H" or h2[0] != "H":
            raise ValueError(
                f"Water #{w+1} isn't in O,H,H order (got {o[0]},{h1[0]},{h2[0]}) "
                "- check your Packmol structure order."
            )
        mol = w + 1

        aid += 1; o_id = aid
        atom_lines.append(
            f"{aid} {mol} {label_to_type['O']} {atom_type_to_charge[1]:.3f} "
            f"{o[1]:.6f} {o[2]:.6f} {o[3]:.6f}"
        )
        aid += 1; h1_id = aid
        atom_lines.append(
            f"{aid} {mol} {label_to_type['H']} {atom_type_to_charge[2]:.3f} "
            f"{h1[1]:.6f} {h1[2]:.6f} {h1[3]:.6f}"
        )
        aid += 1; h2_id = aid
        atom_lines.append(
            f"{aid} {mol} {label_to_type['H']} {atom_type_to_charge[2]:.3f} "
            f"{h2[1]:.6f} {h2[2]:.6f} {h2[3]:.6f}"
        )

        bid += 1; bond_lines.append(f"{bid} 1 {o_id} {h1_id}")
        bid += 1; bond_lines.append(f"{bid} 1 {o_id} {h2_id}")
        anid += 1; angle_lines.append(f"{anid} 1 {h1_id} {o_id} {h2_id}")

    natoms, nbonds, nangles = len(atom_lines), len(bond_lines), len(angle_lines)

    vol = (box["xhi"] - box["xlo"]) * (box["yhi"] - box["ylo"]) * (box["zhi"] - box["zlo"])
    mass_g = nwater * 18.015 / 6.02214076e23
    density = mass_g / (vol * 1e-24)
    print(f"  {nwater} waters, box volume {vol:.1f} A^3, density {density:.3f} g/cm3")

    with open(out_path, "w") as f:
        f.write("LAMMPS data file for bulk TIP3P water, generated from Packmol output\n\n")
        f.write(f"{natoms} atoms\n{nbonds} bonds\n{nangles} angles\n\n")
        f.write("2 atom types\n1 bond types\n1 angle types\n\n")
        f.write(f"{box['xlo']:.4f} {box['xhi']:.4f} xlo xhi\n")
        f.write(f"{box['ylo']:.4f} {box['yhi']:.4f} ylo yhi\n")
        f.write(f"{box['zlo']:.4f} {box['zhi']:.4f} zlo zhi\n\n")
        f.write("Masses\n\n")
        for t, label in atom_type_to_label.items():
            f.write(f"{t} {atom_type_to_mass[t]}  # {label}\n")
        f.write("\nAtoms # full\n\n")
        f.write("\n".join(atom_lines) + "\n")
        f.write("\nBonds\n\n")
        f.write("\n".join(bond_lines) + "\n")
        f.write("\nAngles\n\n")
        f.write("\n".join(angle_lines) + "\n")

    print(f"  wrote {out_path}: {natoms} atoms, {nbonds} bonds, {nangles} angles")


# =====================================================================
# Step 3: write the LAMMPS input script
# (built with file.write() + f-strings, same pattern as your friend's
#  prepare_relaxation_input()/prepare_phonopy_lammps_input() functions)
# =====================================================================

def write_lammps_input(out_path, data_file):
    with open(out_path, "w") as f:
        f.write(f"""# ---------------------------------------------------------------
# Rigid TIP3P bulk water. Parameters per https://docs.lammps.org/Howto_tip3p.html
# Generated by build_tip3p_lammps.py
# ---------------------------------------------------------------

units           real
atom_style      full
boundary        p p p

read_data       {data_file}

bond_style      zero
bond_coeff      1 {oh_bond_length}

angle_style     zero
angle_coeff     1 {hoh_angle_deg}

special_bonds   amber

fix             fShake all shake 0.0001 20 0 b 1 a 1

neighbor        2.0 bin
neigh_modify    delay 0 every 1 check yes

thermo          {thermo_every}
thermo_style    custom step temp press pe ke etotal density

# --- soft-start: relieve close contacts from Packmol packing using a
# BOUNDED repulsive potential (pair_style soft) instead of the real,
# divergent lj/cut/coul/long. Because the force can never blow up, a plain
# fix nve is safe here -- no need for nve/limit's displacement cap, which
# LAMMPS itself warns is not meant to be combined with fix shake.
pair_style      soft 8.0
pair_coeff      * *     0.0            # ramped up via fix adapt below
kspace_style    none                   # soft potential has no electrostatics

variable        prefactor equal ramp(1.0,{softstart_soft_max})
fix             fSoftRamp all adapt 1 pair soft a * * v_prefactor

velocity        all create {softstart_temp_K} {run_seed} mom yes rot yes dist gaussian
timestep        {softstart_dt_fs}
fix             fNVE all nve
thermo          10
run             {softstart_steps}
unfix           fSoftRamp
unfix           fNVE

# --- switch to the real TIP3P nonbonded potential for production ---
pair_style      lj/cut/coul/long 8.0
kspace_style    pppm 1.0e-4
pair_coeff      1 1 {lj_O_epsilon} {lj_O_sigma}      # O-O
pair_coeff      2 2 0.0000 1.0000                    # H-H (no LJ)
pair_coeff      1 2 0.0000 1.0000                    # O-H cross term irrelevant

# --- production NVT equilibration ---
velocity        all create {target_temp_K} {run_seed} mom yes rot yes dist gaussian
timestep        {production_dt_fs}
fix             fNVT all nvt temp {target_temp_K} {target_temp_K} {nvt_damping_fs}

dump            d1 all custom {dump_every} dump.water_tip3p.lammpstrj id mol type q x y z
dump_modify     d1 sort id

thermo          {thermo_every}
run             {production_steps}

write_data      water_tip3p_equilibrated.data
""")
    print(f"  wrote {out_path}")


# =====================================================================
# Main
# =====================================================================

if __name__ == "__main__":
    assert os.path.exists(packmol_xyz_file), f"{packmol_xyz_file} not found"

    print(f"parsing {packmol_xyz_file} ...")
    atoms = parse_packmol_xyz(packmol_xyz_file)

    print("writing LAMMPS data file ...")
    write_lammps_data(atoms, box_bounds, lammps_data_file)

    print("writing LAMMPS input script ...")
    write_lammps_input(lammps_input_file, lammps_data_file)

    print("done. Run with e.g.:")
    print(f"  lmp -in {lammps_input_file} -log log.water_tip3p")