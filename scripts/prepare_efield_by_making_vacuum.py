#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:51:05 2026

@author: zhengyuliu

pymatgen version of add_vacuum_split_slab.py
 
Turn a periodic  slab | H2O | (same slab via PBC)  cell into
              slab_low | H2O | slab_up | vacuum
by cutting the IrO2(110) slab between two stoichiometric trilayers and
inserting a vacuum gap. The block is centred at z = 0.5, so with
IDIPOL = 3, DIPOL = 0.5 0.5 0.5 the sawtooth jump sits at z = 0 (mid-vacuum).
 
Usage:
  python add_vacuum_split_slab_pmg.py POSCAR --vac 15 --mode 2+3   # same atoms
  python add_vacuum_split_slab_pmg.py POSCAR --vac 15 --mode 3+3   # +1 trilayer
 
Assumes an orthogonal cell with c along z.
"""
import argparse
import numpy as np
from pymatgen.core import Structure, Lattice
from pymatgen.io.vasp import Poscar

p = argparse.ArgumentParser()
p.add_argument("poscar")
p.add_argument("--vac", type=float, default=15.0, help="vacuum gap in Å (O to O)")
p.add_argument("--mode", choices=["2+3", "3+3"], default="2+3")
p.add_argument("--cut", type=float, default=0.95,
               help="fractional z (unwrapped, 0.5-1.5) of the cut between trilayers")
p.add_argument("--tri", type=float, default=0.10,
               help="trilayer thickness in fractional z (3.215 Å here)")
p.add_argument("-o", "--out", default=None)
args = p.parse_args()
 
s = Structure.from_file(args.poscar)
c = s.lattice.c
species = np.array([site.specie.symbol for site in s])
frac = s.frac_coords.copy()
 
# --- water = H + any O with an H within 1.25 Å (PBC-aware) --------------------
is_water = species == "H"
for i, site in enumerate(s):
    if species[i] == "O":
        if any(n.specie.symbol == "H" for n in s.get_neighbors(site, 1.25)):
            is_water[i] = True
is_slab = ~is_water
 
# --- unwrap the slab, which straddles the PBC boundary -------------------------
zu = frac[:, 2].copy()
zu[is_slab & (zu < 0.5)] += 1.0
 
cart = s.lattice.get_cartesian_coords(frac)
cart[:, 2] = zu * c
 
zc = args.cut
upper = is_slab & (zu < zc)
lower = is_slab & (zu > zc)
 
sp_list, xyz_list, idx_list = [], [], []
lo = cart[lower].copy(); lo[:, 2] -= c                     # put lower slab under the water
for mask, xyz in [(lower, lo), (is_water, cart[is_water]), (upper, cart[upper])]:
    sp_list.append(species[mask]); xyz_list.append(xyz); idx_list.append(np.where(mask)[0])
 
if args.mode == "3+3":
    extra = is_slab & (zu > zc) & (zu < zc + args.tri)     # trilayer just above the cut
    sp_list.append(species[extra]); xyz_list.append(cart[extra].copy())
    idx_list.append(10**6 + np.arange(extra.sum()))        # sort after original atoms
 
sp = np.concatenate(sp_list)
xyz = np.vstack(xyz_list)
idx = np.concatenate(idx_list)
 
zmin, zmax = xyz[:, 2].min(), xyz[:, 2].max()
c_new = (zmax - zmin) + args.vac
xyz[:, 2] += c_new / 2 - (zmin + zmax) / 2                 # centre block at c/2
 
m = s.lattice.matrix
lat = Lattice([m[0], m[1], [0.0, 0.0, c_new]])
 
# element order as in the original POSCAR; original atom order kept inside each element
order = []
for el in dict.fromkeys(species):
    k = np.where(sp == el)[0]
    order += list(k[np.argsort(idx[k])])
 
new = Structure(lat, sp[order].tolist(), xyz[order], coords_are_cartesian=True)
 
out = args.out or f"POSCAR_vac{args.vac:g}_{args.mode}_pmg"
Poscar(new).write_file(out)
print(f"written {out}: {new.composition.formula}  c = {c_new:.3f} Å")
print("INCAR: IDIPOL = 3 ; LDIPOL = .TRUE. ; DIPOL = 0.5 0.5 0.5  (jump at z = 0)")