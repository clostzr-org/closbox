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
import re
import argparse
import subprocess
import pykakasi

def setup_converter():
    """Initializes pykakasi using the modern API."""
    return pykakasi.kakasi()

def convert_japanese_to_kunrei(text, kks):
    """Converts text to Kunrei-shiki romaji using the modern dict structure."""
    result_fragments = kks.convert(text)
    romaji_list = [item['kunrei'] for item in result_fragments]
    return "".join(romaji_list)

def translate_text(text):
    """Calls translate-shell to fetch English meaning safely."""
    if not text.strip():
        return ""
    try:
        result = subprocess.run(
            ["trans", "-brief", "-to", "en", "-no-warn", text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        translated = result.stdout.strip()
        return translated if translated and not result.stderr else ""
    except Exception:
        return ""

def clean_string(text):
    """Replaces spaces and invalid filename characters with underscores."""
    sanitized = text.replace(" ", "_")
    for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        sanitized = sanitized.replace(char, "_")
    return sanitized

def has_japanese(text):
    """Checks if a string contains Japanese characters (Kanji, Hiragana, Katakana)."""
    # Unicode ranges for Japanese script elements
    return bool(re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', text))

def is_already_formatted(filename):
    """
    Checks if the filename already matches the target pattern:
    'original_text_-_kunrei_-_english_translation'
    """
    # This looks for two distinct '_-_' separator groups in the name string
    parts = filename.split('_-_')
    return len(parts) >= 3

def process_filename(filename, kks):
    """Generates the new name in 'original - kunrei - english' format."""
    name_without_ext, ext = os.path.splitext(filename)
    
    # 1. Skip if it doesn't contain Japanese, or if it already matches our naming pattern
    if not has_japanese(name_without_ext) or is_already_formatted(name_without_ext):
        return filename

    # 2. Generate the building blocks
    original_part = clean_string(name_without_ext)
    
    romaji_raw = convert_japanese_to_kunrei(name_without_ext, kks)
    romaji_part = clean_string(romaji_raw)
    
    english_raw = translate_text(name_without_ext)
    english_part = clean_string(english_raw)
    
    # 3. Assemble components based on translation availability
    if english_part and english_part.lower() != original_part.lower():
        combined_name = f"{original_part}_-_{romaji_part}_-_{english_part}"
    else:
        combined_name = f"{original_part}_-_{romaji_part}"
        
    return combined_name + ext

def rename_file(file_path, kks):
    """Renames a single target file if changes are required."""
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    
    new_base_name = process_filename(base_name, kks)
    
    if base_name != new_base_name:
        new_file_path = os.path.join(dir_name, new_base_name)
        try:
            os.rename(file_path, new_file_path)
            print(f"[RENAMED] {base_name}\n       -> {new_base_name}\n")
        except Exception as e:
            print(f"[ERROR] Could not rename {base_name}: {e}\n", file=sys.stderr)
    else:
        print(f"[SKIPPED] Already formatted or no Japanese: {base_name}")

def rename_directory_recursive(dir_path, kks):
    """Recursively parses folder paths bottom-up to prevent tree breakage."""
    if not os.path.exists(dir_path):
        print(f"[ERROR] Directory does not exist: {dir_path}", file=sys.stderr)
        return

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for file in files:
            full_path = os.path.join(root, file)
            rename_file(full_path, kks)
            
        for d in dirs:
            full_path = os.path.join(root, d)
            rename_file(full_path, kks)

def main():
    parser = argparse.ArgumentParser(description="Smart rename Japanese files to 'Original_-_Kunrei_-_English' format.")
    parser.add_argument("path", help="Path to target file or folder")
    
    args = parser.parse_args()
    target_path = os.path.abspath(args.path)
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)
        
    kks = setup_converter()
    
    if os.path.isfile(target_path):
        print(f"Target: Single File -> {target_path}\n")
        rename_file(target_path, kks)
    elif os.path.isdir(target_path):
        print(f"Target: Directory Tree -> {target_path}\n")
        rename_directory_recursive(target_path, kks)

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
