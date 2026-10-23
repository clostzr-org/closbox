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
import sys

def supports_color():
    """Returns True if the current terminal environment supports ANSI colors."""
    # 1. Check if output is redirected to a file or log
    if not sys.stdout.isatty():
        return False
        
    # 2. Check for the industry-standard NO_COLOR environment variable
    if "NO_COLOR" in os.environ:
        return False
        
    # 3. Check for specific terminal environments
    term = os.environ.get("TERM", "").lower()
    if term in ("dumb", "unknown"):
        return False
        
    # Windows-specific check: PyCharm/VSCode terminals handle it, but raw CMD needs care
    if os.name == "nt":
        # Returns True if running in modern Windows Terminal or IDEs
        return "ANSICON" in os.environ or "WT_SESSION" in os.environ or os.environ.get("TERM_PROGRAM") == "vscode"

    return True

# Global flag to track color availability
COLOR_ENABLED = supports_color()

def ansi_color(fg=None, bg=None, bold=False, underline=False, bright=False, reset=False):
    # CRITICAL: If colors are not supported/enabled, return an empty string immediately
    if not COLOR_ENABLED:
        return ""

    if reset:
        return '\033[0m'

    colors = {
        'black': 0, 'red': 1, 'green': 2, 'yellow': 3,
        'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7
    }
    
    codes = []
    if bold: codes.append("1")
    if underline: codes.append("4")
        
    if fg in colors:
        base = 9 if bright else 3
        codes.append(f"{base}{colors[fg]}")
        
    if bg in colors:
        base = 10 if bright else 4
        codes.append(f"{base}{colors[bg]}")
        
    return f"\033[{';'.join(codes)}m" if codes else ""

# -------------------------------------------------------------
# Dynamic Class Setup
# -------------------------------------------------------------
class Color:
      pass

# Dynamically populate shortcuts
color_list = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for name in color_list:
    short_name = name[:3]
    setattr(Color, f"f_{short_name}", ansi_color(fg=name))
    setattr(Color, f"b_{short_name}", ansi_color(bg=name))

Color.reset = ansi_color(reset=True)

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
