import os

for root, dirs, files in os.walk("."):
    if "INCAR" not in files:
        continue
    incar_path = os.path.join(root, "INCAR")

    with open(incar_path) as f:
        lines = f.readlines()

    kept = [l for l in lines if not l.strip().upper().startswith("DIPOL")]

    if len(kept) != len(lines):
        with open(incar_path, "w") as f:
            f.writelines(kept)
        print(f"{incar_path}: removed {len(lines) - len(kept)} DIPOL line(s)")