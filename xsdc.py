#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
import os, sys, time, inspect, subprocess
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
if not hbin in sys.path:
   sys.path.append(hbin)
import osl
osl.osl(spath)  # Example: symlink a specific file
oslm = []
for message in osl.info:
    oslm.append(message)
    #print(message)

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

def xsd_df():
    import subprocess
    # Run the df command to get disk space information
    df_process = subprocess.Popen(["df"], stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(["grep", "-E", "/storage/*-*"], stdin=df_process.stdout, stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(["awk", "{print $6}"], stdin=grep_process.stdout, stdout=subprocess.PIPE)
    dfx = awk_process.communicate()[0].decode().split()
    xsd = None
    for d in dfx:
        if "-" in d:
           xsd = d
    return xsd
    
def xsd_sh():
    cmd = f'xsdc.sh'
    xsd = subprocess.run(cmd, stdout=subprocess.PIPE, 
          universal_newlines=True, check=True)
    xsd = xsd.stdout
    xsd = xsd.strip()
    return xsd

if __name__ == '__main__':
   if not xsd_df() == None:
      print(xsd_df())
   else:
      print(xsd_sh())
