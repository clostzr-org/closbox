#!/data/data/com.termux/files/usr/bin/python
import colorama
from colorama import Back, Fore
colorama.init(autoreset=True)
import datetime, fnmatch, inspect, json
import os, re, sh, shutil
import stat, subprocess, sys
bbl = Back.BLUE
bcy = Back.CYAN
bgr = Back.GREEN
blb = Back.LIGHTBLUE_EX
bmg = Back.MAGENTA
brd = Back.RED
brs = Back.RESET
byl = Back.YELLOW
fbl = Fore.BLUE
fcy = Fore.CYAN
fgr = Fore.GREEN
flb = Fore.LIGHTBLUE_EX
fmg = Fore.MAGENTA
frd = Fore.RED
frs = Fore.RESET
fyl = Fore.YELLOW
caller = sys.argv[0].replace('.py', '')

if os.path.isfile(caller):
 print(f'exist: {caller}')
else:
 print(f'not-exist: {caller}')

if not os.path.isfile(caller):
 print(f'not-exist: {caller}')
else:
 print(f'exist: {caller}')

try:
 open(caller, 'r')
 print(f'open-read {caller} done')
except Exception:
 print(f'cannot open {caller}')
 
def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 #os.system(f'cmd {args}')
 
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

colors = dict(Fore.__dict__.items())

for color in colors.keys():
    print(colors[color] + f"{color}")
