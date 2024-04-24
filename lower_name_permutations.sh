#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found."
    exit 1
fi

output_file="${1%.txt}_wordlist.txt" 

# replace space with a dot and put everything in lowercase
sed  -e 's/ /./g' -e 's/[[:upper:]]/\L&/g' "$1" > "$output_file"

# reverse firstname and lastname, seprate with a dot and all in lowercase
awk '{print tolower($2 "." $1)}' "$1" >> "$output_file"

# Keep first letter, put a dot and lowercase everything
awk '{print tolower( substr($1, 1, 1) "." $2)}' "$1" >> "$output_file"

echo "Operation Success, file at: $(pwd)/$output_file"
