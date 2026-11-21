from plot_vasp_planar_avg import plot_planar_avg#plot_locpot, plot_chgcar

fig = plot_planar_avg("LOCPOT", isovalue=0.5, opacity=0.3)
fig.show()

# fig = plot_chgcar("CHGCAR", spin=False, isovalue=[0.01, 0.08])
# fig.show()