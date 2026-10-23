#!/data/data/com.termux/files/usr/bin/python
import datetime, fnmatch, inspect, json
import os, re, shutil
import stat, subprocess, sys
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK
brd = Back.RED
bgr = Back.GREEN
byl = Back.YELLOW
bbl = Back.BLUE
bmg = Back.MAGENTA
bcy = Back.CYAN
bwh = Back.WHITE
fbk = Fore.BLACK
frd = Fore.RED
fgr = Fore.GREEN
fyl = Fore.YELLOW
fbl = Fore.BLUE
fmg = Fore.MAGENTA
fcy = Fore.CYAN
fwh = Fore.WHITE
frs = Fore.RESET
stdm = Style.DIM
stnr = Style.NORMAL
stbr = Style.BRIGHT

dn00 = os.path.dirname(sys.argv[0])
bn00 = os.path.basename(sys.argv[0])
bn0s = os.path.splitext(bn00)
bs00 = bn0s[0]
db00 = f'{dn00}/{bs00}'
home = f'/data/data/com.termux/files/home'
hbak = f'{home}/bak'

try: import osl 
except: pass

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 args = args.strip(' ')
 #os.system(f'cmd {args}')
 return args
 
if os.path.isdir('/sdcard/MyBoy'):
 pass
else:
 print(f'/sdcard/MyBoy not found')
 sys.exit()

cmd = ['rclone', 'copyto', '/sdcard/MyBoy', 'gdsh:Myboy', '-vvvv']
bakgba = subprocess.run(
cmd, check=True, stdout=subprocess.PIPE, universal_newlines=True
) 
