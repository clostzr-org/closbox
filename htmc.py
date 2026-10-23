#!/data/data/com.termux/files/usr/bin/python
import csv, datetime, fnmatch, inspect, json
import os, re, shutil, stat, string
import subprocess, sys, time, colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK; brd = Back.RED
bgr = Back.GREEN; byl = Back.YELLOW
bbl = Back.BLUE; bmg = Back.MAGENTA
bcy = Back.CYAN; bwh = Back.WHITE
fbk = Fore.BLACK; frd = Fore.RED
fgr = Fore.GREEN; fyl = Fore.YELLOW
fbl = Fore.BLUE; fmg = Fore.MAGENTA
fcy = Fore.CYAN; fwh = Fore.WHITE
frs = Fore.RESET
stdm = Style.DIM; stnr = Style.NORMAL
stbr = Style.BRIGHT; stra = Style.RESET_ALL
dn00 = os.path.dirname(sys.argv[0])
bn00 = os.path.basename(sys.argv[0])
bn0s = os.path.splitext(bn00)
bs00 = bn0s[0]
db00 = f'{dn00}/{bs00}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
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

args = sys.argv[1:]
 
#insert_your_codes_here
import webbrowser
import tempfile

# Define some HTML content
#html_content = "<h1>Hello, world!</h1>"
html_content = exargs()

# Create a temporary file and write the HTML content to it
with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
    url = 'file://' + f.name
    f.write(html_content)

# Open the temporary file in the web browser
webbrowser.open(url)
 
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
