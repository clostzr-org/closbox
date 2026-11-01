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
   import xlsxwriter
except Exception:
   os.system(f'pip install xlsxwriter')
   import xlsxwriter
import datetime

import xlsxwriter
import datetime
import csv
from io import StringIO

# CSV input content
csv_content = """
00,Admin,2025-08-31-Sunday,10:00:47,checkIn,10:01:50,breakIn,12:33:36,overtimeOut,18:08:31,overtimeOut,18:42:04,checkIn,2025-09-01-Monday,01:44:25,overtimeIn,04:58:49,checkIn,04:58:55,checkIn,05:33:49,checkIn,07:57:55,breakIn,08:04:14,checkIn,20:04:02,checkIn,21:06:33,checkIn
01,Entin Sukaesih,2025-08-31-Sunday,12:34:53,checkIn,21:48:02,checkOut,2025-09-01-Monday,11:31:48,checkIn,21:02:00,checkOut,2025-09-02-Tuesday,11:33:25,checkOut,22:23:19,overtimeOut,2025-09-03-Wednesday,11:49:29,checkIn
"""

# Create a new Excel file.
workbook = xlsxwriter.Workbook('/sdcard/dates.xlsx')
worksheet = workbook.add_worksheet()

# Define the headers.
headers = ['jobno', 'name']

# Define the start date and the number of dates.
start_date = datetime.date(2025, 8, 31)
num_dates = 7

# Generate the date headers.
date_headers = [(start_date + datetime.timedelta(days=i)).strftime('%Y/%m/%d/%A') for i in range(num_dates)]
headers.extend(date_headers)

# Write the headers to the worksheet.
for col_num, header in enumerate(headers):
    worksheet.write(0, col_num, header)
    worksheet.set_column(col_num, col_num, len(header) + 2)

# Read the CSV data.
csv_file = StringIO(csv_content)
csv_reader = csv.reader(csv_file)

# Write the data to the worksheet.
row_num = 1
for row in csv_reader:
    if row:  # Check if the row is not empty
        jobno = row[0]
        name = row[1]
        worksheet.write(row_num, 0, jobno)
        worksheet.write(row_num, 1, name)
        col_num = 2
        i = 2
        while i < len(row):
            date_str = row[i]
            try:
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d-%A").date()
                header_date_strs = [datetime.datetime.strptime(h, "%Y/%m/%d/%A").date() for h in date_headers]
                if date_obj in header_date_strs:
                    date_index = header_date_strs.index(date_obj)
                    time_str = row[i+1]
                    status_str = row[i+2] if i+2 < len(row) else ''
                    worksheet.write(row_num, date_index + 2, time_str + ' ' + status_str)
                    i += 3
                else:
                    i += 1
            except ValueError:
                i += 1
        row_num += 1
    else:
        print("Skipping empty row")

# Close the workbook.
workbook.close()




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
