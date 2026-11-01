#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, subprocess
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
hsym  = home + '/symlink'

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
       print(f'failed to create a symlink')
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
       
osl()

args = sys.argv[1:]
jargs = ' '.join(args).strip()

#insert_your_codes_here

import os
import subprocess

def get_script_name(script_path):
    """Returns the script name without the extension."""
    return os.path.splitext(os.path.basename(script_path))[0]

def get_script_dir(script_path):
    """Returns the directory containing the script."""
    return os.path.dirname(script_path)
    
def xsd_df():
    import subprocess
    # Run the df command to get disk space information
    df_process = subprocess.Popen(["df"], stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(["grep", "-E", "/storage/*-*"], stdin=df_process.stdout, stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(["awk", "{print $6}"], stdin=grep_process.stdout, stdout=subprocess.PIPE)
    dfx = awk_process.communicate()[0].decode().split()
    xsd = None
    for d in dfx:
        if "-" in d:
           xsd = d
    return xsd
    
def main():
    script_path = sys.argv[0]  # Get the path to the current script
    script_name = get_script_name(script_path)
    script_dir = get_script_dir(script_path)

    xsd = xsd_df()

    print(f"extsd: {xsd_df()}")
    print(f"textname: {script_name}.txt")

    # Create the config file with the content you specified
    config_file_path = f"{script_name}.txt"
    with open(config_file_path, "w") as config_file:
        config_file.write(f"--js-runtimes node -c -i -o {xsd}/Music/%(playlist_title)s/%(title)s.%(ext)s --geo-bypass --geo-bypass-country US --restrict-filenames\n")

    # Execute yt-dlp with the config file and arguments
    yt_dlp_args = [
        "yt-dlp", 
        "--config-location", 
        config_file_path
    ] + sys.argv[1:]  # Append additional arguments
    subprocess.run(yt_dlp_args)

    # Remove the temporary config file
    # os.remove(config_file_path)

if __name__ == "__main__":
    main()


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
