#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
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
stdm = Style.DIM;    stnr = Style.NORMAL
stbr = Style.BRIGHT; stra = Style.RESET_ALL
sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()
try:
 import android
except Exception:
 import subprocess
 cmd = 'pip install boot python-android '
 out = subprocess.run(cmd.split(), capture_output=True, text=True)
 out = out.stdout
 print(out)
 import android
 

def is_rooted():
    return android.checkRoot()

if is_rooted():
    print("Device likely rooted")
else:
    print("Device likely not rooted")


import subprocess

try:
    result = subprocess.run(['su', '-c', 'ls'], capture_output=True, text=True)

    if result.stderr:
        print("Error occurred:")
        print(result.stderr)
    else:
        print("Command executed successfully.")

except FileNotFoundError:
    print("Command not found.")

try:
 os.system(f'su -c getprop')
except Exception:
 print(f'su not found, exiting ...')
 sys.exit()

hsct = '/data/data/com.termux/files/home/.shortcuts'
os.makedirs(hsct, exist_ok=True)
if not sys.argv[0] == f'{hsct}/{sbn}':
 os.system(f'sudo cp -v {sys.argv[0]} {hsct}/{sbn}')
 if not os.path.isfile(sne):
  os.system(f'ln -sv {sys.argv[0]} {sne}')

ascas = 'am start -n com.android.settings/.SubSettings'
casar = 'com.android.settings.applications.RunningServices'
os.system(f'su -c "{ascas} -e :settings:show_fragment {casar}" ')
