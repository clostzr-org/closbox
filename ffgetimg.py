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
 
#insert_your_codes_here
def fmtt(time_str):
    #time_str = "001122"
    time_str = str(time_str)
    print(f'{frd}time_str in fmtt: {time_str}')
    formatted_time = ""
    for i in range(0, len(time_str), 2):
        formatted_time += time_str[i:i+2] + ":"
    formatted_time = formatted_time[:-1]  # Remove the last colon
    print(f'{fgr}formatted_time: {formatted_time}')
    return(formatted_time)
    
# Input video file
video_file = f"{args[0]}"
print(f'{fbl}src_vid: {video_file}')

# Time in the video to extract the image (format: HH:MM:SS.s)
print(f'{fcy}args1: {args[1]}')
time_str = args[1]

# Check if the time_str has the format "00:11:22.3"
if re.match(r'^\d{2}:\d{2}:\d{2}.\d{1}$', time_str):
   print("The string has the format '00:11:22.3'.")
   video_time = time_str
else:
   print("The string does not have the format '00:11:22.3'.")
   video_time = fmtt(time_str)

# Check if the video_time does not have the format "00:11:22"
if not re.match(r'^\d{2}:\d{2}:\d{2}.\d{1}$', video_time):
   print("The string still does not have the format '00:11:22'.")
   usg()
   sys.exit()
else:
   print("The string has the format '00:11:22.3'.")
   
print(f'{fyl}video_time: {video_time}')

# Get the absolute path of the source directory
source_dir = os.path.dirname(os.path.abspath(video_file))

# Get the video file name without extension
video_name = os.path.splitext(os.path.basename(video_file))[0]

# Format the time to use in the image name
formatted_time = video_time.replace(':', '')

# Output image file name
output_image = f"{source_dir}/{video_name}-{formatted_time}.jpg"

# Extract the image from the video using FFmpeg
subprocess.run(["ffmpeg", "-i", video_file, 
 "-ss", video_time, "-vframes", "1", '-update', '1', 
 output_image
 ])

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
