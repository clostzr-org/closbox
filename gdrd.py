#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, subprocess
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
hsym  = home + '/symlink'
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
       print(f'failed to create a symlink')
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
       
osl()

args = sys.argv[1:]
jargs = ' '.join(args).strip()

def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} [argument]
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    if args == sys.argv[0]:
       args = ''
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
import os

# Function to run rclone command
def run_rclone_command(command):
    return os.popen(command).read()

# List all files in a Google Drive remote
def list_files_in_remote(remote_name):
    return run_rclone_command(f"rclone lsf {remote_name}")

# Get file modified timestamp
def get_file_modtime(remote_name, file_name):
    return run_rclone_command(f"rclone lsl {remote_name}{file_name} --json")

# Compare and remove older duplicates
def remove_older_duplicates(remote_name):
    files = list_files_in_remote(remote_name).splitlines()

    for file in files:
        print(f'current_file: {fmg}{file}')
        identical_files = [f for f in files if f.split('/')[-1] == file.split('/')[-1] and f != file]
        if identical_files:
            newest_file = max([file] + identical_files, key=lambda f: get_file_modtime(remote_name, f))
            older_files = [f for f in identical_files if f != newest_file]
            print(f'newest: {newest_file}')
            for older_file in older_files:
                print(f'older: {frd}{older_file}')
                run_rclone_command(f"rclone delete {remote_name}{older_file}")
    
    print("Duplicate files handling completed.")

# Specify your Google Drive remote name
#google_drive_remote = "gdrs:nintendo/gba/rom/"

remove_older_duplicates(google_drive_remote)

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
