#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
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
sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()
try: import osl
except: pass
 
def usg():
 usg = inspect.cleandoc(f'''
 usage: {sne} <option>
 options: -d select directory
          -f select file
 ''')
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(f'{sys.argv[0]} ', '')
 #os.system(f'cmd {args}')
 return args

args = sys.argv[1:]
 
#insert_your_codes_here
if '-d' in args:
 cmd = '--select-folder'
if '-f' in args:
 cmd = '--select-file'
if not '-d' in args or '-f' in args:
 usg(); sys.exit()
tgf = 'termux-gui-files'
cmd = [f'{tgf}', f'{cmd}']
tgfc = subprocess.run(cmd, stdout=subprocess.PIPE, 
universal_newlines=True, check=True)
fout = tgfc.stdout
print(f'fout: {fout}')
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
