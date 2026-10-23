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

# Get all files in current directory (skip directories)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
if not files:
    print("No files found in current directory.")
    exit()

# Regex pattern to find numeric parts in filenames (handles numbers before extension)
num_pattern = re.compile(r'(\d+)', re.IGNORECASE)
file_numbers = []

# First pass: collect all numeric parts and their original filenames
file_info = []
for filename in files:
    name_part, ext_part = os.path.splitext(filename)
    nums = num_pattern.findall(name_part)
    if nums:
        # Take the last numeric segment as the target number (adjust if needed)
        main_num = nums[-1]
        file_info.append((filename, name_part, ext_part, int(main_num), len(main_num)))
        file_numbers.append(len(main_num))
    else:
        # Files without numbers stay unchanged
        file_info.append((filename, name_part, ext_part, None, 0))

if not file_numbers:
    print("No files with numeric numbering found.")
    exit()

# Determine maximum digit length across all numeric parts
max_digits = max(file_numbers)

# Second pass: rename files with padding
for filename, name_part, ext_part, main_num, num_len in file_info:
    if main_num is not None and num_len < max_digits:
        # Replace the last numeric segment with padded version
        padded_num = f"{main_num:0{max_digits}d}"
        new_name = num_pattern.sub(lambda m: padded_num if m.group() == str(main_num) else m.group(), name_part) + ext_part
        # Avoid overwriting existing files
        if new_name != filename and not os.path.exists(new_name):
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")
        elif new_name == filename:
            print(f"No change needed: {filename}")
        else:
            print(f"Skipped {filename} (target name {new_name} already exists)")
    else:
        print(f"No change needed: {filename}")


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
