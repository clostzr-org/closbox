#!/data/data/com.termux/files/usr/bin/bash

# Filename Desymbolizer - strips non-alphanumerics and preserves specific symbols
# Usage: desym.sh [filename]

if [[ -z "$1" ]]; then
    echo -e "filename desymbolizer - strip all non-alphanumerics\n--usage: $(basename "$0") [filename]"
    exit 1
fi

# Process all arguments as a single string, replacing characters not in the allowed set with underscores
echo "$*" | sed -E 's/[^a-zA-Z0-9\/\(\)\#\+~\.\-\[\]]/_/g'
