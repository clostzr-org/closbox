#!/data/data/com.termux/files/usr/bin/python
from ansicolors import *

import os, sys
spath = sys.argv[0]
if os.path.islink(spath):
   spath = os.readlink(spath)
   
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'
import time
start_time = time.time()

import osl
osl.osl(sys.argv[0])
for i in osl.info:
    print(f'{i}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
 
def usg():
 hdr = f'Multiling o keyboard settings backup'
 usg = f'{hdr}\nUsage: copy the mokbd settings and call this script'
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 args = args.strip(' ')
 #os.system(f'cmd {args}')
 return args

import subprocess; cmd = f'termux-clipboard-get -h'; 
spr = subprocess.run(cmd.split(), capture_output=True, check=True, text=True, universal_newlines=True); 
sprout = spr.stdout; sperr = spr.stderr; spret = spr.returncode
#print(f'sprout: {sprout}\nsperr: {sperr}\nspret: {spret}')
if not spret == 0:
   os.system(f'apt install termux-api')
   
from tcget import tcget as gcb
gcb = gcb()
try:
 gcbs = gcb.split()
 gcbs0 = gcbs[0]
except Exception:
 print(f'clipboard is empty')
 sys.exit()

print(f'clipboard_content:\n{gcbs}')
print(f'gcb: {frd}{gcb}{frs}')
print(f'{fyl}clipboard_firstString: {gcbs[0]}{frs}')
mkt = f'{sdbne}.txt'

if  gcbs0 == 'OK_Settings_Begin':
    print(f'settings backup file: {mkt}\nexporting.mkbd.settings...')
    dn0 = os.path.dirname(sys.argv[0])
    with open(mkt, 'w') as mktf:
         mktf.write(f'{gcb}')
else:
    usg()
    print(f'exiting...')
    sys.exit()
