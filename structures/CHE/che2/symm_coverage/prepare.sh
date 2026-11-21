#!bin/bash
for i in {0..137}; do
    directory="coverage$i"
    echo "Processing directory: $directory"
    cd "$directory" || { echo "Failed to change directory to $directory"; continue; }
    mv Ir*/* .
    rmdir Ir*_0
    rm *json
    cd ..
done
