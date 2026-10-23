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
    usage: {frs} {sbn} [file_or_directory]
    ''')
    print(f'{usg}')

#insert_your_codes_here
import re

def count_lines_starting_with_numbers_in_file(file_path):
    """
    Counts the number of lines in a file that start with a digit.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The count of lines starting with numbers, or -1 if the file is not found.
    """
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if re.match(r'^\d', line):
                    count += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return -1
    except IsADirectoryError:
        # This case should ideally be handled before calling this function for directories
        return 0 # A directory itself doesn't have lines starting with numbers
    except Exception as e:
        print(f"An error occurred while processing '{file_path}': {e}")
        return -1
    return count

def count_lines_recursively(directory_path):
    """
    Recursively counts lines starting with numbers in all files within a directory.

    Args:
        directory_path (str): The path to the input directory.

    Returns:
        int: The total count of lines starting with numbers across all files.
    """
    total_count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            count = count_lines_starting_with_numbers_in_file(file_path)
            if count != -1:
                total_count += count
    return total_count

if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            usg()
            sys.exit()
    except IndexError:
        # No arguments provided, handle as needed (e.g., show usage or default behavior)
        print("No arguments provided. Please provide a file path or directory path.")
        usg()
        sys.exit(1)

    target_path = sys.argv[1]
    total_lines_starting_with_numbers = 0

    if os.path.isfile(target_path):
        total_lines_starting_with_numbers = count_lines_starting_with_numbers_in_file(target_path)
        if total_lines_starting_with_numbers != -1:
            print(f"The number of lines starting with numbers in '{target_path}' is: {total_lines_starting_with_numbers}")
    elif os.path.isdir(target_path):
        print(f"Scanning directory: {target_path}")
        total_lines_starting_with_numbers = count_lines_recursively(target_path)
        print(f"The total number of lines starting with numbers in '{target_path}' and its subdirectories is: {total_lines_starting_with_numbers}")
    else:
        print(f"Error: '{target_path}' is not a valid file or directory.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")