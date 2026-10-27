#!/data/data/com.termux/files/usr/bin/python
import datetime, inspect, json, os
import re, stat, subprocess, sys
def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
        'black':  '\033[30m',        'red':    '\033[31m',
        'green':  '\033[32m',        'yellow': '\033[33m',
        'blue':   '\033[34m',        'magenta':'\033[35m',
        'cyan':   '\033[36m',        'white':  '\033[37m',
        'reset': '\033[0m'
    }

    code = ''
    if reset:
        code = color_codes['reset']
    elif fg:
        code = color_codes.get(fg, '')
    elif bg:
        code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'  # Background code adjustment

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

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'

argc = len(sys.argv)
if argc > 1:
 a1 = sys.argv[1]
else:
 pass
 #a1 = input("_argument: ")
#print("argument1: ", a1) if len(a1) else sys.exit()

'''
raw_input can correctly handle the EOF, 
so we can write a loop, 
read till we have received an EOF (Ctrl-D) from user:
Python 3
'''

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
print(f'contents: {contents}')
