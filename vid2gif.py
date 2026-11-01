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
Sure, to set the output directory to be the same as 
the source directory, you can modify the  
convert_to_gif()  function 
as follows:
'''

def convert_to_gif(input_file, output_dir=None):
    """
    Converts video files (mp4, avi, mov) to GIF format.
    """
    if output_dir is None:
        output_dir = os.path.dirname(input_file)
    
    if os.path.isdir(input_file):
        for file_name in os.listdir(input_file):
            file_path = os.path.join(input_file, file_name)
            if os.path.isfile(file_path) and file_name.endswith(('.mp4', '.avi', '.mov')):
                output_file = os.path.splitext(file_name)[0] + '.gif'
                output_path = os.path.join(output_dir, output_file)
                convert_file(file_path, output_path)
    else:
        output_file = os.path.splitext(os.path.basename(input_file))[0] + '.gif'
        output_path = os.path.join(output_dir, output_file)
        convert_file(input_file, output_path)

def convert_file(input_path, output_path):
    """
    Helper function to convert a single video file to GIF.
    """
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'fps=30,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse',
        '-loop', '0',
        output_path
    ]
    subprocess.run(command)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python convert_to_gif.py input_file_or_directory [output_directory]')
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    convert_to_gif(input_file, output_dir)
'''
In this modified version, if the input is a directory, 
the output directory will be set to the same directory as 
the input file. If the input is a single file, 
the output directory will be set to the directory 
containing the input file. The output file path is constructed 
using  os.path.join()  to join the output directory and 
the output file name.
'''
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
