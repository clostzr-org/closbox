#!/data/data/com.termux/files/usr/bin/python
import time
import os
import sys
import shutil
import string
from tcget import tcget

# Timing start
start_time = time.time()

# Define paths
home = '/data/data/com.termux/files/home'
hbak = home + '/bak'
hbin = home + '/bin'

# Append to sys.path if needed
if hbin not in sys.path:
    sys.path.append(hbin)

from ansicolors import *

# Script path handling
spath = sys.argv[0]
if os.path.islink(spath):
    spath = os.readlink(spath)
sdn = os.path.dirname(spath)
sbn = os.path.basename(spath)
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'

# Initialize variables
verbose = False

# Call osl for some processing (assuming it's defined elsewhere)
import osl
osl.osl(spath)
for message in osl.info:
    print(f'{message}')

# Function to sanitize filenames
def nosym(someString):
    someString = someString.replace(' ', '_')
    SPECIAL_CHARS = '_-[].+()'
    PERMITTED_CHARS = string.digits + string.ascii_letters + SPECIAL_CHARS
    someString = "".join(c for c in someString if c in PERMITTED_CHARS)
    return someString

# Determine target directory
tcg_path = tcget()
target_dir = None

# Check if tcg exists and is a directory
if os.path.isdir(tcg_path):
    target_dir = tcg_path
    print(f"Using tcg: {target_dir}")
else:
    # No valid tcg, check for command-line argument
    args = sys.argv[1:]
    if args:
        arg_path = args[0]
        if os.path.exists(arg_path):
            target_dir = arg_path
            print(f"Using argument path: {target_dir}")
        else:
            print(f"Path provided does not exist: {arg_path}")
            # Prompt user if path doesn't exist
            user_input = input("Enter a directory or file path: ").strip()
            if os.path.exists(user_input):
                target_dir = user_input
            else:
                print("Invalid path provided.")
                sys.exit(1)
    else:
        # Prompt user for input
        user_input = input("Please enter a directory or file path: ").strip()
        if os.path.exists(user_input):
            target_dir = user_input
        else:
            print("Invalid path entered.")
            sys.exit(1)

# Function to rename files/directories recursively
def rename_recursive(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in dirs + files:
                full_path = os.path.join(root, name)
                new_name = nosym(name)
                if name != new_name:
                    new_full_path = os.path.join(root, new_name)
                    print(f"Renaming: {full_path} -> {new_full_path}")
                    shutil.move(full_path, new_full_path)
    elif os.path.isfile(path):
        dir_name = os.path.dirname(path)
        base_name = os.path.basename(path)
        new_name = nosym(base_name)
        if base_name != new_name:
            new_path = os.path.join(dir_name, new_name)
            print(f"Renaming: {path} -> {new_path}")
            shutil.move(path, new_path)
    else:
        print(f"Path does not exist: {path}")

# Perform renaming
if os.path.isdir(target_dir):
    rename_recursive(target_dir)
elif os.path.isfile(target_dir):
    rename_recursive(target_dir)
else:
    print("Target path is invalid.")
    sys.exit(1)

input('Press ENTER to exit.')