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
try:
       import jaconv
except Exception:
       os.system(f'pip install jaconv')
       import jaconv
import re
import shutil

os.system(f'pip install yt-dlp')
os.system(f'apt install translate-shell')

def xsd_df():
    import subprocess
    # Run the df command to get disk space information
    df_process   = subprocess.Popen(["df"], stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(["grep", "-E", "/storage/*-*"], stdin=df_process.stdout, stdout=subprocess.PIPE)
    awk_process  = subprocess.Popen(["awk", "{print $6}"], stdin=grep_process.stdout, stdout=subprocess.PIPE)
    dfx = awk_process.communicate()[0].decode().split()
    xsd = None
    for d in dfx:
        if "-" in d:
           xsd = d
    return xsd

def transliterate_japanese(text):
    """Transliterates Japanese characters to English using translate-shell."""
    try:
        result = subprocess.run(['trans', '-brief', ':en', text], capture_output=True, text=True, check=True)
        transliterated_text = result.stdout.strip()
        print(f'trans output: {transliterated_text}')
        # Basic cleaning: remove non-alphanumeric characters and spaces
        transliterated_text = re.sub(r'[^\sa-zA-Z0-9]+', '', transliterated_text) #keep spaces to split later
        transliterated_text = re.sub(' +', ' ', transliterated_text) #remove extra spaces

        return transliterated_text
    except subprocess.CalledProcessError as e:
        print(f"Error during transliteration: {e}")
        return text  # Return original text on error
    except FileNotFoundError:
        print("Error: translate-shell (trans) not found. Please install it.")
        return text

def download_with_transliterated_filename(url):
    print(f'current url: {url  }')
    xsd = xsd_df()
    xsdm = f'{xsd}/Music'
    os.makedirs(xsdm, exist_ok=True)  # Create the directory if it doesn't exist

    """Downloads a video or playlist from YouTube with transliterated filenames."""
    try:
        # Define the transliteration command as a string
        transliterate_command = """
import sys, subprocess, re
initial_filename = sys.argv[1]
print(f'initial filename: {initial_filename}')
new_filename = sys.argv[2]
print(f'new filename: {new_filename}')
input(f'press Enter'); sys.exit()
try:
    title = initial_filename.split('.')[0]
    ext = initial_filename.split('.')[1]
except IndexError:
    title = initial_filename
    ext = ''
transliterated_title = transliterate_japanese(title)
safe_title = ''.join(x for x in transliterated_title if x.isalnum() or x in '._- ')
if ext:
    new_name = f'{safe_title}.{ext}'
else:
    new_name = safe_title
print(f'new name: {new_name}')
input(f'press Enter')
#subprocess.run(['mv', '-v', new_filename, new_name], text=True)
        """
        # Sanitize for filename (remove unsafe chars)
        # output_template = f"%(title)s.%(ext)s" #Initial filename
        # transliterated_title = transliterate_japanese(output_template)
        output_template = r"%(title)s.%(ext)s" #Keep the standard title to be transliterated during execution
        download_command = ['yt-dlp', '-c', '--js-runtimes', 'node', '--max-filesize', '16m', '-x',
                            '--output', f'{xsdm}/%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s', '--no-overwrites',
                            '--exec', f'python -c "{transliterate_command}" "%(title)s.%(ext)s" "%(filepath)s"', #pass the initial filename
                            '--print', 'playlist_title',
                            '--print', 'title',
                           url
                           ]
        subprocess.run(download_command, text=True)
        
        output_dir = f'{xsdm}'

        print(f"Downloaded playlist/video with transliterated filenames to {output_dir}.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    try: 
       arg1 = jargs
    except Exception:
       arg1 = input(f'youtube playlist url: ')
    playlist_url = arg1  # Replace with the actual YouTube playlist URL
    download_with_transliterated_filename(playlist_url)

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