#!/bin/bash
dest="./left"
while IFS= read -r dir; do
    [ -z "$dir" ] && continue
    mv -n "$dir" "$dest/"
done < coverage_left.txt