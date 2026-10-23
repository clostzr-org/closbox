#!/data/data/com.termux/files/usr/bin/python
import time
import os
import sys
import csv
import shutil
import subprocess
import xlsxwriter

try:
     import openpyxl  # For reading .xlsx files
except Exception:
     os.system('pip install openpyxl')
     import openpyxl  # For reading .xlsx files

start_time = time.time()

# Your existing setup code...
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if  not hbin in sys.path:
    sys.path.append(hbin)
from ansicolors import *

spath = sys.argv[0]
if os.path.islink(spath):
    spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'

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

# Function to get input path
def get_input_path():
    def command_exists(cmd):
        return shutil.which(cmd) is not None

    if command_exists('tcget'):
        try:
            result = subprocess.run(['tcget'], capture_output=True, check=True, text=True)
            path = result.stdout.strip()
            if os.path.exists(path):
                return path
        except:
            pass
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            return arg_path
    user_input = input("Enter a file or directory path: ").strip()
    if os.path.exists(user_input):
        return user_input
    else:
        print("Path does not exist.")
        sys.exit()

# Function to convert .xlsx to multiple CSVs
def excel_to_csvs(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path)
    dir_name = os.path.dirname(xlsx_path)
    for sheet in wb.worksheets:
        sheet_name = sheet.title
        csv_filename = os.path.join(dir_name, f"{sheet_name}.csv")
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in sheet.iter_rows(values_only=True):
                writer.writerow([cell if cell is not None else '' for cell in row])
        print(f"Exported sheet '{sheet_name}' to {csv_filename}")

