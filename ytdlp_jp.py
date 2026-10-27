#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
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
import subprocess
import jaconv
import re

def transliterate_japanese(text):
    """Transliterates Japanese characters to English using jaconv and some cleaning."""
    # Convert kana to romaji
    text = jaconv.kana2alphabet(text)
    #Remove full-width alphabet and numbers
    text = jaconv.z2h(text, kana=False, ascii=True, digit=True)
    # Basic cleaning: remove non-alphanumeric characters and spaces
    text = re.sub(r'[^\sa-zA-Z0-9]+', '', text) #keep spaces to split later
    text = re.sub(' +', ' ', text) #remove extra spaces
    return text.strip()

def download_with_transliterated_filename(url):
    """Downloads a video from YouTube with a transliterated filename."""
    try:
        # Get the video title using yt-dlp's --print title option
        command = ['yt-dlp', '--print', 'title', url]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        title = result.stdout.strip()

        # Transliterate the title
        transliterated_title = transliterate_japanese(title)

        # Sanitize for filename (remove unsafe chars)
        safe_title = "".join(x for x in transliterated_title if x.isalnum() or x in "._- ") # More restrictive than --restrict-filenames, but safer
        # Create the output template
        output_template = f"{safe_title}.%(ext)s"

        # Download the video with the transliterated title
        download_command = ['yt-dlp', '-o', output_template, url]
        subprocess.run(download_command, check=True)

        print(f"Downloaded '{title}' as '{safe_title}'")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    video_url = 'YOUR_YOUTUBE_URL_HERE'  # Replace with the actual YouTube URL
    download_with_transliterated_filename(video_url)


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
