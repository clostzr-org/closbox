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
hbak  = home + '/bak'
hbin  = home + '/bin'

start_time = time.time()

desc = inspect.cleandoc(f'''
    alias:{fgr} {frs}
 function:{fyl} {frs}
''')
print(f'{desc}')
    
try:
 import osl
except Exception:
 print(f'{frd}unable to import osl{frs}')
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
    ''')
    print(f'{usg}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()
 
#insert_your_codes_here
#!/data/data/com.termux/files/usr/bin/python
import shutil
import subprocess
import sys

def get_and_view_random_image(keyword="nature"):
    # 1. Construct the alternative LoremFlickr endpoint URL
    # Format: ://loremflickr.com
    image_url = f"https://loremflickr.com/320/240/{keyword}"
    
    print(f"Targeting Image Endpoint: {image_url}")
    print("Fetching and opening random image...")

    # 2. Automatically launch your default terminal image viewer or web browser
    try:
        if shutil.which("termux-open"):
            # Native Android handler for Termux environments
            subprocess.run(["termux-open", image_url], check=True)
        elif sys.platform == "win32":
            # Native Windows terminal handler
            subprocess.run(["start", image_url], shell=True, check=True)
        elif sys.platform == "darwin":
            # Native macOS terminal handler
            subprocess.run(["open", image_url], check=True)
        else:
            # Standard Linux Desktop environment fallback
            subprocess.run(["xdg-open", image_url], check=True)
    except Exception as e:
        print(f"Could not initialize system viewer. Error details: {e}")

if __name__ == "__main__":
    # You can change 'nature' to 'abstract', 'city', 'space', etc.
    get_and_view_random_image(keyword="wallpaper")

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
