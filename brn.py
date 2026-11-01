#!/data/data/com.termux/files/usr/bin/python
import inspect, json, os, subprocess, sys, time

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

verbose = False

home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'

if os.path.islink(sys.argv[0]):
   srcp = os.readlink(sys.argv[0])
   if verbose == True:
      if os.path.isfile(srcp):
         print(f'caller           : {sys.argv[0]}')
         print(f'caller_islink_to : {srcp}')
else:
   srcp = sys.argv[0]
   
sdn   = os.path.dirname(srcp)
sbn   = os.path.basename(srcp)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'

verbose = False
#verbose = True

start_time = time.time()

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    info = []
    home = os.environ['HOME']
    symdir = f'{home}/symlink'
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    print(f'current-caller_path: {source_path}')
    info.append(f'checking symlink status...')
    if not source_path.endswith('.py'):
       info.append(f'perhaps the caller is a symlink')
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
    
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} [dir]
    ''')
    print(f'{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()

if verbose == True:
   print(f'args  :{args}')
   print(f'jargs :{jargs}')

# get the directory, prefix, and suffix from the user
def tcg():
    cmd = 'termux-clipboard-get'
    spr = subprocess.run(
          cmd, 
          stdout=subprocess.PIPE, 
          universal_newlines=True, 
          check=True
          )
    spo = spr.stdout
    print(f'spo: {spo}')
    return spo
    
try:
 arg1 = sys.argv[1]
 if os.path.isdir(arg1):
  directory = arg1
 else:
  if arg1 == 'tcg':
   directory = tcg()
   if os.path.isdir(directory):
    print(f'dir_tcg: {directory}')
   else:
    raise Error
except Exception:
 directory = ''
 
if os.path.isdir(directory):
   pass
else:
   directory = input("Enter the directory path: ")
   if os.path.isdir(directory):
    pass
   else:
    usg()
    sys.exit()

directory = os.path.abspath(directory)
files = os.listdir(directory)
nfo = inspect.cleandoc(f'''
      directory: {directory}
      ''')
print(f'Batch Renamer\n{nfo}')
for f in files:
 f = f'{directory}/{f}'
 bnf = os.path.basename(f)
 if os.path.isdir(f):
  print(f'subdir: {bnf}')
 if os.path.isfile(f):
  print(f'file: {bnf}')

#directory = input("Enter the directory path: ")

prefix = suffix = rep1 = rep2 = ''

rep1 = input('replace_this: ')
rep2 = input('replace_with: ')
prefix = input("Enter the prefix (leave blank for no prefix): ")
suffix = input("Enter the suffix (leave blank for no suffix): ")
# get a list of all files in the directory
files = os.listdir(directory)

# loop through the files and rename them
def batchren():
    changes = {}
    for i, file in enumerate(files):
        print(f'')
        # construct the new filename
        new_filename = ""
        repname = file
        if rep1:
         repname = file.replace(f'{rep1}', '')
         print(f'new_filename_with_rep1: {repname}')
        if rep2:
         repname = file.replace(f'{rep1}', f'{rep2}')
         print(f'new_filename_with_rep2: {repname}')
        if prefix:
            new_filename += prefix + "_"
        new_filename += repname
        nfn = new_filename.replace(prefix, f'{frd}{prefix}{frs}')
        if suffix:
            new_filename = os.path.splitext(repname)[0] + "_" + suffix + os.path.splitext(repname)[1]
        ofn = file
        nfn = new_filename.replace(file, f'{fgr}{file}{frs}')
        if file == nfn:
         pass
        else:
         print(f'{fyl}oldname{frs}: {fgr}{file}{frs}')
         print(f'{fmg}newname{frs}: {nfn}')
         oname = os.path.join(directory, file)
         nname = os.path.join(directory, new_filename)
         changes[oname] = nname
    #print(f'changes:\n{changes}')
    cmd = input('\ntype "ok" or "quit" or leave blank to skip this file. Your command: ')
    if cmd == 'ok':
     for key, value in changes.items():
      print(f'{frd}renaming{frs}\n{key}\n{fgr}to{frs} {value}')
      os.rename(key, value)
    elif cmd == 'quit':
     sys.exit()
        
        # rename the file
        # os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))

batchren()
'''
In this updated script, the user is prompted to enter 
the directory path, prefix, and suffix. 
If the user enters a prefix or suffix, the script constructs 
the new filename by adding the prefix or suffix to the original filename. 
If both a prefix and suffix are specified, 
the script adds the prefix before the filename and 
the suffix after the extension.

For example, if the prefix is  new_  and the suffix is  backup , 
a file named  file.txt  would be renamed to  new_file_backup.txt .

Note that if the user doesn't enter a prefix or suffix, 
the corresponding variables will be empty strings, 
so the script won't add anything to the filenames.
'''
