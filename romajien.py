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
#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
import pykakasi

def setup_converter():
    """Initializes and configures pykakasi for Kunrei-shiki Romaji."""
    kks = pykakasi.kakasi()
    kks.setMode("H", "a")  # Hiragana to Romaji
    kks.setMode("K", "a")  # Katakana to Romaji
    kks.setMode("J", "a")  # Kanji to Romaji
    kks.setMode("r", "Kunrei")  # Set Romaji system to Kunrei
    return kks.getConverter()

def translate_text(text):
    """Calls translate-shell to fetch English meaning safely."""
    if not text.strip():
        return ""
    try:
        # -brief: translation only, -to en: output language, -no-warn: suppress network warnings
        result = subprocess.run(
            ["trans", "-brief", "-to", "en", "-no-warn", text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10  # Protection against network hangs
        )
        translated = result.stdout.strip()
        # Fallback if translate-shell returns empty or an unexpected error
        return translated if translated and not result.stderr else ""
    except Exception:
        return ""

def clean_string(text):
    """Replaces spaces and invalid filename special characters with underscores."""
    # Replace all white spaces
    sanitized = text.replace(" ", "_")
    # Clean characters that break terminal or filesystem paths
    for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        sanitized = sanitized.replace(char, "_")
    return sanitized

def process_filename(filename, converter):
    """Generates the new name containing Kunrei Romaji and English translation suffix."""
    name, ext = os.path.splitext(filename)
    
    # 1. Romaji Conversion
    romaji_part = converter.do(name)
    
    # 2. English Translation
    english_part = translate_text(name)
    
    # 3. Assemble and sanitize string
    if english_part and english_part.lower() != name.lower():
        # Scheme: Romaji_-_English_Translation.ext
        combined_name = f"{romaji_part}_-_{english_part}"
    else:
        combined_name = romaji_part
        
    final_name = clean_string(combined_name) + ext
    return final_name

def rename_file(file_path, converter):
    """Renames a single target file if changes are required."""
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    
    new_base_name = process_filename(base_name, converter)
    
    if base_name != new_base_name:
        new_file_path = os.path.join(dir_name, new_base_name)
        try:
            os.rename(file_path, new_file_path)
            print(f"[SUCCESS] {base_name} -> {new_base_name}")
        except Exception as e:
            print(f"[ERROR] Could not rename {base_name}: {e}", file=sys.stderr)
    else:
        print(f"[SKIPPED] File matches criteria: {base_name}")

def rename_directory_recursive(dir_path, converter):
    """Recursively parses folder path bottom-up to prevent pathing issues."""
    if not os.path.exists(dir_path):
        print(f"[ERROR] Directory does not exist: {dir_path}", file=sys.stderr)
        return

    # topdown=False parses innermost files first so parent folder modifications won't break iteration loops
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for file in files:
            full_path = os.path.join(root, file)
            rename_file(full_path, converter)
            
        for d in dirs:
            full_path = os.path.join(root, d)
            rename_file(full_path, converter)

def main():
    parser = argparse.ArgumentParser(description="Rename Japanese files to Kunrei Romaji with English translation suffix.")
    parser.add_argument("path", help="Path to target file or folder")
    
    args = parser.parse_args()
    target_path = os.path.abspath(args.path)
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)
        
    converter = setup_converter()
    
    if os.path.isfile(target_path):
        print(f"Target: Single File -> {target_path}")
        rename_file(target_path, converter)
    elif os.path.isdir(target_path):
        print(f"Target: Directory Tree -> {target_path}")
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
