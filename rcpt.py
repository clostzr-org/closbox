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

#!/data/data/com.termux/files/usr/bin/python
import os
import subprocess
import sys
import time

# --- Timing Setup ---
START_TIME = time.time()

# --- Fast ANSI Styling Matrix ---
# Generates direct, hardware-level escape codes efficiently without string parsing
ANSI_FG = {name: f"\033[{30+i}m" for i, name in enumerate(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])}
ANSI_BG = {name: f"\033[{40+i}m" for i, name in enumerate(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])}
RESET = "\033[0m"

# Quick Shortcuts (Foreground)
FBK, FRD, FGR, FYL, FBL, FMG, FCY, FWH = ANSI_FG.values()
# Quick Shortcuts (Background)
BBK, BRD, BGR, BYL, BBL, BMG, BCY, BWH = ANSI_BG.values()


def osl(source_file=None):
    """Creates a symbolic link for the script inside the Termux symlink matrix directory."""
    home = os.environ.get('HOME', '/data/data/com.termux/files/home')
    symdir = os.path.join(home, 'symlink')
    
    # Use fallback target if argument wasn't passed directly
    target = source_file if source_file else sys.argv[0]
    
    if not os.path.isfile(target) or not target.endswith('.py'):
        return ["[ - ] Target is not a valid Python script asset."]
        
    os.makedirs(symdir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(target))[0]
    link_path = os.path.join(symdir, base_name)
    
    try:
        if os.path.exists(link_path) or os.path.islink(link_path):
            os.remove(link_path)
        os.symlink(os.path.abspath(target), link_path)
        return [f"[ + ] Symbolic link successfully created: {link_path}"]
    except Exception as e:
        return [f"[ - ] Symbolic configuration fault: {e}"]


def display_usage(script_name):
    """Prints uniform command line interaction rules."""
    print(f"Usage: {script_name} [source] [destination_prefix]")


def run_rclone_sync(src, dst, drv):
    """Executes rclone operation with built-in auto-reconnect fallback mechanism."""
    cmd = ['rclone', 'copyto', src, dst, '-vvvv']
    try:
        # Use standard check_call to stream verbose output directly to Termux
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        if drv:
            print(f"{FYL}[ * ] Reconnecting remote drive sector: {drv}...{RESET}")
            # Run recovery dynamically through clean list arrays
            subprocess.run(['rclone', 'config', 'reconnect', drv], check=False)
            try:
                subprocess.check_call(cmd)
                return
            except subprocess.CalledProcessError as e:
                print(f"{FRD}[ - ] Terminal transfer failure execution step: {e}{RESET}")
                sys.exit(e.returncode)
        else:
            print(f"{FRD}[ - ] File operation execution failed and no remote driver string recognized.{RESET}")
            sys.exit(1)


def main():
    script_path = os.path.realpath(sys.argv[0])
    script_dir = os.path.dirname(script_path)
    script_name = os.path.splitext(os.path.basename(script_path))[0]

    # Process and print environment linking metrics instantly
    log_messages = osl(script_path)
    for msg in log_messages:
        print(msg)

    # Clean parsing of raw inputs and arguments
    args = sys.argv[1:]
    exargs_str = " ".join(args)
    print(f"exargs: {exargs_str}\nargs: {args}")

    if len(args) < 1:
        display_usage(script_name)
        sys.exit(1)

    src = args[0]
    if not os.path.exists(src):
        print(f"{FRD}[ - ] Target source location missing: {src}{RESET}")
        sys.exit(1)

    # Handle parameters and track dynamic driver namespaces safely
    dst = os.path.basename(src)
    drv = None

    if len(args) >= 2:
        pfx = args[1]
        drv = pfx.split(':')[0] + ':' if ':' in pfx else None
        dst = f"{pfx.rstrip('/')}/{dst}"
        if drv:
            print(f"drv: {drv}")

    print(f"src: {src}\ndst: {dst}")

    # Fire core engine execution loop safely
    run_rclone_sync(src, dst, drv)

    # Print total operations completion times
    elapsed = time.time() - START_TIME
    print(f"\n{FGR}[ + ] Process complete. Execution time: {elapsed:.4f} seconds.{RESET}")


if __name__ == '__main__':
    main()
