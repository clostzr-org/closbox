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
import json
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

def get_direct_independent_gif(category="dance"):
    """
    Queries the Nekos.best open endpoint to retrieve a raw animation link.
    Available categories include: baka, bite, blush, dance, happy, laugh, pat, poke, smile, wave.
    """
    safe_category = urllib.parse.quote(category.lower())
    api_url = f"https://nekos.best/{safe_category}"
    
    # Safe high-res independent fallback link if offline
    fallback_link = "https://nekos.best/dance/0055.gif"
    
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            payload = json.loads(response.read().decode('utf-8'))
            
            # The API returns an array matching results; extract the direct asset link
            direct_gif_url = payload['results'][0]['url']
            return direct_gif_url
            
    except Exception as network_error:
        print(f"Network drop or unknown category ({network_error}). Serving backup tracking link...")
        return fallback_link

def auto_play_gif():
    # Swap out 'dance' for other actions like 'happy', 'smile', or 'wave'
    direct_link = get_direct_independent_gif(category="dance")
    
    print(f"\nDirect `.gif` Link: {direct_link}")
    print("Launching independent system display engine...")

    try:
        if shutil.which("termux-open"):
            # Native environment intent loader for Termux/Android
            subprocess.run(["termux-open", direct_link], check=True)
        elif sys.platform == "win32":
            # Native Windows terminal handler
            subprocess.run(["start", direct_link], shell=True, check=True)
        elif sys.platform == "darwin":
            # Native macOS shell player
            subprocess.run(["open", direct_link], check=True)
        else:
            # Standard Linux Desktop graphics workspace fallback (xdg-open)
            subprocess.run(["xdg-open", direct_link], check=True)
    except Exception as thread_error:
        print(f"Failed to bind visual context buffer: {thread_error}")

if __name__ == "__main__":
    auto_play_gif()

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
