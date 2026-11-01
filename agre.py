#!/data/data/com.termux/files/usr/bin/python
import inspect, os, subprocess, sys, time

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=False)
    COLORAMA = True
except ImportError:
    COLORAMA = False

if COLORAMA:
    # Foreground shortcuts
    fbk, frd, fgr, fyl = Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW
    fbl, fmg, fcy, fwh = Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
    frs = Fore.RESET

    # Background shortcuts (names now correctly match their colors)
    bbk, brd, bgr, byl = Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW
    bbl, bmg, bcy, bwh = Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE
    brs = Back.RESET

    rst = Style.RESET_ALL
    bold = Style.BRIGHT
else:
    def _ansi_fg(n): return f'\033[{n}m'
    def _ansi_bg(n): return f'\033[{n}m'

    fbk, frd, fgr, fyl = _ansi_fg(30), _ansi_fg(31), _ansi_fg(32), _ansi_fg(33)
    fbl, fmg, fcy, fwh = _ansi_fg(34), _ansi_fg(35), _ansi_fg(36), _ansi_fg(37)
    frs = _ansi_fg(39)

    bbk, brd, bgr, byl = _ansi_bg(40), _ansi_bg(41), _ansi_bg(42), _ansi_bg(43)
    bbl, bmg, bcy, bwh = _ansi_bg(44), _ansi_bg(45), _ansi_bg(46), _ansi_bg(47)
    brs = _ansi_bg(49)

    rst = '\033[0m'
    bold = '\033[1m'

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'

start_time = time.time()

desc = inspect.cleandoc(f'''
    alias:{fgr} ag using re{rst}
 function:{fyl} search for a string in current dir.{rst}
''')
print(f'{desc}')

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    info = []
    home = os.environ['HOME']
    symdir = f'{home}/symlink'
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    if not source_path.endswith('.py'):
        return
    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = f'{symdir}/{lpbn}'
    if not os.path.isdir(symdir):
        os.mkdir(symdir)
    if os.path.exists(link_path):
        if not os.path.islink(link_path):
            os.remove(link_path)
    try:
       os.symlink(source_path, link_path)
    except Exception:
       print(f'symlink creation returns error')
    if os.path.islink(link_path):
        info.append(f"Symbolic link '{link_path}' exists.")
    else:
        info.append(f"Failed to create symbolic link '{link_path}'.")

osl()

import os
import re

def find_in_files_colored(pattern, directory):
    """Searches for the given pattern in files within the specified directory
    and outputs results with the matching strings highlighted in red.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
               ext = filename.rsplit('.', 1)[1]
            except Exception:
               ext = 'None'
            match ext:
                  case ('html' | 'pyc' | 'None'):
                       continue
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                    for line_num, line in enumerate(file, 1):
                        if match := re.search(pattern, line):
                            # Highlight the matched string in bold red
                            colored_line = line.replace(
                                match.group(0),
                                f"{bold}{frd}{match.group(0)}{rst}",
                            )
                            print(
                                f"{fgr}{filepath}{rst}:\n{fyl}{line_num}{rst}: {colored_line.strip()}"
                            )
            except (UnicodeDecodeError, PermissionError, OSError):
                continue

# Example Usage
import sys
search_pattern = sys.argv[1]
search_directory = "."  # Current directory
find_in_files_colored(search_pattern, search_directory)
