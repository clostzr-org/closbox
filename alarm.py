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
hbak  = f'{home}/bak'

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

import datetime
import time
import os

def play_alarm():
    os.system('play-audio alarm_sound.mp3')

alarm_hour = int(input("Enter the hour of the alarm (0-23): "))
alarm_minute = int(input("Enter the minute of the alarm (0-59): "))

while True:
    now = datetime.datetime.now()
    print(f'{fmg}currentTime:{frs} {now}')
    print(f'{fyl}alarmTime  :{frs} {alarm_hour}:{alarm_minute}')
    

    if now.hour == alarm_hour and now.minute == alarm_minute:
        play_alarm()
        time.sleep(60)

    time.sleep(10)

