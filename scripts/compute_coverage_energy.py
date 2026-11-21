#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:35:35 2026

@author: zhengyuliu
"""
import numpy as np
import matplotlib.pyplot as plt

##Results from Relaxation and AIMD

E_f = -3.0675 # in eV formation energy of water molecule, H2O(aimd) - H2 - 1/2O2
E_bulk = -21.828785 # eV per formula unit
A = 6.3779691351338155*12.8580661768673767 # in ang squared



def chemical_potential(U, pH, T = 300, U_SHE = -4.73):
    
    mu_H = -(U - U_SHE) - 8.61733*10**(-5)*T*np.log(10)*pH
    mu_O = -3.0675 - 2*mu_H
    
    return mu_H, mu_O

def get_energy(E, a, b, c, d, pH, U):
    
    E_surf = (1/(2*A))*(E - 40*E_bulk - (b + c)*chemical_potential(U, pH)[0] - (a+b-d)*chemical_potential(U, pH)[1])
    
    return E_surf

##-------

energies = {}
with open("results.txt") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 2:
            continue                 # skip blank or broken lines
        cov, val = parts[0], parts[1]
        energies[cov] = None if val == "None" else float(val)

print(energies)

labels = {}
with open("labels.txt") as f:
    next(f)                      # skip the first line
    for line in f:
        parts = line.split()
        if len(parts) < 5:
            continue
        labels[parts[0]] = list(float(x) for x in parts[1:5])
        
final_results = {}

pH = 1
U = np.linspace(-1.0, 2.0, 300)

# plt.figure()

# for cov, E in energies.items():        # only converged coverages
#     a, b, c, d = labels[cov]           # the 4 numbers for this coverage
#     G = [get_energy(E, a, b, c, d, pH, u) for u in U]
#     #print(a, b, c, d,E,  "\n")
#     plt.plot(U, G, label=cov)
# #print(get_energy(-891.75573, 0, 2, 3, 0, 0, 1))



# plt.xlabel("U (V)")
# plt.ylabel("ΔG (eV)")
# plt.title(f"pH = {pH}")
# #plt.legend(fontsize=7)
# plt.show()




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

U = np.linspace(-0.5, 2.0, 200)
pH0 = 0

def G_curve(cov, pH):
    a, b, c, d = labels[cov]
    return [get_energy(energies[cov], a, b, c, d, pH, u) for u in U]

fig = plt.figure()
ax = plt.gca()                        # the one plot
plt.subplots_adjust(bottom=0.2)       # leave room for the slider

lines = {}
for cov in energies:
    if cov not in labels:
        continue
    lines[cov], = ax.plot(U, G_curve(cov, pH0), label=cov)

ax.set_xlabel("U (V)")
ax.set_ylabel("ΔG (eV)")
ax.set_title(f"pH = {pH0}")
#ax.legend(fontsize=7)

# slider underneath the plot
slider_ax = fig.add_axes([0.15, 0.05, 0.7, 0.03])
pH_slider = Slider(slider_ax, "pH", 0, 14, valinit=pH0)

def update(val):
    pH = pH_slider.val
    for cov, line in lines.items():
        line.set_ydata(G_curve(cov, pH))
    ax.relim(); ax.autoscale_view()
    ax.set_title(f"pH = {pH:.1f}")
    fig.canvas.draw_idle()

pH_slider.on_changed(update)
plt.show()
