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
hbin = '/data/data/com.termux/files/home/bin'
hbak = f'{home}/bak'
start_time = time.time()

try: import osl
except: pass 

hsct = '/data/data/com.termux/files/home/.shortcuts'
os.makedirs(hsct, exist_ok=True)
if not sys.argv[0] == f'{hsct}/{sbn}':
 os.system(f'sudo cp -v {sys.argv[0]} {hsct}/{sbn}')
 if not os.path.isfile(sne):
  os.system(f'ln -sv {sys.argv[0]} {sne}')
 
def usg():
 usg = inspect.cleandoc(f'''
 usage: {sne} <argument>
 ''')
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(f'{sys.argv[0]} ', '')
 #os.system(f'cmd {args}')
 return args

args = sys.argv[1:]
 
#insert_your_codes_here

import os
import glob

# Directory path
mbdir = '/sdcard/mxbkm'
os.makedirs(mbdir, exist_ok=True)

# Get a list of all files in the directory
files = glob.glob(os.path.join(mbdir, '*'))
print(f'files: {files}')

# Sort the files by their modified timestamp in descending order
try:
 newest_file = max(files, key=os.path.getmtime)
except Exception:
 print(f'{frd}isEmpty: {mbdir}')
 sys.exit()

print("{fgr}Newest file:", newest_file)

def fromtcg():
    from tcget import tcget as tcg
    tcg = tcg()
    try:
     if tcg.endswith('.mic'):
      file = tcg
     else:
      file = sys.arg[1]
    except Exception:
     file = input(f'file: ')
 
file = newest_file
print(f'file: {newest_file}')
with open(file, 'r') as jstr:
 jstr = jstr.read()
 jstr = json.loads(jstr)

for uri in jstr['db']['uris']:
    if uri['title']:
        print(f'{fgr}uri:{uri}')
        
sorted_uris = sorted(jstr['db']['uris'], key=lambda x: x['title'].lower())
    
jstr['db']['uris'] = sorted_uris
print(f'new_jstr_content:\n{jstr}')
newbkm = f'{hbin}/mxbkm.mic'


jdmps = json.dumps(jstr).replace("{", "\n{")
jdmps = jdmps.replace(',', ',\n')
print(f'json.dumps: {jdmps}')
 
with open(newbkm, 'w') as onbw:
 onbw.write(f'{jdmps}')
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

os.system(f'termux-share {newbkm}')
