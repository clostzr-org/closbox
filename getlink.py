#!/data/data/com.termux/files/usr/bin/python
from ansicolors import *
import os, sys, time, inspect
sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
verbose = False
start_time = time.time()

import osl; osl.osl(sys.argv[0])
for message in osl.info:
    print(f'{message}')
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sne} [website] [search_term] 
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]

try:
    import requests
except Exception:
	os.system(f'pip install requests')
	import requests
try:
   from bs4 import BeautifulSoup
except Exception:
   os.system(f'pip install bs4')
   from bs4 import BeautifulSoup
import random
    
#insert_your_codes_here
def gifbin(*args):
    pttr = 'dance'
    for arg in args:
     if arg == '':
      pttr = 'dance'
     else:
      pttr = arg
      break
    print(f'pttr: {pttr}')
    directory_url = f'https://gifbin.com/search/{pttr}/'
    print(f'durl: {directory_url}')
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("img")
    print(f'links: {links}')
    srcl = []
    for link in links:
     print(f'link: {fgr}{link}{frs}')
     href = link.get("src")
     print(f'href: {fbl}{href}')
     if href == None:
      continue
     if not href.endswith(f'.gif'):
      continue
     lnk = f'https://gifbin.com{href}'
     lnkd = os.path.dirname(lnk)
     lnkb = os.path.basename(lnk).split('tn_')[1]
     lnk = f'{lnkd}/{lnkb}'.replace('.gif', '.webm')
     lnk = f'{lnkd}/{lnkb}'.replace('.gif', '.gif')
     print(f'lnk: {fmg}{lnk}')
     srcl.append(lnk)
     return srcl
     
def gifdb(*args):
    pttr = 'dance'
    for arg in args:
     if arg == '':
      pttr = 'dance'
     else:
      pttr = arg
      break
    print(f'pttr: {pttr}')
    directory_url = f'https://gifdb.com/search/{pttr}'
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("img")
    print(f'links: {links}')
    srcl = []
    for link in links:
     href = link.get("src")
     print(f'href: {href}')
     if href == None:
      continue
     if not href.endswith(f'.gif'):
      continue
     lnk = f'https://gifdb.com{href}'
     print(f'lnk: {lnk}')
     srcl.append(lnk)
     return srcl
    
def giphy(*args):
    pttr = 'dance'
    for arg in args:
     if arg == '':
      pttr = 'dance'
     else:
      pttr = arg
      break
    print(f'{fyl}gif search term: "{fgr}{pttr}{frs}"')
    directory_url = f"https://giphy.com/search/{pttr}"
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gif_links = []
    for item in soup.find_all('img'):  # Target the divs with class 'giphy-embed'
        print(f'{frd}item: {item}')
        data_source = item.get('src') # Get the iframe's src attribute
        print(f'{fyl}data_source: {data_source}')
        if '?cid=' in data_source:
            gif_id = data_source.split('?cid=')[0]  # Extract the GIF ID
            base_gif_url = f"{gif_id}"  # Construct the base GIF URL
            gif_links.append(base_gif_url)
        else:
            gif_links.append(data_source)
    return gif_links
    
import requests
from bs4 import BeautifulSoup

def vecteezy(*args):
    for arg in args:
        if len(arg) > 2:
            pttr = arg
            break
    print(f'search term: {pttr}')
    directory_url = f"https://www.vecteezy.com/free-photos/{pttr}"
    print(f'directory_url: {directory_url}')

    # Add User-Agent header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(directory_url, headers=headers)

    print(f'response: {response}')
    soup = BeautifulSoup(response.content, "html.parser")
    print(f'soup: {soup}')
    links = soup.find_all("img")
    print(f'links:{fyl}{links}{frs}')

    def phref():
        for link in links:
            print(f'{fmg}link:{frs}{link}{frs}')
            href = link.get("src")
            if href == 'None':
               continue
            print(f'{fbl}href:{frs}{href}')
    phref()

    divs = soup.find_all("img")
    src_ls = []
    for div in divs:
        src = div.get("src")
        src_ls.append(src)
    return src_ls
    
def vecteezy(*args):
    for arg in args:
        if len(arg) > 2:
            pttr = arg
            break
    print(f'search term: {pttr}')
    directory_url = f"https://www.freeimages.com/search?keyword={pttr}"
    print(f'directory_url: {directory_url}')

    # Add User-Agent header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(directory_url, headers=headers)

    print(f'response: {response}')
    soup = BeautifulSoup(response.content, "html.parser")
    print(f'soup: {soup}')
    links = soup.find_all("img")
    print(f'links:{fyl}{links}{frs}')

    def phref():
        the_links = []
        for link in links:
            print(f'{fmg}link:{frs}{link}{frs}')
            try:
               alt = link.get("alt").lower()
            except Exception:
               continue
            print(f'{fgr}alt:{frs}{alt}')
            if not pttr in alt:
               print(f'{pttr} {fyl}not found in{frs} {alt}')
               continue
            href = link.get("src")
            if href == 'None' or href == '':
               continue
            if str(href).endswith('.svg'):
               continue
            if str(href).startswith('http') and not href.endswith('.jpg'):
               href = href.rsplit('?', 1)[0]
               print(f'{fyl}splitting the href...{frs}')
            print(f'{fbl}href:{frs}{href}')
            if not str(href).endswith('.jpg'):
               continue
            try:
               if len(href):
                  the_links.append(href)
            except Exception:
               continue
        return the_links
    #phref()
    src_ls = phref()
    return src_ls

