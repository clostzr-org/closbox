#!/data/data/com.termux/files/usr/bin/python
import inspect, json, os, subprocess, sys, time

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

if os.path.islink(sys.argv[0]):
   srcp = os.readlink(sys.argv[0])
   if os.path.isfile(srcp):
      print(f'caller: {sys.argv[0]}')
      print(f'caller_islink_to: {srcp}')
else:
   srcp = sys.argv[0]
   
sdn   = os.path.dirname(srcp)
sbn   = os.path.basename(srcp)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
snadd = sdbne + '.add.txt'
sntxt = sdbne + '.txt'
sntxt_sorted = f'{sdbne}.sorted.txt'
snjsn = sdbne + '.json'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

info = inspect.cleandoc(f'''
sourcepath: {srcp}
  datapath: {sntxt}
''')
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

args = sys.argv[1:]
jargs = ' '.join(args).strip()
    
def usg():
    usg = inspect.cleandoc(f'''
    {info}
    usage: {sne} [command] [url]
    commands: (under construction)
    ''')
    print(f'{usg}')

'''
Certainly! Here's an updated version of the script that counts the number of files 
that have been downloaded from a playlist using  yt-dlp  and displays progress notifications in Termux:
'''

import subprocess
import re

def show_progress_notification(progress, file_count):
    percent = progress['percent']
    eta = progress['eta']
    speed = progress['speed']

    message = f"Downloading: {percent}%\nETA: {eta}\nSpeed: {speed}\nFiles Downloaded: {file_count}"
    subprocess.run(['termux-notification', '--title', 'YouTube Downloader', '--content', message])

def download_playlist(playlist_url):
    command = ['yt-dlp', 
    playlist_url, 
    '-x',
    '-c',
    '-i',
    '-o',
    '/sdcard/Download/%(playlist)s/%(playlist_index)s_-_%(title)s.%(ext)s',
    '--geo-bypass',
    '--geo-bypass-country', 'US',
    '--restrict-filenames',
    '-f', 'bestaudio', '--progress']
    print(f'command: {command}')

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    file_count = 0

    for line in iter(process.stdout.readline, ''):
        print(f'line: {line}')
        progress_match = re.match(r'\[download\]\s+(\d+.\d)% of', line)
        eta_match = re.match(r'\[download\]\s+ETA\s+([^\s]+)', line)
        speed_match = re.match(r'\[download\]\s+([^\s]+)\s+at', line)
        file_match = re.match(r'\[download\]\s+Destination:\s+[^\s]+', line)

        if progress_match and eta_match and speed_match:
            progress = {
                'percent': float(progress_match.group(1)),
                'eta': eta_match.group(1),
                'speed': speed_match.group(1)
            }
            file_count += 1
            show_progress_notification(progress, file_count)

        elif file_match:
            file_count += 1

    process.wait()

# Usage
#playlist_url = 'https://www.youtube.com/playlist?list=PLAYLIST_ID'
try:
 print(f'args: {sys.argv[1]}')
 playlist_url = f'{sys.argv[1]}'
except Exception:
 usg()
 sys.exit()
download_playlist(playlist_url)

'''
In this updated script, the  show_progress_notification()  function is modified to 
include the  file_count  parameter. The function now displays the download progress, 
ETA, speed, and the number of files downloaded so far.
 
The  download_playlist()  function is updated to keep track of the  file_count  variable. 
Whenever a progress line is detected, the  file_count  is incremented, and the  
show_progress_notification()  function is called with the updated  file_count .
 
Additionally, a new regular expression pattern  file_match  is introduced to 
detect the lines indicating the destination file for each downloaded file. 
When a line matching this pattern is found, the  file_count  is incremented.
 
To use this script, replace  'https://www.youtube.com/playlist?list=PLAYLIST_ID'  with 
the actual URL of the YouTube playlist you want to
'''
