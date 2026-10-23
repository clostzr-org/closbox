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
def ansi_color(fg=None, bg=None, bold=False, underline=False, bright=False, reset=False):
    # Base numbers for standard colors
    colors = {
        'black': 0, 'red': 1, 'green': 2, 'yellow': 3,
        'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7
    }
    
    if reset:
        return '\033[0m'
        
    codes = []
    
    # 1. Handle Text Styles (Bold/Underline)
    if bold:
        codes.append("1")
    if underline:
        codes.append("4")
        
    # 2. Handle Foreground Colors (Standard: 30-37, Bright: 90-97)
    if fg in colors:
        base = 9 if bright else 3
        codes.append(f"{base}{colors[fg]}")
        
    # 3. Handle Background Colors (Standard: 40-47, Bright: 100-107)
    if bg in colors:
        base = 10 if bright else 4
        codes.append(f"{base}{colors[bg]}")
        
    # Join all elements with a semicolon if codes exist
    return f"\033[{';'.join(codes)}m" if codes else ""

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
