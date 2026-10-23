#!/data/data/com.termux/files/usr/bin/python
import colorama, inspect, os, subprocess, sys, time

from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK; brd = Back.RED
bgr = Back.GREEN; byl = Back.YELLOW
bbl = Back.BLUE;  bmg = Back.MAGENTA
bcy = Back.CYAN;  bwh = Back.WHITE
fbk = Fore.BLACK; frd = Fore.RED
fgr = Fore.GREEN; fyl = Fore.YELLOW
fbl = Fore.BLUE;  fmg = Fore.MAGENTA
fcy = Fore.CYAN;  fwh = Fore.WHITE
frs = Fore.RESET
stdm  = Style.DIM;    stnr = Style.NORMAL
stbr  = Style.BRIGHT; stra = Style.RESET_ALL

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'

start_time = time.time()

desc = inspect.cleandoc(f'''
    alias:{fgr} csv-to-json{frs}
 function:{fyl} convert csv file to json file
''')
print(f'{desc}')
    
try:
 import osl
except Exception:
 print(f'{frd}unable to import osl{frs}')
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
    ''')
    print(f'{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
 
#insert_your_codes_here
import csv
import json
import sys

def usg():
    print(f"Usage: {sne} csv_file_path json_file_path")

try:
    csv_file_path = sys.argv[1]
except IndexError:
    usg()
    sys.exit()
try:
    json_file_path = sys.argv[2]
except IndexError:
    json_file_path = csv_file_path.rsplit('.', 1)[0] + '.json'

print(f'csv_File: {csv_file_path}')
print(f'json_File: {json_file_path}')

# Create a dictionary to store the data
data = {}

# Read csv file and add to data
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    snum = 0
    for row in csv_reader:
        if len(row) < 1:
            continue
        print(f'row: {row}\nrow[0]: {row[0]}')
        key = row[0]
        snum += 1
        data[key] = row

print(f'data:\n{data}')
# Write data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
    json_file.write('\n')


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
