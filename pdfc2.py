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
import sys
import shutil
import subprocess
import time

# Timing start
START_TIME = time.time()

# Setup paths globally
HOME = '/data/data/com.termux/files/home'
HBIN = os.path.join(HOME, 'bin')

if HBIN not in sys.path:
    sys.path.append(HBIN)

# Safe imports for custom modules
try:
    from tcget import tcget
except ImportError:
    tcget = None

try:
    from ansicolors import *  # Assumed used for terminal styling
except ImportError:
    pass

try:
    import osl
except ImportError:
    osl = None


def check_dependencies():
    """Ensures ghostscript is installed once before processing files."""
    if shutil.which('gs') is not None:
        return

    print("Ghostscript not found. Installing dependencies...")
    try:
        # Combined system update and installation quietly
        subprocess.run(['pkg', 'install', 'ghostscript', '-y'], check=True, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'ghostscript'], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"[-] Dependency installation failed: {e}")
        sys.exit(1)


def get_input_path():
    """Resolves input path via tcget module, CLI args, or user prompt."""
    # 1. Try native python module tcget if available
    if tcget:
        try:
            path = tcget()
            if path and os.path.exists(path.strip()):
                return path.strip()
        except Exception:
            pass

    # 2. Try running tcget as a terminal command fallback
    if shutil.which('tcget'):
        try:
            res = subprocess.run(['tcget'], capture_output=True, text=True, check=True)
            path = res.stdout.strip()
            if os.path.exists(path):
                return path
        except subprocess.SubprocessError:
            pass

    # 3. Use CLI argument if provided
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            return arg_path

    # 4. Fallback to interactive user prompt
    user_input = input("Enter a file or directory path: ").strip()
    if os.path.exists(user_input):
        return user_input
    
    print("[-] Path does not exist.")
    sys.exit(1)


def process_pdf(file_path):
    """Compresses a single PDF file efficiently using Ghostscript."""
    print(f"[*] Processing file: {file_path}")
    
    # Generate output path robustly using os.path
    base, _ = os.path.splitext(file_path)
    output_pdf = f"{base}.compressed.pdf"

    cmd = [
        'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dBATCH',
        f'-sOutputFile={output_pdf}', file_path
    ]
    
    try:
        # Run quietly without flooding the Termux screen with GS logs
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"[+] Compressed successfully: {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error processing {file_path}: {e.stderr.decode().strip()}")


def main():
    # Execute metadata processing if osl module exists
    if osl:
        try:
            spath = os.readlink(sys.argv[0]) if os.path.islink(sys.argv[0]) else sys.argv[0]
            osl.osl(spath)
            for message in getattr(osl, 'info', []):
                print(f"{message}")
        except Exception:
            pass

    path = get_input_path()
    
    # Enforce dependency check only if we actually have valid inputs to process
    check_dependencies()

    if os.path.isfile(path):
        if path.lower().endswith('.pdf'):
            process_pdf(path)
        else:
            print("[-] The target file is not a PDF.")
    elif os.path.isdir(path):
        # Optimized traversal
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.pdf') and not file.endswith('.compressed.pdf'):
                    process_pdf(os.path.join(root, file))
    else:
        print("[-] Invalid path sequence.")
        sys.exit(1)

    print(f"\n[+] Done! Execution time: {time.time() - START_TIME:.2f} seconds.")


if __name__ == "__main__":
    main()
