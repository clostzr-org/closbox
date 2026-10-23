#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv, os
import   datetime,  shutil,   time,  sys
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
 print(f'unable to import osl')
 
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
ajp_flowers_frame = inspect.cleandoc(f'''
a gift card with a frame made of flowers, perfect rectangular shape, gift card style, flowers only, no animal faces, the center part is reserved for words, the borders are made of flowers, no cut, full frame. full screen. no wood, only flowers, a wedding card, tons of flowers, full of flowers at the borders. super realistic flowers.. in 2:3 ratio. symmetric. stretched. fullscreen. white border. centered. the frame is located at the middle.. symmetric border. symmetric frame
''')

ajp_vmp_30yo = inspect.cleandoc(f'''
a super skinny slim anorexia female underworld vampire gothic corset scary serious vile charming mysterious frightening tanktop tight shirt 30 years old attractive intimidating alluring menacing hideous powerful lady antagonist wicked foul straight easygoing friendly cheerful superior warrior
''')

ajp_vmp_40yo = inspect.cleandoc(f'''
a slim skinny anorexia vampire female charming attractive big nipples big thighs black bra adult mature 40 years old dangerous serious cold straight perfect super big thighs
''')

ajp_vmp_50yo = inspect.cleandoc(f'''
a slim skinny anorexia vampire female charming attractive big nipples big thighs black bra adult mature 50 years old dangerous serious cold straight perfect super big thighs very muscular abdomen calm unfriendly confident proud arms crossed brutal wild feral angry scolding
''')

ajp_slim_blackShirt = inspect.cleandoc(f'''
30 years old extreme anorexia slim skinny pale vampire female high ranking officer. extreme slim muscular abdomen. quality long shirt. long coat. quality short skirt. adult charismatic confident gothic harsh serious unfriendly native american.
''')

ajp_wot = inspect.cleandoc(f'''
a skinny slim anorexia supermodel actress pornstar muscular abdomen giant thighs very super beautiful bitch slut pussy fuck charismatic appealing aggressive lust passion desire turned on sexually aroused pheromones estrogen mini nipples. doing a sex scene: riding a perfect giant dick, woman on top, reverse cowgirl style. orgasm
''')

ajp_necklace = inspect.cleandoc(f'''
an ultra slim sexy body builder charismatic attractive seducing arousing female pornstar supermodel with super beautiful face and straight blonde hair standing straight facing the camera viewed from the front wearing a necklace, bracelets on her right hand and left hand and a robe. super wide waist and big thighs.
''')

ajp_teacher = inspect.cleandoc(f'''
an adult confident easygoing nerd female teacher supermodel with attractive charismatic intimidating mature beautiful pretty face. straight hair. thin lips. thinner lip. thinnest lip. slim  super formal long coat feminim long shirt long trouser headmaster professor academic professional consultant
''')

ajp_wot = inspect.cleandoc(f'''
a female supermodel pornstar slut bitch laying on the bed having sex in missionary style. riding a penis. reverse cowgirl style. orgasming. hands laid back. body laid backward. thighs in front view. really sexually aroused. creampie. high libido. lust. full of estrogen. really turned on. muscular abdomen. slim anorexia skinny. over the top view. blonde. high class. elegant. charismatic attractive.
''')

ajp_mma = inspect.cleandoc(f'''
a female mma fighter. 30 years old. standing straight. anorexic skinny slim muscular. black shirt. black shortpant. big thighs. attractive charismstic charming.
''')

ajp_pornstar = inspect.cleandoc(f'''
a female supermodel pornstar slut bitch sexually aroused creampie high libido lust full of estrogen turned on. muscular abdomen. slim anorexia skinny. over the top view. blonde. high class. elegant. charismatic attractive. big labia. vampire. super sexy
''')

ajp_libido = inspect.cleandoc(f'''
a female supermodel brunette vampire pornstar slut bitch sexually aroused creampie high libido lust full of estrogen turned on. sexy muscular abdomen. long gown long coat. skinny slim anorexia
''')

ajp_supermodel = inspect.cleandoc(f'''
slim skinny anorexia supermodel pornstar attractive charismatic scary intimidating lust libido estrogen pheromones vampire mature serious beautiful blonde white hair muscular sexy abdomen
''')

hoodie = inspect.cleandoc(f'''
Generate an image of Natural light, Surrealism, Artistic portrait, a female futuristic soldier wearing slimfit t-shirt with wide neck that showing the cleavage inside, covered by a hoodie sweater jacket, black health masker, post apocalyptic survivor, beautiful eyes, straight hair, indoor, Medium shot.In the style of Movie stills, with 9:16 aspect ratio.
''')

def slctn():
    opts = inspect.cleandoc(f'''
1. vamp30
2. vamp40
''')
    print(f'options:\n{opts}')
    while True:
        prmp = input(f'type your choice: ')
        if prmp == "1" or prmp == "2":
            p = ajp_vmp_30yo
            print(f'selected:\n{prmp}. {p}')
            sys.exit()
        else:
            break
            p = ''
            print(f'your choice: {prmp}. {p}')
            
    
ajpls = [ajp_wot, ajp_teacher]
if __name__ == '__main__':
   for p in ajpls:
       print(f'p: {p}')
   os.system(f'termux-clipboard-set "{ajp_vmp_30yo}" ')
   from tcget import tcget as tcg
   tcg = tcg()
   print(f'termux-clipboard-get:\n{tcg}')
   slctn()
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
