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
verbose = False
start_time = time.time()
 
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
 
#insert_your_codes_here
'''
I see, my apologies for the confusion. 
Here's the modified Python script to convert any video file to mp4 
using the command you provided:
'''
import os
import subprocess

def convert_to_mp4(input_file, output_dir=None):
    """
    Converts video/image files (mp4, avi, mov, gif, webm) to MP4 format.
    """
    if output_dir is None:
        output_dir = os.path.dirname(input_file)
    
    if os.path.isdir(input_file):
        for file_name in os.listdir(input_file):
            file_path = os.path.join(input_file, file_name)
            if os.path.isfile(file_path) and file_name.endswith(('.mp4', '.avi', '.mov', '.gif', '.webm')):
                output_file = os.path.splitext(file_name)[0] + '.mp4'
                output_path = os.path.join(output_dir, output_file)
                convert_file(file_path, output_path)
    else:
        output_file = os.path.splitext(os.path.basename(input_file))[0] + '.mp4'
        output_path = os.path.join(output_dir, output_file)
        convert_file(input_file, output_path)

def convert_file(input_path, output_path):
    """
    Helper function to convert a single video/image file to MP4.
    """
    command = [
        "ffmpeg",
        "-i", input_path,
        "-movflags", "faststart",
        "-pix_fmt", "yuv420p",
        "-vf", "fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2",
        "-g", "30",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        output_path
    ]
    subprocess.run(command)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python convert_to_mp4.py input_file_or_directory [output_directory]')
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    convert_to_mp4(input_file, output_dir)
'''
In this modified version, the  convert_to_mp4()  function
 is almost identical to the previous  convert_to_gif()  function, 
except that it now uses the  ffmpeg  command with the options you 
provided to convert the input video file to mp4. 
The script can now handle any video file with 
extensions  .mp4 ,  .avi ,  .mov ,  .gif , and  .webm .
 
To use this script, save it to a file (e.g.  convert_to_mp4.py ) 
and run it with the input file or directory as 
an argument ( python convert_to_mp4.py input_file_or_directory ). 
If an output directory is not provided, the output file will 
be saved in the same directory as the input file.
'''

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
