#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, subprocess
from ansicolors import *

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

import osl
osl.osl(sys.argv[0])
for m in osl.info:
    print(f'{m}')

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

#insert_your_codes_here
def usg():
    inspect.cleandoc(f'''
    create a 60 seconds audio track from a short audio
    usage: {sne} [audiofile]
    ''') 

import subprocess
import json

def get_audio_duration(file_path):
    try:
        command = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            file_path
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = json.loads(result.stdout)
        duration = float(output['format']['duration'])
        return duration
    except Exception as e:
        print(f"Error: {e}")
        return None

def looper(file):
    print(f'current file: {file}')
    gad = get_audio_duration(file)
    if gad is not None:
       print(f'duration: {gad}')
    else:
       return
    if gad > 60:
       print(f'duration exceeds 60s')
       return
    # Get the absolute directory and basename of the input file
    abs_dirname = os.path.dirname(os.path.abspath(file))
    basename = os.path.splitext(os.path.basename(file))[0]
    ext = os.path.splitext(file)[1][1:]
    
    # Output file naming format
    output_file = f"{abs_dirname}/{basename}-60s.{ext}"
    print(f'output_file: {output_file}')
    ffmpeg_command = f"ffmpeg -i {file} -filter_complex 'aloop=loop=-1:size=60*44100' -t 60 -ab 256k -ar 44100 {output_file} -y"
    os.system(ffmpeg_command)
    
def isfolder(dir):
    from pathlib import Path

    directory = Path(dir)
    
    for item in directory.iterdir():
        if item.is_file():
            print(f"File: {item.name}")
            looper(dir + '/' + item.name)
        elif item.is_dir():
            print(f"Directory: {item.name}")
            isfolder(dir + '/' + item.name)

       
# Input file path
print(f'args = {args}')
try:
 infile = args[0]
except Exception:
 from tcget import tcget
 infile = tcget()
 if os.path.exists(infile):
    if os.path.isfile(infile):
       input_file = infile
       print(f'input_file: {input_file}')
 else:
    infile = input(f'audio source: ')

if not os.path.exists(infile):
   print(f'doesnt exists: {frd}{infile}{frs}')
   sys.exit()
   
if os.path.isdir(infile):
   isfolder(infile)
   
if os.path.isfile(infile):
   looper(infile)
    
if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
