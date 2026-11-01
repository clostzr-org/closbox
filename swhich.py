#!/data/data/com.termux/files/usr/bin/python
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

import time
start_time = time.time()

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
import shutil

def swhich(name):
    import shutil
    """Check whether `name` is on PATH and marked as executable."""
    return shutil.which(name) is not None

# Example usage:
def example(name):
    if swhich(name):
       print(f"The '{name}' command is installed.")
    else:
       print(f"The '{name}' command is not installed.")

if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   example(sys.argv[1])
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
