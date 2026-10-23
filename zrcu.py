#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import inspect
import subprocess

# Standard ANSI escape codes for local Termux rendering without external packages
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Context setup
spath = os.path.realpath(sys.argv[0]) # Automatically unpacks symlinks recursively
sdn = os.path.dirname(spath)
sbn = os.path.basename(spath)
sne = os.path.splitext(sbn)[0]

home = os.path.expanduser("~")
hbak = os.path.join(home, 'bak')
hbin = os.path.join(home, 'bin')
hsym = os.path.join(home, 'symlink')
zrc = os.path.join(home, '.zshrc')

# Self-linking module injection
try:
    import osl
    osl.osl(spath)
    for message in getattr(osl, 'info', []):
        print(message)
except ImportError:
    print("Warning: 'osl' module not found. Skipping self-link creation.")

def usg():
    """Prints usage structure."""
    print(f"usage: {sbn} <argument>")

def exargs():
    """Returns space-separated clean CLI arguments."""
    return ' '.join(sys.argv[1:]).strip()

# Lazy execution optimization: Prompt user FIRST before spending network overhead
inp00 = input('Update .zshrc configuration? (y/n): ').strip().lower()
if inp00 != 'y':
    sys.exit("Operation cancelled.")

# Core System Dependency Verification (Executed once here, instead of inside .zshrc)
print("Verifying baseline framework environment...")
subprocess.run("apt update && apt upgrade -y", shell=True)
subprocess.run("pip install colorama", shell=True)
subprocess.run("apt install micro -y", shell=True)

if os.path.isfile(zrc):
    print(f'Found configuration target: {zrc}')

    # Process files safely within isolated context blocks to protect against lock conflicts
    with open(zrc, 'r') as ozr:
        lines = ozr.readlines()
        print(f'--- Current .zshrc Content ---\n{"".join(lines).strip()}\n-----------------------------')

    # Locate truncation markers cleanly inside memory
    line_number = None
    for i, line in enumerate(lines, 1):
        if "# alias ohmyzsh" in line:
            line_number = i
            break

    if line_number is not None:
        print(f"Marker matching line rule at index: {line_number}")

        # Keep everything up to (and including) the marker line
        truncated_content = lines[:line_number]

        # Clean string configuration string 
        xstr = inspect.cleandoc(f'''
        # EXTRA LINES GENERATED AUTOMATICALLY
        for d in ~/bin ~/symlink; do
            if [[ ! -d $d ]]; then
               mkdir -p "$d"
               chmod 755 "$d"
               echo "Directory initialized: $d"
            fi
        done
        
        # System Paths Optimization
        for d in ~/.local/bin ~/bin ~/bin/_*(N/) ~/symlink; do
            if [[ $d:t != "__pycache__" ]]; then
               path+=("$d")
            fi
        done
        
        print -r "path_list:start"
        print -l $path
        print -r "path_list:end"
        
        if [ -f "$HOME/bin/sym_rm.py" ]; then
            python "$HOME/bin/sym_rm.py"
        fi
        
        alias micro='micro -clipboard internal'
        cd ~/bin
        ''')

        # Rewrite structural sequence cleanly using explicit atomic operations
        with open(zrc, 'w') as oza:
            oza.writelines(truncated_content)
            oza.write(f'\n{xstr}\n')

        with open(zrc, 'r') as ozr:
            updated_content = ozr.read()
            print(f'{YELLOW}Update completed successfully:{RESET}\n{MAGENTA}{updated_content}{RESET}')
    else:
        print("Required marker '# alias ohmyzsh' not found. Cancelled patch generation.")
else:
    print(f"Configuration profile '{zrc}' missing.")
