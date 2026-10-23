#!/data/data/com.termux/files/usr/bin/python
from ansicolors import *

import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import time
start_time = time.time()

import osl; osl.osl(sys.argv[0])
for message in osl.info:
    print(f'{message}')

args = sys.argv[1:]
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
import requests
from bs4 import BeautifulSoup
import re

def get_image_links(query, num_images=10):
    """
    Retrieves image links from a Google search for a given query.

    Args:
        query (str): The search query.
        num_images (int): The number of image links to retrieve (default: 10).

    Returns:
        list: A list of image URLs.  Returns an empty list if no images are found
              or if an error occurs.
    """
    image_links = []
    try:
        # 1. Prepare the search query
        search_query = f"https://www.google.com/search?q={query}&tbm=isch"  # tbm=isch specifies image search
        print(f"Searching Google Images for: {query}")

        # 2. Send the request (with User-Agent to avoid bot detection)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(search_query, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # 3. Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # 4. Extract image links
        # Google's image links are often embedded in script tags within the HTML.
        # This part is the most subject to change.
        for img in soup.find_all("img"):
            img_url = img.get("src")
            if img_url and img_url.startswith("http"): #or img_url.startswith("data:image"):
                image_links.append(img_url)

        image_links = image_links[:num_images]  #Limit to the requested number of images

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return image_links


if __name__ == '__main__':
    try:
       search_term = sys.argv[1]
    except Exception:
       search_term = input(f'search term: ')
    if len(search_term) == 0:
       sys.exit()
    num_images_to_fetch = 4
    links = get_image_links(search_term, num_images_to_fetch)

    if links:
       ln1, ln2, ln3, ln4 = links
       print(f'url1:{ln1}\n\nurl2:{ln2}\n\nurl3:{ln3}\n\nurl4:{ln4}')
       print(f"\nFound {len(links)} image links:")
       for link in links:
           print(f'{frd}url:{frs}{link}')
           #os.system(f'termux-open "{link}"')
    else:
       print("No image links found.")

if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
