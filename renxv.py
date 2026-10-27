#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv, sh
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

# Define colors for printing
red = "\033[91m"
blu = "\033[94m"
nll = "\033[0m"

# List all files in the current directory
files = os.listdir()

for a in files:
    if os.path.isdir(a):
        continue
    if a.split('.')[-1] == "4pm":
        print(f"{red}4pm:{a}{nll}")
        os.rename(a, f"{a.split('.')[0]}.mp4")
    if a.split('.')[-1] == "mp4":
        print(f"{blu}mp4:{a}{nll}")
        os.rename(a, f"{a.split('.')[0]}.4pm")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
