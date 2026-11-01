#!/data/data/com.termux/files/usr/bin/python
import inspect, os, shutil, subprocess, sys, time

def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
        'black':  '\033[30m',        'red':    '\033[31m',
        'green':  '\033[32m',        'yellow': '\033[33m',
        'blue':   '\033[34m',        'magenta':'\033[35m',
        'cyan':   '\033[36m',        'white':  '\033[37m',
        'reset': '\033[0m'
    }

    code = ''
    if reset:
        code = color_codes['reset']
    elif fg:
        code = color_codes.get(fg, '')
    elif bg:
        code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'  # Background code adjustment

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

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'

verbose = False
start_time = time.time()

try: import osl
except: pass 

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
    os.symlink(source_path, link_path)
    if os.path.islink(link_path):
        info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
        info.append(f"Failed to create symbolic link '{link_path}'.")

osl()

def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
    ''')
    print(f'{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()

rcmain = '/data/data/com.termux/files/home/.config/rclone/rclone.conf'
rcmdir = os.path.dirname(rcmain)
if not os.path.isdir(rcmdir):
   os.makedirs(rcmdir, exist_ok=True)
rchbin = '/data/data/com.termux/files/home/bin/rclone.conf'

if os.path.isfile(rcmain):
 gszmain = os.path.getsize(rcmain)
 gmtmain = os.path.getmtime(rcmain)
else:
 gszmain = 'n/a'
 gmtmain = 'n/a'
 
if os.path.isfile(rchbin):
 gszhbin = os.path.getsize(rchbin)
 gmthbin = os.path.getmtime(rchbin)
else:
 gszhbin = 'n/a'
 gmthbin = 'n/a'

nfo = inspect.cleandoc(f'''
rcmain: {rcmain}
rchbin: {rchbin}
getsize_main: {gszmain}
getsize_hbin: {gszhbin}
getmt_main: {gmtmain}
getmt_hbin: {gmthbin}
''')
print(f'{nfo}')

if os.path.isfile(rcmain):
 print(f'{rcmain} {fgr}exists{frs}\ncopying rcmain to rchbin...')
 shutil.copy2(rcmain, rchbin)
else:
 print(f'{rcmain} {frd}doesnt_exists{frs}\ncopying rchbin to rcmain...')
 shutil.copy2(rchbin, rcmain)
  
#print(f'you must call this with: sudo {sys.argv[0]}')
sys.exit()