def tenor(*args):
    for arg in args:
     if len(arg) > 2:
      pttr = arg
      break
    print(f'search term: {pttr}')
    directory_url = "https://tenor.com/search/{pttr}"
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("div", class_="Gif")
    def phref():
     for link in links:
         href = link.get("href")
         print(href)
    divs = soup.find_all("div", class_="Gif")
    src_ls = []
    for div in divs:
        img = div.find("img")
        src = img.get("src")
        src_ls.append(src)
    return src_ls
    
def unsplash(*args):
    for arg in args:
     if len(arg) > 2:
      pttr = arg
      break
    print(f'{fmg}wallpaper search term: "{fgr}{pttr}{fyl}"')
    directory_url = f'https://unsplash.com/s/photos/{pttr}'
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f'directory_url:\n{directory_url}')
    links = soup.find_all("img")
    srcl = []
    for link in links:
     href = link.get("src")
     if href == None:
      continue
     if 'unsplash.com/profile-' in href:
      continue
     if href.startswith('http'):
      lnk = f'{href}'
      srcl.append(lnk)
    return srcl
     
def whcc(*args):
    for arg in args:
     if len(arg) > 2:
      pttr = arg
      break
    print(f'{fmg}wallpaper search term: "{fgr}{pttr}{fyl}"')
    directory_url = f'https://wallhaven.cc/search?q={pttr}'
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    #print(f'{fyl}dir_url:{frs}\n{fgr}{directory_url}')
    links = soup.find_all("a")
    #print(f'links: {links}')
    srcl = []
    for link in links:
     href = link.get("href")
     if href == None:
      continue
     if 'wallhaven.cc/w/' in href:
      fln = f'https://w.wallhaven.cc/full/4v/wallhaven-4vgql5.jpg'
      bln = f'{href}'.split('w/')[1]
      bl2 = bln[:2]
      lnk = f'https://w.wallhaven.cc/full/{bl2}/wallhaven-{bln}.jpg'
      if verbose == True:
         print(
         f'baseLink: {bln}\n'
         f'bl2     : {bl2}\n'
         f'lnk     : {lnk}'
         )
      srcl.append(lnk)
    return srcl
     
def wpfl(*args):
    for arg in args:
     if len(arg) > 2:
      pttr = arg
      break
    print(f'{fmg}wallpaper search term: "{fgr}{pttr}{fyl}"')
    directory_url = f'https://wallpaperflare.com/search?wallpaper={pttr}'
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f'{fyl}directory_url:{frs}\n{fgr}{directory_url}')
    links = soup.find_all("img")
    print(f'links: {links}')
    srcl = []
    for link in links:
     href = link.get("data-src")
     print(f'href: {href}')
     if href == None:
      continue
     lnk = f'{href}'
     print(f'lnk: {lnk}')
     srcl.append(lnk)
    return srcl
     
def wpcm(*args):
    for arg in args:
     if len(arg) > 2:
      pttr = arg
      break
    print(f'{fmg}wallpaper search term: "{fgr}{pttr}{fyl}"')
    directory_url = f'https://wallpapers.com/search/{pttr}'
    response = requests.get(directory_url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f'{fyl}dir_url:{frs}\n{fgr}{directory_url}')
    links = soup.find_all("img")
    srcl = []
    for link in links:
     href = link.get("data-src")
     if href == None:
      continue
     lnk = f'https://wallpapers.com{href}'
     srcl.append(lnk)
    return srcl
     
def randomlink(links):
    random_link = random.choice(links)
    print(f'{fmg}random.choice_link:\n{fgr}{random_link}')
    return random_link
    
sites_info = inspect.cleandoc(f'''
gfbn) gifbin
gfdb) gifdb
gphy) giphy
tenr) tenor
unsp) unsplash
whcc) wallhaven.cc
wpfl) wallpaperflare.com
wpcm) wallpapers.com
''')
sites = {
'gfbn' : gifbin,
'gfdb' : gifdb,
'gphy' : giphy,
'tenr' : tenor,
'unsp' : unsplash,
'vctz' : vecteezy,
'wpfl' : wpfl,
'whcc' : whcc,
'wpcm' : wpcm
}
websites = ['gfbn','gfdb','gphy','pxby','tenr','unsp','vctz','wpfl','whcc','wpcm']
def random_website():
    randweb = random.choice(websites)
    return randweb

def get_link(website, search_term):
    if website in sites:
       webs = website
    else:
       webs = random_website()
       print(f'random_website: {webs}')
    site = sites.get(unsp, 'unsp')
    if not len(search_term) == 0:
       searcht = search_term
    links = site(searcht)
    try:
       chosenlink = randomlink(links)
    except Exception:
       chosenlink = ''
    return chosenlink
    
if __name__ == '__main__':
   print(f'sites:\n{str(sites).replace(',', '\n')}')
   print(f'sites_info:\n{sites_info}')
   usg()
   try:
    arg0 = args[0]
    #arg0 = 'pxby'
   except Exception:
    arg0 = random_website()
   if not arg0 in websites:
      arg0 = random_website()
   try:
    arg1 = args[1]
   except Exception:
    arg1 = 'black%20futuristic'
   site = sites.get(arg0, 'unsp')
   pttr = arg1
   print(f'{fyl}website{frs}: {site}\n{fgr}pattern{frs}: "{pttr}"')
   links = site(pttr)
   try:
      chosenlink = randomlink(links)
   except Exception:
      chosenlink = ''
   print(f'random_link: {chosenlink}')
   os.system(f'termux-open "{chosenlink}"')
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
  