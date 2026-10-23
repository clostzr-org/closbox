#!/data/data/com.termux/files/usr/bin/python
import colorama, inspect, os, subprocess, sys, time
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
import os
import ffmpeg

# Set the directory where the videos are located
video_dir = "/storage/emulated/0/video_directory"

# Get the absolute path of the video directory
video_dir_abs = os.path.abspath(video_dir)

# Create the "resized" subdirectory if it doesn't exist
resized_dir = os.path.join(video_dir_abs, "resized")
os.makedirs(resized_dir, exist_ok=True)

# Loop through all files in the directory
for filename in os.listdir(video_dir):
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".mkv"):
        video_path = os.path.join(video_dir_abs, filename)
        
        # Get the original resolution of the video
        probe = ffmpeg.probe(video_path)
        width = probe["streams"][0]["width"]
        height = probe["streams"][0]["height"]
        
        # Check if the resolution is greater than 720x1280 or 1280x720
        if (width > 720 and height > 1280) or (width > 1280 and height > 720):
            # Calculate the new resolution
            new_width = width // 2
            new_height = height // 2
            
            # Resize the video using ffmpeg
            resized_filename = f"resized_{filename.split('.')[0]}_{new_width}x{new_height}p.{filename.split('.')[-1]}"
            resized_path = os.path.join(resized_dir, resized_filename)
            
            try:
                (
                    ffmpeg
                    .input(video_path)
                    .filter("scale", new_width, new_height)
                    .output(resized_path)
                    .run()
                )
                print(f"Resized {filename} to {new_width}x{new_height}")
                
                # Remove the source video if the resizing was successful
                os.remove(video_path)
                print(f"Removed source video: {filename}")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")
        else:
            print(f"{filename} is already smaller than 720x1280 or 1280x720, skipping...")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
