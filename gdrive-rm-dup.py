#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
import   requests,  random, socket, glob
from bs4 import BeautifulSoup
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
hbak  = f'{home}/bak'
start_time = time.time()

if not os.path.isfile(sdbne):
   os.system(f'ln -sv {sys.argv[0]} {sdbne}')
    
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
google_drive_remote = "gdrs:nintendo/gba/rom/"

remove_older_duplicates(google_drive_remote)

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