# Inside your main() function, before processing files, add:
def singlesheet():
    # Check for special arguments '-x2c' and '-sngs'
    if len(sys.argv) > 1:
        if sys.argv[1] == '-x2c':
            # existing '-x2c' handling...
            # (keep your existing code here)
            pass
        elif sys.argv[1] == '-sngs':
            # Single sheet mode
            if len(sys.argv) < 3:
                print("Please provide the file or directory path after '-sngs'")
                sys.exit()
            sngs_path = sys.argv[2]
            #sngs_path = get_input_path()
            if not os.path.exists(sngs_path):
                print("Invalid path.")
                sys.exit()
            # Determine output filename
            if os.path.isfile(sngs_path):
                base_name = os.path.splitext(os.path.basename(sngs_path))[0]
                output_xlsx = os.path.join(os.path.dirname(sngs_path), f"{base_name}_single_sheet.xlsx")
            elif os.path.isdir(sngs_path):
                dir_name = os.path.basename(os.path.normpath(sngs_path))
                output_xlsx = os.path.join(os.path.dirname(sngs_path), f"{dir_name}/{dir_name}_single_sheet.xlsx")
            else:
                print("Invalid path.")
                sys.exit()

            # Create workbook and add one sheet
            workbook = xlsxwriter.Workbook(output_xlsx)
            sheetname = "Data"
            worksheet = workbook.add_worksheet(f'{sheetname}')
            row_idx = 0

            # Gather all relevant files
            files_to_process = []
            if os.path.isfile(sngs_path):
                ext = os.path.splitext(sngs_path)[1].lower()
                if ext in ['.txt', '.csv']:
                    files_to_process.append(sngs_path)
            elif os.path.isdir(sngs_path):
                for root, dirs, files in os.walk(sngs_path):
                    for file in files:
                        ext = os.path.splitext(file)[1].lower()
                        if ext in ['.txt', '.csv']:
                            files_to_process.append(os.path.join(root, file))

            # Process each file
            for file_path in files_to_process:
                with open(file_path, 'r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        for col_num, cell in enumerate(row):
                            worksheet.write(row_idx, col_num, cell)
                        row_idx += 1
                print(f"Added {file_path} to single sheet.")

            workbook.close()
            print(f"All files combined into {output_xlsx}")
            sys.exit()
        else:
            # existing code...
            pass

    # Rest of your existing main() code...
    
# Main processing
def main():
    # Check for special argument '-x2c'
    # Inside your main() function, replace the existing '-x2c' handling with:

    if len(sys.argv) > 1 and sys.argv[1] == '-x2c':
        # Expect a single path (file or directory) after '-x2c'
        if len(sys.argv) < 3:
            print("Please provide the .xlsx file or directory path after '-x2c'")
            sys.exit()
        xlsx_input_path = sys.argv[2]
        if not os.path.exists(xlsx_input_path):
            print("Invalid path.")
            sys.exit()
        if os.path.isfile(xlsx_input_path):
            # Single file conversion
            if not xlsx_input_path.lower().endswith('.xlsx'):
                print("Provided file is not an .xlsx file.")
                sys.exit()
            excel_to_csvs(xlsx_input_path)
        elif os.path.isdir(xlsx_input_path):
            # Directory: process all .xlsx files inside
            for root, dirs, files in os.walk(xlsx_input_path):
                for file in files:
                    if file.lower().endswith('.xlsx'):
                        full_path = os.path.join(root, file)
                        excel_to_csvs(full_path)
        else:
            print("Invalid path.")
            sys.exit()
        sys.exit()
        
    elif sys.argv[1] == '-sngs':
         singlesheet()
    
    # Otherwise, proceed with original logic
    path = get_input_path()

    # Determine the Excel file name based on the first input file
    if os.path.isfile(path):
        base_name = os.path.splitext(os.path.basename(path))[0]
        excel_path = os.path.join(os.path.dirname(path), f"{base_name}.xlsx")
    elif os.path.isdir(path):
        # If directory, set excel file name based on directory name
        if os.path.isdir(path):
            dir_name = os.path.basename(os.path.normpath(path))
            excel_path = os.path.join(os.path.dirname(path), f"{dir_name}/{dir_name}.xlsx")
        else:
            # existing logic for files
            first_file = None
            for root, dirs, files in os.walk(path):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in ['.txt', '.csv']:
                        first_file = os.path.join(root, file)
                        break
                if first_file:
                    break
            if first_file:
                base_name = os.path.splitext(os.path.basename(first_file))[0]
                excel_path = os.path.join(os.path.dirname(first_file), f"{base_name}.xlsx")
            else:
                excel_path = os.path.join(os.path.dirname(path), "combined_data.xlsx")
                print("No .txt or .csv files found, using default name 'combined_data.xlsx'")
    else:
        print("Invalid path.")
        sys.exit()

    # Create a single workbook for all sheets
    workbook = xlsxwriter.Workbook(excel_path)

    sheet_count = 0  # To generate unique sheet names
    
    def convert_files_to_excel(file_path):
        nonlocal sheet_count
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        if  len(base_name) > 30:
            try:
                bname = ''.join([word[:1] for word in base_name.split('_')])
            except Exception:
                bname = base_name[13:]
        else:
            bname = base_name
        sheet_name = f"{sheet_count+1}-{bname}"
        sheet_count += 1
        worksheet = workbook.add_worksheet(sheet_name)
    
        max_col_widths = {}  # Track max width per column for current file
    
        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row_num, row_data in enumerate(reader):
                    for col_num, cell_data in enumerate(row_data):
                        worksheet.write(row_num, col_num, cell_data)
                        # Update max width for this column
                        cell_length = len(str(cell_data))
                        if col_num not in max_col_widths or cell_length > max_col_widths[col_num]:
                            max_col_widths[col_num] = cell_length
            print(f"Added {fyl}{file_path}{frs} to sheet {fgr}{sheet_name}{frs}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

        # Set column widths based on max content length for this sheet
        for col_num, width in max_col_widths.items():
            worksheet.set_column(col_num, col_num, width + 4)

    if os.path.isfile(path):
        ext = os.path.splitext(path)[1].lower()
        if ext in ['.txt', '.csv']:
            convert_files_to_excel(path)
        else:
            print("The file is not a .txt or .csv file.")
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in ['.txt', '.csv']:
                    full_path = os.path.join(root, file)
                    convert_files_to_excel(full_path)
    else:
        print("Invalid path.")
        sys.exit()

    # Save the overall workbook after processing all files
    workbook.close()
    print(f"All files have been combined into {excel_path}")

if __name__ == "__main__":
    try:
        if sys.argv[1] == '-h':
            usg()
            sys.exit()
    except:
        pass
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")