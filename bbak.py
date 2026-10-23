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

try: import osl
except: pass 
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} [argument]
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
#Here's a shorter version of your code:
import subprocess
import os

def get_android_property(property_name):
    command = ['getprop', property_name]
    try:
        result = subprocess.check_output(command).decode('utf-8').strip()
        return result
    except subprocess.CalledProcessError:
        return None

def choice(file):
    if os.path.isfile(file):
        bnf = os.path.basename(file)
        fstat = f'{bnf} exists.'
        cho = input(f'{fstat} overwrite? (y/n): ')
        if cho == 'y':
            return True

def backup_partition(partition_name, output_file):
    print(f'Backing up {partition_name}...')
    cmd = ['su', '-c', 'dd',
           f'if=/dev/block/by-name/{partition_name}',
           f'of={output_file}'
          ]
    run = subprocess.check_output(cmd)
    out = run.decode()
    print(f'Output: {out}')

crd_bv = get_android_property('ro.crdroid.build.version')
slot_sfx = get_android_property('ro.boot.slot_suffix')
bakdir = f'/sdcard/{crd_bv}'

if not 'crDroidAndroid' in crd_bv:
    print('Current ROM is not a crDroid. Exiting...')
    sys.exit()

if __name__ == '__main__':
    if not os.path.isdir(bakdir):
        os.makedirs(bakdir)
        backup_partition(f'boot{slot_sfx}', f'{bakdir}/boot.img')
        backup_partition(f'dtbo{slot_sfx}', f'{bakdir}/dtbo.img')
        sys.exit()

    ifb = os.path.isfile(f'{bakdir}/boot.img')
    ifd = os.path.isfile(f'{bakdir}/boot.img')

    if not ifb or not ifd:
        backup_partition(f'boot{slot_sfx}', f'{bakdir}/boot.img')
        backup_partition(f'dtbo{slot_sfx}', f'{bakdir}/dtbo.img')
        sys.exit()

    if choice(f'{bakdir}/boot.img') == True:
        backup_partition(f'boot{slot_sfx}', f'{bakdir}/boot.img')

    if choice(f'{bakdir}/dtbo.img') == True:
        backup_partition(f'dtbo{slot_sfx}', f'{bakdir}/dtbo.img')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

#I removed unnecessary imports, optimized the backup function, and 
#made some other minor improvements. Let me know if you have any questions!

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
