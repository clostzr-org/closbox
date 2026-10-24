#!/usr/bin/env python3

# --- AUTO-INSTALL DEPENDENCIES ---
import subprocess
import sys

def install_package(package):
    print(f"[*] Dependency '{package}' not found. Installing automatically...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[+] Successfully installed {package}\n")
    except Exception as e:
        print(f"[-] Failed to auto-install {package}. Please install it manually via: pip install {package}")
        sys.exit(1)

# Check and install xlsxwriter if missing
try:
    import xlsxwriter
except ImportError:
    install_package("xlsxwriter")

# Enable ANSI escape sequences on Windows 10/11 terminals
import os
if os.name == 'nt':
    os.system('')

def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
        'black':'\033[30m', 'red'    :'\033[31m',
        'green':'\033[32m', 'yellow' :'\033[33m',
        'blue' :'\033[34m', 'magenta':'\033[35m',
        'cyan' :'\033[36m', 'white'  :'\033[37m',
        'reset':'\033[0m'
    }
    code = ''
    if reset:
       code = color_codes['reset']
    elif fg:
       code = color_codes.get(fg, '')
    elif bg:
       code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'
    return code

# Define color shortcuts for convenience
fbk = ansi_color(fg='black')
frd = ansi_color(fg='red')
fgr = ansi_color(fg='green')
fyl = ansi_color(fg='yellow')
fbl = ansi_color(fg='blue')
fmg = ansi_color(fg='magenta')
fcy = ansi_color(fg='cyan')
fwh = ansi_color(fg='white')
frs = ansi_color(fg='reset')

bbk = ansi_color(bg='black')
brd = ansi_color(bg='red')
bgr = ansi_color(bg='green')
bcy = ansi_color(bg='yellow')
byl = ansi_color(bg='blue')
bbl = ansi_color(bg='magenta')
bmg = ansi_color(bg='cyan')
bwh = ansi_color(bg='white')
brs = ansi_color(bg='reset')

import os
sdn   = os.path.dirname(os.path.abspath(sys.argv[0]))
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = os.path.join(sdn, sne)

# Cross-platform home directory configuration
home  = os.path.expanduser("~")
hbak  = os.path.join(home, 'bak')
hbin  = os.path.join(home, 'bin')
verbose = False

import time
start_time = time.time()

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory (skipped on Windows if permissions fail)."""
    global info
    info = []
    symdir = os.path.join(home, 'symlink')
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    if not source_path.endswith('.py'):
       return
    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = os.path.join(symdir, lpbn)
    
    if not os.path.isdir(symdir):
       try:
           os.mkdir(symdir)
       except Exception:
           return
    if os.path.exists(link_path):
       if not os.path.islink(link_path):
            try:
                os.remove(link_path)
            except Exception:
                pass
    try:
       os.symlink(source_path, link_path)
    except Exception:
       pass
       
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' exists.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()

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
def create_excel_file(filename, sheetname="Sheet1"):
    """
    Creates a new Excel file (.xlsx) with a single sheet.

    Args:
        filename (str): The name of the Excel file to create (e.g., "my_data.xlsx").
        sheetname (str, optional): The name of the sheet in the Excel file. Defaults to "Sheet1".
    """
    try:
        # Create a new Excel workbook.
        workbook = xlsxwriter.Workbook(filename)

        # Add a worksheet to the workbook.
        worksheet = workbook.add_worksheet(sheetname)

        # Close the workbook to save the Excel file.
        workbook.close()

        print(f"Excel file '{filename}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
   try:
     if len(sys.argv) > 1 and sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass

   filename = input("Enter the desired filename for the Excel file (e.g., data.xlsx): ")
   sheetname = input("Enter the desired sheet name (optional, press Enter for default 'Sheet1'): ") or "Sheet1"
   create_excel_file(filename, sheetname)

   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time:.4f} seconds")