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
import csv
import xlsxwriter
from io import StringIO

csv_data = """Periode,11-15 Agustus 2025
Deskripsi,Pengeluaran Biaya Operasional (Bensin, Gas, Listrik, dll)
No,Uraian,Jml,Satuan,Harga Satuan,Total/5 hari
1,Sabun Cuci Alat,20,Kompan,Rp. 73,000,Rp. 1,460,000
2,Sponge Cuci Alat,15,PCS,Rp. 5,000,Rp. 75,000
3,Tissue,10,Pack,Rp. 23,000,Rp. 230,000
4,Sabun Pel,10,Kompan,Rp. 49,000,Rp. 490,000
5,pengharum Ruangan,5,PCS,Rp. 23,000,Rp. 115,000
6,Trashbag,25,Pack,Rp. 38,000,Rp. 950,000
7,Air Minum,25,Galon,Rp. 21,000,Rp. 525,000
8,bensin,15,mobil,Rp. 150,000,Rp. 2,250,000
9,Listrik,5,hari,Rp. 250,000,Rp. 1,250,000
10,Pengelolaan Sampah,5,Hari,Rp. 50,000,Rp. 250,000
11,Plastik Buah,11,Pack,Rp. 30,000,Rp. 330,000
12,plastik 5 Kg,10,Pack,Rp. 48,000,Rp. 480,000
13,Plastik 1/4 Kg,2,Pack,Rp. 8,000,Rp. 16,000
14,Penghilang bau limbah,2,Pcs,Rp. 100,000,Rp. 200,000
15,Map Bindex,2,Pcs,Rp. 27,000,Rp. 54,000
16,paper Clip hitam sedang,2,Box,Rp. 10,000,Rp. 20,000
17,Sticky Notes,2,Pcs,Rp. 10,000,Rp. 20,000
18,pensil,1,Pack,Rp. 15,000,Rp. 15,000
19,Steples besar,1,PCS,Rp. 70,000,Rp. 70,000
20,Kertas HVS,2,RIM,Rp. 40,000,Rp. 80,000
21,Handgloves Plastik,25,Pca,Rp. 8,000,Rp. 200,000
22,Sarung tangan Karet,10,Box,Rp. 55,000,Rp. 550,000
23,P3K Obat-obatan,1,Paket,-,Rp. 600,000
24,Mini whiteborad,3,pcs,Rp. 37,000,Rp. 111,000
,Total/5 Hari,,,,Rp. 10,341,000"""

try:
   inpuT = sys.argv[1]
except Exception:
   inpuT = input(f'input csv: ')
   
if os.path.isfile(inpuT):
   outfile = inpuT.rsplit('.', 1)[0] + f'.xlsx'
   with open(inpuT, 'r') as ifile:
        inputs = ifile.read()
        csv_data = inputs

# Use StringIO to treat the string as a file
csv_file = StringIO(csv_data)

# Read the CSV data using the csv module
reader = csv.reader(csv_file)

# Prepare the data
data = list(reader)

# Clean the data: remove the first two rows and the last row
data = data[2:-1]

# Function to clean currency strings
def clean_currency(value):
    return value.replace('Rp. ', '').replace(',', '')

# Modify the data to remove currency formatting
for row in data:
    if len(row) > 5:  # Make sure the row has enough columns
        row[4] = clean_currency(row[4])
        row[5] = clean_currency(row[5])

# Create an Excel file and add a worksheet
workbook = xlsxwriter.Workbook(outfile)
worksheet = workbook.add_worksheet()

# Write the data to the Excel file
for row_num, row_data in enumerate(data):
    for col_num, cell_data in enumerate(row_data):
        worksheet.write(row_num, col_num, cell_data)

# Close the workbook
workbook.close()

print(f"Data saved to {outfile}")

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
