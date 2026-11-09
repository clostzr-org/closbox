#!/data/data/com.termux/files/usr/bin/python

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
verbose = False

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
       pass
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' exists.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()

args = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr}audio volume up {frs}
 function: {fyl}increase audio volume and normalize it to prevents clipping {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here
import subprocess

def increase_volume_ffmpeg(input_file, output_file, gain_db):
    try:
        command = [
            'ffmpeg',
            '-i', input_file,
            '-af', f'volume={gain_db}dB, loudnorm=I=-5:TP=0:LRA=50',
            '-ab', '128k',
            '-ar', '44100',
            output_file, '-y'
        ]
        spr = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)
        print(f'{spr.stdout}')
        print(f"Successfully increased volume and normalized audio. Output file: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
try:
   input_file = sys.argv[1]  # Replace with your input audio file
except Exception:
   from tcget import tcget
   input_file = tcget()
   if not os.path.exists(input_file):
      input_file = input(f'input_file: ')
      
if not os.path.exists(input_file):
   print(f'{frd}doesnt exists{frs}: {input_file}')
   sys.exit()
   
fbn = input_file.rsplit('.', 1)[0]
ext = input_file.rsplit('.', 1)[1]

output_file = f'{fbn}-vlp.{ext}' # Replace with your desired output audio file
print(f'output_file: {output_file}')
gain_db = 128  # Adjust the gain in decibels as needed

increase_volume_ffmpeg(input_file, output_file, gain_db)


if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
