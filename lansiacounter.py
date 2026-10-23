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
import re

def count_lines_starting_with_numbers(file_path):
    """
    Counts the number of lines in a file that start with a digit.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The count of lines starting with numbers.
    """
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Use regex to check if the line starts with a digit
                if re.match(r'^\d', line):
                    count += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return -1  # Indicate an error
    return count

# Example usage:
# Assuming your file is named 'data.txt' and is in the same directory as the script.
file_name = sys.argv[1]
number_of_lines = count_lines_starting_with_numbers(file_name)

if number_of_lines != -1:
    print(f"The number of lines starting with numbers is: {number_of_lines}")
    
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
