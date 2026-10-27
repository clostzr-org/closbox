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

start_time = time.time()

desc = inspect.cleandoc(f'''
    alias:{fgr}{frs}
 function:{fyl}
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

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    if args == sys.argv[0]:
       args = ''
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
try:
 import goslate
except Exception:
 os.system(f'pip install goslate')
 import goslate

def translate_japanese(japanese_text):
    """Translates Japanese text to Romanji and English."""

    gs = goslate.Goslate()

    # Translate to Romanji
    romanji_text = gs.translate(japanese_text, 'ja-r')

    # Translate to English
    english_text = gs.translate(japanese_text, 'en')

    return romanji_text, english_text

# Example usage
japanese_text = "こんにちは" 
japanese_text = input(f'japanese text: ')

romanji, english = translate_japanese(japanese_text)

print(f"Japanese: {japanese_text}")
print(f"Romanji: {romanji}")
print(f"English: {english}")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
