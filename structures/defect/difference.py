#!/usr/bin/env python3
"""
diff_rhob_locpot.py

Compute the difference between two VASPsol++ RHOB grids written in
LOCPOT format (file1 - file2) and write the result as a new
LOCPOT-format file, viewable in VESTA, VMD, p4vasp, etc.

Requires: pymatgen
    pip install pymatgen

Usage:
    python diff_rhob_locpot.py RHOB_1 RHOB_2 -o RHOB_diff
"""

import argparse
import sys


def main():
    ap = argparse.ArgumentParser(
        description="Diff two VASPsol++ RHOB files in LOCPOT format (file1 - file2)."
    )
    ap.add_argument("file1", help="Path to first RHOB (LOCPOT-format) file")
    ap.add_argument("file2", help="Path to second RHOB (LOCPOT-format) file")
    ap.add_argument("-o", "--out", default="RHOB_diff",
                     help="Output LOCPOT-format file name (default: RHOB_diff)")
    args = ap.parse_args()

    try:
        from pymatgen.io.vasp.outputs import Locpot
    except ImportError:
        print("This script requires pymatgen. Install with:\n  pip install pymatgen",
              file=sys.stderr)
        sys.exit(1)

    try:
        v1 = Locpot.from_file(args.file1)
        v2 = Locpot.from_file(args.file2)
    except Exception as e:
        print(f"Error reading LOCPOT-format files: {e}", file=sys.stderr)
        sys.exit(1)

    key1 = next(iter(v1.data))
    key2 = next(iter(v2.data))
    shape1 = v1.data[key1].shape
    shape2 = v2.data[key2].shape

    if shape1 != shape2:
        print(f"Error: grid shapes differ ({shape1} vs {shape2}). "
              "Both RHOB files must be on the same FFT grid to diff directly "
              "(check NGXF/NGYF/NGZF or NGX/NGY/NGZ in your VASP runs).",
              file=sys.stderr)
        sys.exit(1)

    diff = v1.linear_add(v2, scale_factor=-1.0)
    diff.write_file(args.out)

    d = diff.data[key1]
    print(f"Grid shape:      {d.shape}")
    print(f"Diff min:        {d.min():.6e}")
    print(f"Diff max:        {d.max():.6e}")
    print(f"Diff mean:       {d.mean():.6e}")
    print(f"Diff std dev:    {d.std():.6e}")
    print(f"Mean |diff|:     {abs(d).mean():.6e}")
    print(f"\nWrote difference grid ({args.file1} - {args.file2}) to: {args.out}")
    print("Open it in VESTA/VMD/p4vasp to view the 3D difference.")


if __name__ == "__main__":
    main()