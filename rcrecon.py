#!/data/data/com.termux/files/usr/bin/python
import csv, datetime, fnmatch, inspect, json
import os, re, sh, shutil, stat, string
import subprocess, sys, time, colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK; brd = Back.RED
bgr = Back.GREEN; byl = Back.YELLOW
bbl = Back.BLUE; bmg = Back.MAGENTA
bcy = Back.CYAN; bwh = Back.WHITE
fbk = Fore.BLACK; frd = Fore.RED
fgr = Fore.GREEN; fyl = Fore.YELLOW
fbl = Fore.BLUE; fmg = Fore.MAGENTA
fcy = Fore.CYAN; fwh = Fore.WHITE
frs = Fore.RESET
stdm = Style.DIM; stnr = Style.NORMAL
stbr = Style.BRIGHT; stra = Style.RESET_ALL
script_dn = os.path.dirname(sys.argv[0])
script_bn = os.path.basename(sys.argv[0])
script_ne = os.path.splitext(script_bn)[0]
dnoext = f'{script_dn}/{script_ne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()

if not os.path.exists(dnoext):
 cmd = ['ln', '-sv', f'{sys.argv[0]}', f'{dnoext}']
 lns = subprocess.run(cmd, stdout=subprocess.PIPE, 
       universal_newlines=True, check=True)
 lno = lns.stdout
 lst = lno.split('-> ')
 print(f'{fcy}symlink: {lst[0]}',
       f'{fyl}source : {lst[1]}')
 
def usg():
 usg = inspect.cleandoc(f'''
 usage: {script_ne} <argument>
 ''')
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(f'{sys.argv[0]} ', '')
 #os.system(f'cmd {args}')
 return args

args = sys.argv[1:]
 
#insert_your_codes_here
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

os.system('rclone config reconnect gdny:')
