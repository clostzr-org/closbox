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

def usg():
    print(f'usage: {sne} [remote-dir]')

if len(args) < 1:
 usg()
 sys.exit()
 
#insert_your_codes_here
import subprocess

# Ask the user for a remote path
try:
   remote_path = sys.argv[1]
except Exception:
   remote_path = input("Enter the remote path: ")

# Use rclone to list the contents of the remote path
list_command = f"rclone lsf {remote_path}"
list_output = subprocess.check_output(list_command.split(), text=True).splitlines()
print(f'list_output:\n{list_output}')

# Display the contents of the remote path
fcount = fnum = 0
print("Contents of the remote path:")
for item in list_output:
    fcount += 1
    fnum = str(fcount)
    while len(str(fnum)) < 4:
          fnum = '0' + str(fnum)
    print(f'{fnum}: {item}')

# Replace white spaces with underscores in file and directory names
for item in list_output:
    new_name = item.replace(" ", "_")
    if item != new_name:
       print(f'current file: {item}')
       rename_command = f'rclone moveto "{remote_path}/{item}" {remote_path}/{new_name}'
       subprocess.run(rename_command.split(), capture_output=True, text=True)

# Display the updated contents after replacing white spaces
updated_list_command = f"rclone lsf {remote_path}"
updated_list_output = subprocess.check_output(updated_list_command.split()).decode('utf-8').splitlines()

fcount = fnum = 0
print("\nUpdated contents of the remote path:")
for item in updated_list_output:
    fcount += 1
    fnum = str(fcount)
    while len(str(fnum)) < 4:
          fnum = '0' + str(fnum)
    print(f'{fnum}: {item}')

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
   