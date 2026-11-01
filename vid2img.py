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
    extract images from a video
    usage: {sne} [videopath] [interval]
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
def extract_images(input_file, interval):
    input_folder = os.path.dirname(input_file)
    # Get the input file name without extension
    file_name = os.path.splitext(os.path.basename(input_file))[0]

    # Create the output folder based on the input file name
    output_folder = f'{file_name}-images'
    output_folder = f'{os.path.join(input_folder, output_folder)}'
    os.makedirs(output_folder, exist_ok=True)

    # Generate the FFmpeg command
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'thumbnail={interval}',
        '-vsync', '0',
        f'{output_folder}/image-%03d.jpg'
    ]

    # Run the FFmpeg command
    subprocess.run(ffmpeg_command)

# Specify the input MP4 file path
input_file = f'{exargs()}'
if not os.path.isfile(input_file):
 print(f'current argument is not a file ({input_file})')
 sys.exit()
if not input_file.endswith('.mp4'):
 print(f'current file: {input_file}')
 print(f'current file is not a mp4 file')
 sys.exit()

# Specify the interval in seconds
interval = 64

usg()
print(f'videopath: {input_file}')
interval = input(f'interval: ')

# Call the function to extract images
extract_images(input_file, interval)

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
