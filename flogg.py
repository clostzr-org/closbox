#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK; brd = Back.RED
bgr = Back.GREEN; byl = Back.YELLOW
bbl = Back.BLUE; bmg = Back.MAGENTA
bcy = Back.CYAN; bwh = Back.WHITE
fbk = Fore.BLACK; frd = Fore.RED
fgr = Fore.GREEN; fyl = Fore.YELLOW
fbl = Fore.BLUE; fmg = Fore.MAGENTA
fcy = Fore.CYAN; fwh = Fore.WHITE
frs = Fore.RESET
stdm = Style.DIM; stnr = Style.NORMAL
stbr = Style.BRIGHT; stra = Style.RESET_ALL
sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()

try: import osl
except: pass 
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} <argument>
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
 
#insert_your_codes_here
import requests
from bs4 import BeautifulSoup

url = "https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/snd_links.html"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <a> tags that contain audio links
audio_links = soup.find_all("a")

# Extract the href attribute from each <a> tag, if it exists
audio_urls = [link["href"] if "href" in link.attrs else "" for link in audio_links]

# Filter out empty audio URLs
audio_urls = [url for url in audio_urls if url]

# Print the audio links
for audio_url in audio_urls:
    print(audio_url)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
