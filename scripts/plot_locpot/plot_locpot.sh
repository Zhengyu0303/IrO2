# LOCPOT — auto isovalue
python plot_vasp_isosurface.py --file LOCPOT --auto

# LOCPOT — explicit ±0.5 eV iso-level
python plot_vasp_isosurface.py --file LOCPOT --isovalue 0.5

# CHGCAR charge density — explicit range
python plot_vasp_isosurface.py --file CHGCAR --isorange 0.01 0.1

# CHGCAR spin density (diff channel)
python plot_vasp_isosurface.py --file CHGCAR --spin --auto

# Save to HTML instead of opening browser
python plot_vasp_isosurface.py --file LOCPOT --auto --output locpot.html