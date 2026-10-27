#!/data/data/com.termux/files/usr/bin/python
import os, subprocess, sys, time
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
        info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
        info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()

def usg():
    usg = inspect.cleandoc(f'''
    mp4 files merger
    usage: {sne} [argument]
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
# specify your video directory path here
video_folder = f'{exargs()}'

# get all file names in the folder
videos = [vid for vid in os.listdir(video_folder) if vid.endswith(".mp4")]

# sort the videos by name
videos.sort()

# create a list to store the video file paths
video_paths = []

# iterate over the videos and get their file paths
for vid in videos:
    video_path = os.path.join(video_folder, vid)
    video_paths.append(video_path)

# specify the output file name with the last video's name
last_video_name = videos[-1]
output_file = last_video_name.split('.')[0] + '-merged.mp4'
#output_file = last_video_name.split('.')[0] + '-merged.webm'
output_file = os.path.join(video_folder, output_file)
print(f'output_file: {output_file}')

os.system(f'apt update && apt upgrade')
os.system(f'apt install ffmpeg')
# create the ffmpeg command to merge the videos
ffmpeg_command = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'concat.txt',
    '-c:v', 'libx264', '-crf', '21', '-preset', 'veryfast', 
    '-c:a', 'aac', '-b:a', '128k', 
    '-r', '30',  # Specify the desired frame rate here
    output_file
]

disabled_ffmpeg_command = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'concat.txt',
    '-c:v', 'libvpx-vp9', '-crf', '21', '-preset', 'veryfast', 
    '-c:a', 'libopus', '-b:a', '64k', 
    '-r', '30',  # Specify the desired frame rate here
    '-s', '640x360',
    output_file
]

disabled_ffmpeg_command = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'concat.txt',
    '-c:a', 'copy', '-c:v', 'copy',
    output_file
]

# create a temporary text file to store the list of video files
with open('concat.txt', 'w') as f:
    for video_path in video_paths:
        f.write(f"file '{video_path}'\n")

# run the ffmpeg command to merge the videos
subprocess.run(ffmpeg_command)

# remove the temporary text file
os.remove('concat.txt')

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
