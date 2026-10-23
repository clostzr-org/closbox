#!/data/data/com.termux/files/usr/bin/python
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if not hbin in sys.path:
   sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if os.path.islink(spath):
   spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import time
start_time = time.time()

import osl; osl.osl(spath)
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
import os
from bs4 import BeautifulSoup
from urllib.parse import quote

import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_pexels_image(search_term, image_folder='images'):
    """
    Scrapes a single image from Pexels based on a search term.

    Args:
        search_term (str): The term to search for on Pexels.
        image_folder (str): The folder to save the image to. Defaults to 'images'.

    Returns:
        str: The file path of the downloaded image, or None if no image was found.
    """
    # Step 1: Create the image folder if it doesn't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Step 2: Construct the search URL
    search_url = f"https://www.pexels.com/search/{quote(search_term)}/"

    try:
        # Step 3: Send a request to the search URL
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Step 4: Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Step 5: Find the first image element
        first_image_element = soup.find('article', {'class': 'photo-item'})
        if not first_image_element:
            print("No images found for the search term.")
            return None

        # Step 6: Extract the image URL
        image_url = first_image_element.find('img')['src']

        # Step 7: Download the image
        image_name = image_url.split('/')[-1].split('?')[0] + '.jpg'  # Adding .jpg extension
        image_path = os.path.join(image_folder, image_name)
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()

        # Step 8: Save the image
        with open(image_path, 'wb') as file:
            for chunk in image_response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image downloaded to: {image_path}")
        return image_path

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    image_path = get_pexels_image(search_term)

    if image_path:
        print(f"Image saved to: {image_path}")
    else:
        print("Failed to download image.")
        
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
