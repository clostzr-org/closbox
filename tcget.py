#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, subprocess

def ansi_color(fg=None, bg=None, bold=False, underline=False, bright=False, reset=False):
    # Base numbers for standard colors
    colors = {
        'black': 0, 'red': 1, 'green': 2, 'yellow': 3,
        'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7
    }
    
    if  reset:
        return '\033[0m'
        
    codes = []
    
    # 1. Handle Text Styles (Bold/Underline)
    if  bold:
        codes.append("1")
    if  underline:
        codes.append("4")
        
    # 2. Handle Foreground Colors (Standard: 30-37, Bright: 90-97)
    if  fg in colors:
        base = 9 if bright else 3
        codes.append(f"{base}{colors[fg]}")
        
    # 3. Handle Background Colors (Standard: 40-47, Bright: 100-107)
    if  bg in colors:
        base = 10 if bright else 4
        codes.append(f"{base}{colors[bg]}")
        
    # Join all elements with a semicolon if codes exist
    return f"\033[{';'.join(codes)}m" if codes else ""

class Color:
      pass

# Dynamically generate attributes like Color.f_red or Color.b_green
for name in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
    setattr(Color, f"f_{name[:3]}", ansi_color(fg=name))
    setattr(Color, f"b_{name[:3]}", ansi_color(bg=name))

Color.reset = ansi_color(reset=True)

# Usage is incredibly clean:
#print(f"{Color.f_red}{Color.b_yel}Warning!{Color.reset}")



import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'
import time
start_time = time.time()

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    info = []
    home = os.environ['HOME']
    symdir = f'{home}/symlink'
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    if not source_path.endswith('.py'):
       return
    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = f'{symdir}/{lpbn}'
    if not os.path.isdir(symdir):
       os.mkdir(symdir)
    if os.path.exists(link_path):
       if not os.path.islink(link_path):
          os.remove(link_path)
    try:
       os.symlink(source_path, link_path)
    except Exception:
       print(f'failed to create a symlink')
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
       
osl()

def usage():
 usg = inspect.cleandoc(f'''
 = TERMUX-CLIPBOARD-GET
 = usage: {bn00} <command>
 = command:
 = -h    help
 = -p    print    
 ''')
 print(f'{usg}')
 
def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 args = args.strip(' ')
 #os.system(f'cmd {args}')
 return args

def tcget():
 cmd = ['termux-clipboard-get']
 tcget = subprocess.run(
         cmd, check=True, 
         stdout=subprocess.PIPE, 
         text=True
         )
 tcget = tcget.stdout
 return tcget
 
try:
 a1 = sys.argv[1]
 match a1:
  case ('help'|'-h'|'--help'):
   usage()
  case '-p':
   print(f'{tcget()}')
except Exception:
 pass
 
if __name__ == '__main__':
   try:
      print(f'{tcget()}')
   except Exception:
      os.system(f'apt install termux-api')
      print(f'{tcget()}')
