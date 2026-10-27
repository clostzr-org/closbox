#!/data/data/com.termux/files/usr/bin/python
import inspect
import os
import sys
import time
from pathlib import Path

# Start execution timer
start_time = time.perf_counter()

def get_ansi_colors():
    """Generates standard terminal color maps cleanly."""
    codes = {
        'black': '0', 'red': '1', 'green': '2', 'yellow': '3',
        'blue': '4', 'magenta': '5', 'cyan': '6', 'white': '7'
    }
    colors = {f'f{k[:2]}': f'\033[3{v}m' for k, v in codes.items()}
    colors.update({f'b{k[:2]}': f'\033[4{v}m' for k, v in codes.items()})
    colors['frs'] = '\033[0m'
    colors['brs'] = '\033[0m'
    return colors

# Initialize colors as global variables dynamically
globals().update(get_ansi_colors())

# Environment paths setup using Pathlibs
HOME = Path(os.environ.get('HOME', '/data/data/com.termux/files/home'))
HBAK = HOME / 'bak'
HBIN = HOME / 'bin'
HSYMLINK = HOME / 'symlink'

# Script properties
SCRIPT_PATH = Path(sys.argv[0]).resolve()
SBN = SCRIPT_PATH.name

# Header Description Output
desc = inspect.cleandoc(f'''
{fgr}alias    {frs}: symlinks remover{frs}
{fye}function {frs}: remove all symlinks with missing sources{frs}
''')
print(desc)

def osl(*args):
    """Creates a symbolic link for the current running script inside the symlink directory."""
    source_path = SCRIPT_PATH
    
    if args:
        chosen = Path(args[0])
        if chosen.is_file():
            source_path = chosen

    if source_path.suffix != '.py':
        return 'current file is not a .py file'

    HSYMLINK.mkdir(parents=True, exist_ok=True)
    link_path = HSYMLINK / source_path.stem

    if link_path.exists() and not link_path.is_symlink():
        link_path.unlink()

    bnsym = link_path.name
    try:
        if link_path.is_symlink():
            link_path.unlink()
        link_path.symlink_to(source_path)
        print(f'{fye}{bnsym}{frs} : file exists / created successfully')
    except Exception:
        print(f'{fye}{bnsym}{frs} : creation failed or aborted')

# Run symlink registration
osl()

def remove_symlinks_with_missing_sources(directory_path):
    """Scan directory, purge broken links, and print results as comma-separated text."""
    target_dir = Path(directory_path)
    if not target_dir.is_dir():
        return

    print(f'{fye}Symlink directory{frs} : {target_dir}')
    
    removed_links = []
    retained_links = []

    # Use os.walk via modern Pathlib rglob for rapid recursive lookup
    for item in target_dir.rglob('*'):
        if item.is_symlink():
            try:
                # check if the symlink target point to an active file/dir
                if not item.exists():
                    removed_links.append(item.name)
                    item.unlink()
                else:
                    retained_links.append(item.name)
            except FileNotFoundError:
                removed_links.append(item.name)

    if removed_links:
        print(f"{fre}Removed symlinks{frs} : {', '.join(removed_links)}")
    if retained_links:
        print(f"{fgr}Retained symlinks{frs} : {', '.join(retained_links)}")

# Execute cleanup across folders
directories_to_clean = [HBIN, HSYMLINK]
directories_to_clean = [HSYMLINK]
for folder in directories_to_clean:
    remove_symlinks_with_missing_sources(folder)

if __name__ == '__main__':
    elapsed_time = time.perf_counter() - start_time
    print(f"\nElapsed time: {elapsed_time:.4f} seconds")
