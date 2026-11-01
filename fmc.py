#!/data/data/com.termux/files/usr/bin/python
import inspect, os, subprocess, sys, time
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

dn00 = os.path.dirname(sys.argv[0])
bn00 = os.path.basename(sys.argv[0])
bn0s = os.path.splitext(bn00)
bs00 = bn0s[0]
db00 = f'{dn00}/{bs00}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()
try: import osl
except: pass
 
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

args = sys.argv[1:]
 
#insert_your_codes_here
import os

def fmc(file1, file2):
 if os.path.getmtime(file1) < os.path.getmtime(file2):
  return f"older:{file1}"
 elif os.path.getmtime(file1) > os.path.getmtime(file2):
  return f"older:{file2}"
 else:
  return "same_mtime"

if __name__ == '__main__':
 try:
  print(fmc(sys.argv[1], sys.argv[2]))
 except Exception:
  # Usage
  print(
  f'compare files and show the older one based on mtime\n'
  f'usage: {bs00} file1 file2'
  )

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
