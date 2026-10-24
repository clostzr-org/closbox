#!/usr/bin/env python3
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
import asyncio
import subprocess
import sys

# Automatically check and install dependencies
try:
    from nekosbest import Client
except ImportError:
    print("nekosbest library not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nekosbest"])
    from nekosbest import Client

# Configuration Constants
AUTOPLAY_INTERVAL = 3.0  # Time delay in seconds between auto-play loops
IMAGE_CATEGORY = "neko"  # Category to fetch


async def main() -> None:
    print(
        f"Starting Auto-Play loop for category '{IMAGE_CATEGORY}' (Interval: {AUTOPLAY_INTERVAL}s)..."
    )
    print("Press Ctrl+C to stop.\n" + "=" * 50)

    try:
        # Use an async context manager to safely open/close the client session
        async with Client() as client:
            while True:
                # Fetch a single image in the loop
                single = await client.get_image(IMAGE_CATEGORY)
                print(f"[Auto-Play Log]: New Image -> {single.url}")

                # Non-blocking pause before pulling the next image
                await asyncio.sleep(AUTOPLAY_INTERVAL)

    except asyncio.CancelledError:
        print("\nAuto-Play loop gracefully paused.")
    except Exception as e:
        print(f"\nAn error occurred during playback: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nAuto-Play stopped by user. Goodbye!")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
