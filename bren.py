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
import inspect
import os
import sys
import time

sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = sbn.rsplit('.', 1)[0]
scf = f'{sdn}{os.sep}{sne}.cmd'
nfo = inspect.cleandoc(f'''
      sne: {sne}
      scf: {scf}
      ''')

def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
    ''')
    print(f'{usg}')

print(f'os.name: {os.name}\n{nfo}')
if not os.path.exists(f'{sdn}{os.sep}{sne}.cmd'):
    print(f'creating cmd file for current script ({sne})')
    with open(scf, 'w') as oscfw:
        scont = inspect.cleandoc(f'''
        @echo off
        setLocal enableDelayedExpansion
        title %CD%
        "%~dpn0.py" %* 
        ''')
        oscfw.write(scont)
        print(f'new_cmd: {scf}')
        
try:
    sa1 = sys.argv[1]
    print(f'argument: {sa1}')
except:
    sa1 = ''
    print(f'argument is empty')

import os
import re

def batch_rename_files():
    """
    Batch renames files in the current directory based on user input.  Provides a preview and confirmation before execution.
    """

    # Get working directory
    working_dir = os.getcwd()  #Use current directory by default

    #List all files in the directory.
    files = [f for f in os.listdir(working_dir) if os.path.isfile(os.path.join(working_dir, f))]
    if not files:
        print("No files found in the directory.")
        return

    print("Files in the directory:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")


    # Get user input for replacement
    prompt_1 = "Type the word u want to replace and its replacement (separated with space) "
    while True:
        try:
            #old_word = input("Enter the word to replace: ")
            #new_word = input("Enter the replacement word: ")
            old_word, new_word = input(f'{prompt_1}').split()
            print(f'oldword: "{old_word}", newword: "{new_word}" ')
            if not old_word or not new_word:
                raise ValueError("Both words cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Find files matching the pattern and create a preview
    files_to_rename = []
    for file in files:
        if old_word in file:
            new_name = file.replace(old_word, new_word)
            if new_name != file:  #Skip if names are identical
                files_to_rename.append((file, new_name))

    if not files_to_rename:
        print("No files found matching the replacement pattern.")
        return


    print("\nPreview of files to be renamed:")
    for old_name, new_name in files_to_rename:
        print(f"{old_name} -> {new_name}")

    # Confirmation before renaming
    confirmation = input("\nConfirm rename (y/n)? ")
    if confirmation.lower() != 'y':
        print("Rename cancelled.")
        return

    # Perform the renaming
    for old_name, new_name in files_to_rename:
        try:
            os.rename(os.path.join(working_dir, old_name), os.path.join(working_dir, new_name))
            print(f"Renamed '{old_name}' to '{new_name}' successfully.")
        except OSError as e:
            print(f"Error renaming '{old_name}': {e}")

    print("\nBatch renaming complete.")


if __name__ == "__main__":
    if os.path.isdir(sa1):
       os.chdir(sa1)
    batch_rename_files()

print(f'all done')
time.sleep(4)
#input(f'press ENTER')


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
