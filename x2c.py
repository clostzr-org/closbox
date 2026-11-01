#!/data/data/com.termux/files/usr/bin/python

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

import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import time
start_time = time.time()

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
try:
   import openpyxl
except Exception:
   os.system(f'pip install openpyxl')
   import openpyxl
import csv
import os

def convert_xlsx_to_csv(xlsx_file, csv_file=None):
    """
    Converts an XLSX file to a CSV file without using pandas.

    Args:
        xlsx_file (str): The path to the XLSX file.
        csv_file (str, optional): The path to the output CSV file.
            If None, it will create a CSV file with the same name
            as the XLSX file but with the .csv extension.
    """
    try:
        # Determine the output CSV file name.
        if csv_file is None:
            base_name = os.path.splitext(xlsx_file)[0]
            csv_file = base_name + ".csv"

        # Open the XLSX workbook using openpyxl.
        workbook = openpyxl.load_workbook(xlsx_file)

        # Select the first sheet.
        sheet = workbook.active

        # Open the CSV file for writing.
        with open(csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Iterate over rows in the XLSX sheet and write them to the CSV file.
            for row in sheet.iter_rows():
                csv_writer.writerow([cell.value for cell in row])

        print(f"Successfully converted '{xlsx_file}' to '{csv_file}'")

    except FileNotFoundError:
        print(f"Error: File '{xlsx_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
   from tcget import tcget
   
   try:
      inpuT = tcget()
      print(f'input from tcget: {inpuT}')
   except Exception:
      try:
         inpuT = sys.argv[1]
      except Exception:
         inpuT = input(f'inpuT: ')
   print(f'inpuT: {inpuT}')
   
   if os.path.exists(inpuT):
      print(f'{fgr}inpuT exists{frs}')
      inpuT_ext = inpuT.rsplit('.', 1)[1]
      print(f'inpuT_ext: {inpuT_ext}')
      if not inpuT_ext == 'xlsx':
         print(f'{frd}inpuT file is not a xlsx{frs}')
         sys.exit()
   else:
      print(f'{frd}inpuT doesnt exists{frs}')
      sys.exit()
      
   xlsx_file = inpuT  # Replace with your XLSX file name
   convert_xlsx_to_csv(xlsx_file)


if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
