#!/data/data/com.termux/files/usr/bin/python
import colorama, datetime, glob, inspect, json, os
import re, sh, stat, subprocess, sys
from colorama import Fore
fbl = Fore.BLUE
fcy = Fore.CYAN
fgr = Fore.GREEN
flb = Fore.LIGHTBLUE_EX
fmg = Fore.MAGENTA
frd = Fore.RED
frs = Fore.RESET
fyl = Fore.YELLOW
caller = sys.argv[0].replace('.py', '')
argc = len(sys.argv)
if argc > 1:
 a1 = sys.argv[1]
else:
 pass
try:
 with open(caller, 'r'):
  pass
except Exception:
 import mkexe
 from mkexe import mkx
 mkx(sys.argv[0])
 
def fun_args():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 os.system(f"7zz {args}")

from subpr import subprcmd
tsd = subprcmd(["echo", "$HOME"])
tsd = subprocess.run(
['echo', '$HOME'], check=True, 
stdout=subprocess.PIPE, universal_newlines=True
)
tsd = tsd.stdout
ddcfh = '/data/data/com.termux/files/home/'
hbin = f'{ddcfh}bin/'
hbak = f'{ddcfh}bak/'
hbb = f'{hbak}bin/'
thb = f'{hbb}thbnr'
print(f'--ddcfh: {ddcfh}')

def func_xsd():
 extsd = subprocess.run(
 ['extSd'], 
 check=True, stdout=subprocess.PIPE, 
 universal_newlines=True
 )
 extsd = extsd.stdout
 extsd = extsd.strip()
 xxt = f'{extsd}xbin/thbin64'
 
oldfiles = glob.glob(f'{thb}*')
for o in oldfiles:
 print(f'__oldfile: {o}')
 if os.path.isfile(o):
  os.remove(o)
  print(f'__{frd}has been removed{frs}: {o}')

from datetime import datetime
now = datetime.now()
ctm = now.strftime("%Y.%m%d.%H%M%S")
ctm_ym = now.strftime("%Y.%B")

print(f"__current time: {ctm}")
print(f'--currentDir: {os.getcwd()}')
zcmd = subprocess.run([
'7zz', '-phshchk6', 
'a', f'{thb}.{ctm}.zip', f'{hbin}/*'
], 
check=True, stdout=subprocess.PIPE, 
universal_newlines=True
)
zcmd = zcmd.stdout
print(f'__{fgr}zcmd{frs}: {zcmd}')

cmd1 = ['rclone', 'ls', 'eg16:/']
spr1 = subprocess.run(
cmd1, check=True, 
stdout=subprocess.PIPE, universal_newlines=True
)

cmd_rc = subprocess.run(
[
'rclone', 'sync', hbb, 'eg16:/thbnr/', '-v'
], 
check=True, stdout=subprocess.PIPE, 
universal_newlines=True
)
print(f"__{fcy}thbSync operation complete.{frs}")

synclp = subprocess.run(
['rclone', 'sync', f'{hbak}lp/', 'eg16:/lp/', '-v'], 
check=True, 
stdout=subprocess.PIPE, 
universal_newlines=True
)
print(f"__{fcy}lpSync operation complete.{frs}")
