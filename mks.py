#!/usr/bin/env python3
import time
import os
import sys
import subprocess
import shutil
import argparse

start_time = time.time()

# --- UI Helpers ---
C = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "cyan": "\033[36m",
    "yellow": "\033[33m",
    "red": "\033[31m",
}

def print_box(title, content):
    width = 50
    print(f"{C['cyan']}╔{'═' * (width-2)}╗{C['reset']}")
    print(f"{C['cyan']}║ {C['bold']}{title.center(width-4)}{C['reset']}{C['cyan']} ║{C['reset']}")
    print(f"{C['cyan']}╠{'═' * (width-2)}╣{C['reset']}")
    for line in content.split('\n'):
        print(f"{C['cyan']}║ {C['reset']}{line.ljust(width-4)}{C['cyan']} ║{C['reset']}")
    print(f"{C['cyan']}╚{'═' * (width-2)}╝{C['reset']}")

# --- Configuration ---
home = os.path.expanduser('~')
hcwd = os.path.join(home, os.path.basename(os.path.dirname(os.path.abspath(__file__))))

if hcwd not in sys.path:
    sys.path.append(hcwd)

# --- Core Logic ---
def ensure_micro():
    """Ensures micro editor is installed."""
    if shutil.which('micro'):
        return 'micro'
    
    print(f"{C['yellow']}Micro editor not found. Attempting auto-install...{C['reset']}")
    try:
        # Official micro installation script for Unix
        # Using -y logic via non-interactive curl/sh
        cmd = "curl https://getmic.ro | bash"
        subprocess.run(cmd, shell=True, check=True)
        if shutil.which('micro'):
            print(f"{C['green']}Micro installed successfully!{C['reset']}")
            return 'micro'
    except Exception as e:
        print(f"{C['red']}Auto-install failed: {e}{C['reset']}")
    
    return os.environ.get('EDITOR', 'nano')

header_py = f"""#!/usr/bin/env python3
import time
import os, sys

start_time = time.time()
home  = os.path.expanduser('~')
hcwd  = os.path.join(home, os.path.basename(os.path.dirname(__file__)))
if hcwd not in sys.path:
    sys.path.append(hcwd)

spath = os.readlink(sys.argv[0]) if os.path.islink(sys.argv[0]) else os.path.abspath(sys.argv[0])
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
verbose = False

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

def usg():
    import inspect
    usg_text = inspect.cleandoc(f'''
    alias: 
 function: 
    usage: {{sbn}} [argument]
    ''')
    print(usg_text)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        usg()
        sys.exit()

    # insert_your_codes_here

    print(f"Elapsed time: {{time.time() - start_time}} seconds")
"""

def hdsh(src_file, ext):
    return f"""#!/usr/bin/env bash

bnz=$(basename $0)
if [[ "${{bnz##*.}}" == "{ext.strip('.')}" ]]; then
    echo -e "source-file : {src_file}"
fi

echo -e "usage: $(basename $0) [command]"
"""

def create_script(bname, ext):
    clean_base = bname.strip().replace(' ', '_')
    src_file = os.path.join(hcwd, f"{clean_base}{ext}")

    match ext:
        case '.py':
            header, lang = header_py, 'Python'
        case '.sh':
            header, lang = hdsh(src_file, ext), 'Shell'
        case '.txt':
            header, lang = '', 'Text'
        case _:
            header, lang = '', 'Unknown'

    os.makedirs(hcwd, exist_ok=True)

    if not os.path.isfile(src_file):
        with open(src_file, 'w') as f:
            f.write(header + '\n')
    
    os.chmod(src_file, 0o755)

    print_box("Script Created", f"Language: {lang}\nPath: {src_file}")
    
    editor = ensure_micro()
    subprocess.run([editor, src_file])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Make a script with environment presets", add_help=False)
    parser.add_argument('params', nargs='*', help="Filename or extension")
    parser.add_argument('-h', '--help', action='store_true')
    
    args = parser.parse_args()

    if args.help:
        print_box("Usage", f"mks.py [-py|-sh] [filename]\nExample: mks.py .py myscript")
        sys.exit()

    if not args.params:
        print(f"{C['red']}Error: No filename or extension provided.{C['reset']}")
        sys.exit(1)

    # Resolve extension and basename
    ext = '.txt'
    bname = None

    for p in args.params:
        if p.startswith('.'):
            ext = p.lower()
        else:
            bname = p

    if not bname:
        print(f"{C['red']}Error: Basename is required.{C['reset']}")
        sys.exit(1)

    if '.' in bname:
        bname, parsed_ext = os.path.splitext(bname)
        ext = parsed_ext if parsed_ext.startswith('.') else f".{parsed_ext}"

    print(f"{C['blue']}Proposed file: {C['bold']}{bname}{ext}{C['reset']}")
    cnfrm = input(f"Create this file? (y/n): ").strip().lower()
    
    if cnfrm == 'y':
        create_script(bname, ext)
    
    print(f"\n{C['green']}Total Execution Time: {time.time() - start_time:.4f}s{C['reset']}")
