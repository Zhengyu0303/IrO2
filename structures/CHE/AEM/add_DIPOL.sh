#!/bin/bash

for dir in */; do
    # Strip the trailing slash for cleaner terminal output
    dir_name="${dir%/}"
    echo "Processing: $dir_name"

    # Safely enter the directory
    cd "$dir" || continue

    # Move everything from subdirectories into this directory
    # 2>/dev/null hides the error if there are no subdirectories present
    mv */* . 2>/dev/null

    # Optional: Remove the subdirectories which are now empty
    # Uncomment the line below if you want to clean them up
    # find . -maxdepth 1 -type d -empty -delete

    # Return to the parent directory
    cd ..
done
