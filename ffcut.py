#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, subprocess
def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
    'black':'\033[30m', 'red'    :'\033[31m',
    'green':'\033[32m', 'yellow' :'\033[33m',
    'blue' :'\033[34m', 'magenta':'\033[35m',
    'cyan' :'\033[36m', 'white'  :'\033[37m',
    'reset':'\033[0m'
    }
    code = ''
    if reset:
       code = color_codes['reset']
    elif fg:
       code = color_codes.get(fg, '')
    elif bg:
       code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'
    return code

# Define color shortcuts for convenience
fbk = ansi_color(fg='black')
frd = ansi_color(fg='red')
fgr = ansi_color(fg='green')
fyl = ansi_color(fg='yellow')
fbl = ansi_color(fg='blue')
fmg = ansi_color(fg='magenta')
fcy = ansi_color(fg='cyan')
fwh = ansi_color(fg='white')
frs = ansi_color(fg='reset')

bbk = ansi_color(bg='black')
brd = ansi_color(bg='red')
bgr = ansi_color(bg='green')
bcy = ansi_color(bg='yellow')
byl = ansi_color(bg='blue')
bbl = ansi_color(bg='magenta')
bmg = ansi_color(bg='cyan')
bwh = ansi_color(bg='white')
brs = ansi_color(bg='reset')
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


def fmtt():
    time_str = "001122"
    formatted_time = ":".join([time_str[i:i+2] for i in range(0, len(time_str), 2)])
    print(formatted_time)

def fmtt_v2():
    time_str = "001122"
    formatted_time = ""
    for i in range(0, len(time_str), 2):
        formatted_time += time_str[i:i+2] + ":"
    formatted_time = formatted_time[:-1]  # Remove the last colon
    print(formatted_time)
    
def usg():
 usg = inspect.cleandoc(f'''
 usage: {bn00} <argument>
 ''')
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 args = args.strip(' ')
 #os.system(f'cmd {args}')
 return args
 
args=exargs()
from tcget import tcget
tcg=tcget()
if os.path.isfile(tcg):
 args=f'{tcg} {args}'

print(f'args: {args}')
args=args.split()

#ss=f'00:00:00'
#to=f'59:59:59'

for a in args:
 if a.startswith(f'ss='):
  spss=a.split('=')
  ss=spss[1]
  print(f'startFrom: {ss}')
 if a.startswith(f'to='):
  spto=a.split('=')
  to=spto[1]
  print(f'finishAt: {to}')
 if os.path.isfile(a):
  file=a
  
try:
 os.path.isfile(file)
except Exception:
 file=input(f'fileInputHere: ')
 
if os.path.isfile(file):
 print(f'fileExists: {file}')
else:
 print(f'FileDoesntExists: {file}')
 sys.exit()
opsa=os.path.splitext(file)
out=opsa[0]
ext=opsa[1]
  
try:
 ss1=ss.replace(f':', '')
except Exception:
 ss1=f'start'
try:
 to1=to.replace(f':', '')
except Exception:
 to1=f'end'

outfile=f'{out}.{ss1}-{to1}{ext}'
print(f'output: {outfile}')
cmd=f'ffmpeg -i {file} '
try:
 ssc=f'-ss {ss}'
 cmd+=f'{ssc} '
except Exception:
 pass
try:
 toc=f'-to {to}'
 cmd+=f'{toc} '
except Exception:
 pass

cmd+=f'{outfile} '

print(f'command: {cmd}')
os.system(f'{cmd}')

