#!/data/data/com.termux/files/usr/bin/python
import colorama, inspect, os, subprocess, sys, time
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
import socket

def check_internet():
    host = 'www.google.com'; port = 80; timeout = 2
    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except socket.error:
        print("No internet connection available.")
        return False
        
if __name__ == '__main__':
 if check_internet():
  print(f'connected')
 else:
  print(f'not_connected')
  
 end_time = time.time()
 elapsed_time = end_time - start_time
 print(f"Elapsed time: {elapsed_time} seconds")
