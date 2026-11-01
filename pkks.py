#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if  not hbin in sys.path:
    sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if  os.path.islink(spath):
    spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import osl; osl.osl(spath)
for message in osl.info:
    print(f'{message}')

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr} {frs}
 function: {fyl} {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here
import os
import re
try:
    import pykakasi
except Exception:
    os.system(f'pip install pykakasi')
    import pykakasi
from pathlib import Path
#!/usr/bin/env python3
import os
import sys
import argparse
import pykakasi

def setup_converter():
    """Initializes and configures pykakasi for Kunrei-shiki Romaji."""
    kks = pykakasi.kakasi()
    # Configure output to Kunrei-shiki romanization style
    kks.setMode("H", "a")  # Hiragana to Romaji
    kks.setMode("K", "a")  # Katakana to Romaji
    kks.setMode("J", "a")  # Kanji to Romaji
    kks.setMode("r", "Kunrei")  # Set Romaji system to Kunrei
    return kks.getConverter()

def convert_text(text, converter):
    """Converts Japanese text to Kunrei romaji and replaces spaces with underscores."""
    # Convert Japanese characters
    converted = converter.do(text)
    # Replace all white spaces with underscores
    sanitized = converted.replace(" ", "_")
    return sanitized

def rename_file(file_path, converter):
    """Renames a single file if its name contains changes."""
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    
    new_base_name = convert_text(base_name, converter)
    
    if base_name != new_base_name:
        new_file_path = os.path.join(dir_name, new_base_name)
        try:
            os.rename(file_path, new_file_path)
            print(f"[RENAMED] {base_name} -> {new_base_name}")
        except Exception as e:
            print(f"[ERROR] Could not rename {base_name}: {e}", file=sys.stderr)
    else:
        print(f"[SKIPPED] No changes needed for: {base_name}")

def rename_directory_recursive(dir_path, converter):
    """Recursively walks through a directory and renames files."""
    if not os.path.exists(dir_path):
        print(f"[ERROR] Directory does not exist: {dir_path}", file=sys.stderr)
        return

    # topdown=False is critical so files get renamed before their parent directories change
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # Rename files first
        for file in files:
            full_path = os.path.join(root, file)
            rename_file(full_path, converter)
            
        # Optional: Rename directories as well if they contain Japanese characters
        for d in dirs:
            full_path = os.path.join(root, d)
            rename_file(full_path, converter)

def main():
    parser = argparse.ArgumentParser(description="Rename Japanese files to Kunrei Romaji and clean spaces.")
    parser.add_argument("path", help="Path to the file or directory to process")
    
    args = parser.parse_args()
    target_path = os.path.abspath(args.path)
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)
        
    converter = setup_converter()
    
    if os.path.isfile(target_path):
        print(f"Processing single file: {target_path}")
        rename_file(target_path, converter)
    elif os.path.isdir(target_path):
        print(f"Processing directory recursively: {target_path}")
        rename_directory_recursive(target_path, converter)

if __name__ == "__main__":
    main()



if  __name__ == '__main__':
    try:
      if  sys.argv[1] == '-h':
          usg()
          sys.exit()
    except Exception:
      pass
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
