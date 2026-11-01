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
import pytesseract
from PIL import Image

import os
import subprocess
import sys

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
        
# Set your directory path here
directory = get_input_path()

# Get directory name for output filename
dir_name = os.path.basename(os.path.normpath(directory))
output_dir = os.path.abspath(directory)
output_csv = f"{output_dir}/{dir_name}.csv"

# Supported image extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')

# Collect all image files
images = [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]

# Prepare data list
# Each item: {'filename': ..., 'text': ...}
data = []

for img_name in images:
    img_path = os.path.join(directory, img_name)
    try:
        with Image.open(img_path) as img:
            print(f'now processing: {img_name}')
            text = pytesseract.image_to_string(img)
            # Split into lines
            lines = text.strip().splitlines()
            for line in lines:
                print(f'current line: {line}')
                data.append({'filename': img_name, 'text': line})
    except Exception as e:
        print(f"Error processing {img_name}: {e}")

# Write to CSV without pandas
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['filename', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"Extraction and CSV creation complete. Output saved to {output_csv}")

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
