#!/data/data/com.termux/files/usr/bin/python
import datetime, fnmatch, inspect, json
import os, re, sh, shutil
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
stra = Style.RESET_ALL
bn0 = os.path.basename(sys.argv[0])
bn00 = os.path.splitext(bn0)
bns = bn00[0]
dst = 'gdsh:'
dn00 = os.path.dirname(sys.argv[0])
bn00 = os.path.basename(sys.argv[0])
bn0s = os.path.splitext(bn00)
bs00 = bn0s[0]
db00 = f'{dn00}/{bs00}'
dbC = f'{db00}.csv'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
#aapt = '/data/data/com.termux/files/usr/bin/aapt'
aapt = '/data/data/com.termux/files/usr/bin/aapt2'

try:
 with open(db00, 'r') as odbr:
  odbr.read()
  #print(f'= symlink exists ({db00})')
except Exception:
 os.system(f'ln -sv {sys.argv[0]} {db00}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 args = args.strip(' ')
 #os.system(f'cmd {args}')
 return args

def usg():
 usg = inspect.cleandoc(f'''
   RCLONE: UPLOAD APK(S)
 usage: {bns} <apkfile|t> <folder>
 ''') 
 print(f'{usg}')
 
try:
 arg1 = sys.argv[1]
 print(f'  argument.01: {arg1}')
 try:
  arg2 = sys.argv[2]
  dst = f'{dst}apk/{arg2}'
  predef = True
  print(f'  destination folder: {dst}')
 except Exception:
  predef = False
  dst = f'{dst}apk'
  print(f'  folder is unspecified.')
  print(f'  falling back to: {dst}')
except Exception:
 usg()
 sys.exit()

match arg1:
 case 't':
  from tcget import tcget
  a1 = tcget()
 case _:
  a1 = arg1

ifa1 = os.path.isfile(a1)
if ifa1 == True:
 print(f'  isFile: {a1}')
 a1b = os.path.basename(a1)
 a1d = os.path.dirname(a1)
 try:
  a1d1 = os.path.basename(a1d)
 except Exception:
  a1d1 = 'misc'
 if predef == True:
  pass
 else:
  dst = f'{dst}/{a1d1}'
 fnfo = inspect.cleandoc(f'''
 __filename: {a1b}
 __lcldir: {a1d}
 __clddir: {a1d1}
 __dstdir: {dst}
 ''')
 print(f'  file.info:\n{fnfo}')
else:
 print(f'  isNotFile: {a1}')
 sys.exit()
 
cmd = ['rclone', 'copy', f'{a1}', f'{dst}', '-P', '-vvvv']
rcu = subprocess.run(cmd, check=True, 
stdout=subprocess.PIPE, universal_newlines=True) 

