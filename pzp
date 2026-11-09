#!/data/data/com.termux/files/usr/bin/python
import inspect, os, subprocess, sys, time

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

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'

start_time = time.time()

desc = inspect.cleandoc(f'''
    alias:{fgr} pyzipper-wrapper{frs}
 function:{fyl} compress a file, files or directory.
''')
#print(f'{desc}')
    
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
       print(f'symlink creation returns error')
    if os.path.islink(link_path):
        info.append(f"Symbolic link '{link_path}' exists.")
    else:
        info.append(f"Failed to create symbolic link '{link_path}'.")
 
osl()
 
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
    ''')
    print(f'{desc}\n{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
 
#insert_your_codes_here

import argparse
try:
    import pyzipper
except Exception:
    os.system(f'pip install pyzipper')
    import pyzipper
import os

def compress(input_path, output_path, password=None):
    """
    Compresses a file or directory.

    Args:
        input_path: The path to the file or directory to be compressed.
        output_path: The path to the output zip file.
        password: The password to use for the zip file (optional).
    """
    if password:
        encryption = pyzipper.WZ_AES
    else:
        encryption = None 
    with pyzipper.AESZipFile(output_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=encryption) as zip_file:
        if password:
            zip_file.setpassword(password.encode())
        if os.path.isfile(input_path):
            zip_file.write(input_path)
        elif os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for file in files:
                    zip_file.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), input_path))
        else:
            print(f"Invalid input path: {input_path}")

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Compress files or directories")
   parser.add_argument("-p", "--password", help="Password to use for the zip file", required=False)
   parser.add_argument("input", help="File, files, or directory to compress", nargs="+")
   args = parser.parse_args()

   password = args.password
   script_name = os.path.basename(sys.argv[0])
   output_dir = f'/sdcard/{script_name[:-3]}' 
   os.makedirs(output_dir, exist_ok=True)

   for input_path in args.input:
       output_path = os.path.join(output_dir, f'{os.path.splitext(input_path)[0]}.zip')
       compress(input_path, output_path, password)


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
