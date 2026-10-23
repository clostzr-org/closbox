#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
import   requests,  random, socket, glob
from bs4 import BeautifulSoup
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
start_time = time.time()
    
try:
 import osl
except Exception:
 print(f'{frd}unable to import osl{frs}')
 
if os.path.exists(sdbne) and os.path.islink(sdbne):
 print(f'{fbl}islink{frs}: {sne}')
 pass
elif os.path.exists(sdbne) and not os.path.islink(sdbne):
 print(f'{frd}isnotlink{frs}: {sne}')
 os.remove(sdbne)
 os.symlink(__file__, sdbne)
else:
 os.symlink(__file__, sdbne)
 print(f'{fgr}created symlink{frs}: {sdbne}')
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [html-file]
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    if args == sys.argv[0]:
       args = ''
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
subprocess.run(['apt', 'install', 'pango'])
try:
 import weasyprint
except Exception:
 cmd = 'pip install weasyprint'
 subrun = subprocess.run(cmd.split(), stdout=subprocess.PIPE, universal_newlines=True, check=True)
 print(f'{subrun.stdout}')
 import weasyprint

html_file = f'{exargs()}'  # Replace with your HTML file path
htmf_bn = os.path.basename(html_file)
pdf_file = f'/sdcard/{htmf_bn}.pdf'  # Replace with your desired PDF file path

try:
    weasyprint.HTML(string=open(html_file, 'r').read()).write_pdf(pdf_file)
    print(f"HTML file '{html_file}' converted to PDF '{pdf_file}' successfully.")
except Exception as e:
    print(f"Error converting HTML to PDF: {e}")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
