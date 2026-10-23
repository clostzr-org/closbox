#!/data/data/com.termux/files/usr/bin/python
import colorama, datetime, inspect, json, os
import re, stat, subprocess, sys
from colorama import Fore
fbl = Fore.BLUE
fcy = Fore.CYAN
fgr = Fore.GREEN
flb = Fore.LIGHTBLUE_EX
fmg = Fore.MAGENTA
frd = Fore.RED
frs = Fore.RESET
fyl = Fore.YELLOW
dn00 = os.path.dirname(sys.argv[0])
bn00 = os.path.basename(sys.argv[0])
bn0s = os.path.splitext(bn00)
bs00 = bn0s[0]
db00 = f'{dn00}/{bs00}'
dbC = f'{db00}.csv'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
targetdir = '/data/data/com.termux/files/home/.bookmarks/'

try: import osl
except: pass 

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 os.system(f'cmd {args}')

def bkmls():
 bks = os.listdir(targetdir)
 print(f'__bookmarksdir: {targetdir}')
 for b in bks:
  ort = os.readlink(f'{targetdir}{b}')
  print(f'__{fcy}{b}{frs} -> {fbl}{ort}{frs}')
   
def usg():
 usg = inspect.cleandoc(f'''
How to install

Here is where the magic is. 
Add these 4 lines of code to your bashrc or zshrc file.

if [-d "$HOME/.bookmarks"]; then
    export CDPATH=".:$HOME/.bookmarks:/"
    alias goto="cd -P"
fi

Additionally, 
you need to create the directory in your home folder 
or wherever it suits you, 
just remember to update the CDPATH variable above.

mkdir ~/.bookmarks

How to use

To add a new bookmark, 
you just need to create a symbolic link 
to the folder in your bookmarks directory. 
I suggest you start all the bookmarks with the same character. 
This way, the autocomplete will suggest to you all the bookmarks 
available once you type the character. 
In my case, I chose the symbol @ . 
If you want to edit or remove the bookmark, 
delete the symbolic link and/or create a new one.

ln -s path/to/certain/directory/with/my/project @important-project

 usage: {os.path.basename(sys.argv[0])} <src> <dst>
 ''')
 print(f'{usg}')
 
bkmls()

usg()

acmd = f'(a)dd (e)dit (l)ist (q)uit'
menu = input(f'{acmd}\n__your.command: ')



match menu:
 case 'a':
  src = input(f'source_dir: ')
  try:
   targetlnk = srcbn
  except Exception:
   targetlnk = input('__bookmarkname: ')
  if len(targetlnk) < 1:
   print(f'__bookmarkname.cannot.be.empty')
   sys.exit()
  else:
   opis = os.path.isdir(src)
   if opis == True:
    print(f'__isdir: {src}')
   else:
    print(f'__isnotdir: {src}')
    sys.exit()
   dst = f'{targetdir}@{targetlnk}'
   os.symlink(src, f'{dst}')
 case 'e':
  os.chdir(targetdir)
 case 'l':
  bks = os.listdir(targetdir)
  print(f'__bookmarksdir: {targetdir}')
  for b in bks:
   ort = os.readlink(f'{targetdir}{b}')
   print(f'__{fcy}{b}{frs} -> {fbl}{ort}{frs}')
 case 'q':
  sys.exit()
