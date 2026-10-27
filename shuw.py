#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if not hbin in sys.path:
   sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if os.path.islink(spath):
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

args = sys.argv[1:]
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
import subprocess
import shutil

def is_program_installed(program_name):
    """
    Checks if a program is installed by attempting to find it in the system's PATH.
    Returns True if the program is found, False otherwise.
    """
    try:
        # Use shutil.which to find the executable in the PATH
        program_path = shutil.which(program_name)
        if program_path:
            print(f"Found {program_name} at: {program_path}")  # Optional, shows location
            return True
        else:
            return False  # Program not found in PATH

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        program_to_check = sys.argv[1]  # Get the program name from command-line arguments
        if is_program_installed(program_to_check):
            print(f"{program_to_check} is installed.")
        else:
            print(f"{program_to_check} is not installed or not in your PATH.")
            os.system(f'apt install {program_to_check} -y')
    else:
        print("Please provide the program name as a command-line argument.")



if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
