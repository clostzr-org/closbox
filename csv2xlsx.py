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
import os
import csv
import xlsxwriter

def convert_files_to_excel(input_directory):
    # List all files in the directory
    files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    for file in files:
        file_path = os.path.join(input_directory, file)
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(input_directory, f"{base_name}.xlsx")  # Output in the same directory

        # Create a new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(output_path)
        worksheet = workbook.add_worksheet(base_name)

        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row_num, row_data in enumerate(reader):
                    for col_num, cell_data in enumerate(row_data):
                        worksheet.write(row_num, col_num, cell_data)
            print(f"Converted {file} to {output_path}")
        except Exception as e:
            print(f"Error reading or writing {file}: {e}")

        workbook.close()

    print("All files processed.")

# Usage example:
# input_dir = "path/to/your/input_files"
# convert_files_to_excel(input_dir)


from tcget import tcget

# Check if 'tcget' command exists
import shutil
def command_exists(cmd):
    return shutil.which(cmd) is not None

# Function to get input path
def get_input_path():
    # 1. Check if 'tcget' exists
    if command_exists('tcget'):
        try:
            path = subprocess.run(['tcget'], capture_output=True, check=True, text=True).stdout.strip()
            if os.path.exists(path):
                return path
        except:
            pass
    # 2. Use argument if provided
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            return arg_path
    # 3. Prompt user
    user_input = input("Enter a file or directory path: ").strip()
    if os.path.exists(user_input):
        return user_input
    else:
        print("Path does not exist.")
        sys.exit()
        
# Main logic
def main():
    path = get_input_path()

    if os.path.isfile(path):
        if path.lower().endswith('.txt'):
            convert_files_to_excel(path)
        else:
            print("The file is not a PDF.")
    elif os.path.isdir(path):
        # Recursively process all files in directory
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    full_path = os.path.join(root, file)
                    convert_files_to_excel(full_path)
    else:
        print("Invalid path.")
        sys.exit()

if __name__ == "__main__":
    main()

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
