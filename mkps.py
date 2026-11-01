#!/data/data/com.termux/files/usr/bin/python
import colorama, inspect, os, subprocess, sys, time

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
 import osl
except Exception:
 print(f'unable to import osl')

def usg():
 usg = inspect.cleandoc(f'''
 make-a-python-script
 usage: {sbn} <scriptname>
 ''')
 print(f'{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
if not args:
 print(f'no_args')
 usg()
 sys.exit()
 
#insert_your_codes_here
headlines = inspect.cleandoc(f'''
#!/usr/bin/env python3
import colorama, inspect, os, subprocess, sys, time

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
stdm  = Style.DIM;    stnr = Style.NORMAL
stbr  = Style.BRIGHT; stra = Style.RESET_ALL

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{{sdn}}/{{sne}}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'

start_time = time.time()

desc = inspect.cleandoc(f\'\'\'
    alias:{{fgr}} {{frs}}
 function:{{fyl}} {{frs}}
\'\'\')
print(f'{{desc}}')
    
try:
 import osl
except Exception:
 print(f'{{frd}}unable to import osl{{frs}}')
 
def usg():
    usg = inspect.cleandoc(f\'\'\'
    usage: {{sbn}} [argument]
    \'\'\')
    print(f'{{usg}}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
 
#insert_your_codes_here

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {{elapsed_time}} seconds")
''')

for arg in args:
 arg = arg.replace('.py', '')
 sfile = f'{arg}.py'
 if arg == '-h':
  usg()
  sys.exit()
 if os.path.isfile(sfile):
  exists = True
  subprocess.run(['micro', sfile])
 else:
  exists = False
  with open(sfile, 'w') as osfw:
   osfw.write(f'{headlines}\n')
  os.chmod(sfile, 0o755)
  subprocess.run(['micro', sfile])
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
