#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
import   requests,  random, socket, glob
from bs4 import BeautifulSoup
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
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'
start_time = time.time()
try: import osl  
except: pass
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} [argument]
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    if args == sys.argv[0]:
       args = ''
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
if len(args) < 1:
 usg()
 sys.exit()
 
#insert_your_codes_here
newlines = []
for arg in args:
    if os.path.isfile(arg):
     oldraw = arg
     print(f'old raw file: {oldraw}')
     newraw = f'{oldraw}.new'
     print(f'new raw file: {newraw}')
     with open(oldraw, 'r') as oldr:
      lines = oldr.readlines()
      print(f'lines:\n{lines}')
      for line in lines:
          print(f'original line:\n{line}')
          line = line.replace(']•', ']≈•')
          line = line.split('≈')
          val = line
          print(f'splitted line: {line}')
          newline = f'{val[0]}_{val[2]}≈{val[1]}≈{val[3]}'
          print(f'newline: {newline}')
          newlines.append(newline)
    else:
     usg()
     sys.exit()
          
print(f'newlines:\n{newlines}')
with open(newraw, 'w') as onrw:
    onrw.writelines(newlines)
 
if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
