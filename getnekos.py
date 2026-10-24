#!/usr/bin/env python3
import time
start_time = time.time()
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if  not hbin in sys.path:
    sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if  os.path.islink(spath):
    spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import osl; osl.osl(spath)
for message in osl.info:
    print(f'{message}')

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr} {frs}
 function: {fyl} {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here
import asyncio
import os
import subprocess
import sys

# Automatically check and install dependencies
try:
    from nekosbest import Client
except ImportError:
    print("nekosbest library not found. Installing dependencies now...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "nekosbest"],
        stdout=subprocess.DEVNULL,
    )
    from nekosbest import Client

# Configuration: Set to an action category that returns an animated .gif
try:
    IMAGE_CATEGORY = sys.argv[1:][0]
except:
    print('It must be one of the following: angry, baka, bite, bleh, blowkiss, blush, bonk, bored, carry, clap, confused, cry, cuddle, dance, facepalm, feed, handhold, handshake, happy, highfive, hug, husbando, kabedon, kick, kiss, kitsune, lappillow, laugh, lurk, neko, nod, nom, nope, nya, pat, peck, poke, pout, punch, run, salute, shake, shocked, shoot, shrug, sip, slap, sleep, smile, smug, spin, stare, tableflip, teehee, think, thumbsup, tickle, waifu, wave, wag, wink, yawn, yeet.')
    IMAGE_CATEGORY = input('image category: ')


def open_in_termux_browser(url: str) -> None:
    """Uses Termux native system tool to launch Android's default browser."""
    os.system(f'termux-open-url "{url}"')


async def main() -> None:
    print(f"Fetching a GIF from category '{IMAGE_CATEGORY}'...")

    try:
        async with Client() as client:
            # Fetch a single asset
            single = await client.get_image(IMAGE_CATEGORY)

            print(f"\n[Success] GIF Link: {single.url}")
            print("Opening link in your default Android browser...")

            # Open the link once without any loops
            open_in_termux_browser(single.url)

    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
