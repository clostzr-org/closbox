#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if  not hbin in sys.path:
    sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if  os.path.islink(spath):
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

args  = sys.argv[1:]
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
import json
import re
import os

def translate_text(text, target_lang="en"):
    """Translate text using translate-shell (trans command)."""
    try:
        # Use translate-shell to translate to target language (default: English)
        result = subprocess.run(
            ["trans", "-b", f":{target_lang}", text],  # -b = brief output (only translation)
            capture_output=True,
            text=True,
            check=True
        )
        translated = result.stdout.strip()
        
        # Sanitize translated text for use as a filename
        sanitized = re.sub(r'[^\w\-_. ]', '', translated)  # Keep safe chars only
        sanitized = re.sub(r'\s+', ' ', sanitized).strip()  # Clean extra spaces
        return sanitized

    except subprocess.CalledProcessError as e:
        print(f"Translation failed for '{text}': {e.stderr}")
        return text  # Fall back to original title if translation fails

def download_playlist_with_translated_titles(playlist_url, target_lang="en", max_size="16M"):
    """
    Download playlist items with translated titles.
    Steps: 1. Fetch playlist metadata 2. Translate each title 3. Download with translated filename
    """
    try:
        # Step 1: Fetch full playlist metadata (JSON format)
        print("Fetching playlist metadata...")
        metadata_result = subprocess.run(
            ["yt-dlp", "--dump-single-json", playlist_url],
            capture_output=True,
            text=True,
            check=True
        )
        playlist_data = json.loads(metadata_result.stdout)
        playlist_title = playlist_data.get("playlist_title", "Untitled_Playlist")
        print(f"Processing playlist: {playlist_title}\n")

        # Create a folder for the playlist (with translated name)
        translated_playlist_folder = translate_text(playlist_title, target_lang)
        os.makedirs(translated_playlist_folder, exist_ok=True)
        print(f"Saving files to: {translated_playlist_folder}\n")

        # Step 2: Process each entry in the playlist
        for idx, entry in enumerate(playlist_data.get("entries", []), start=1):
            video_url = entry["webpage_url"]
            original_title = entry["title"]
            print(f"\n[{idx}/{len(playlist_data['entries'])}] Processing: {original_title}")

            # Translate the title
            translated_title = translate_text(original_title, target_lang)
            print(f"Translated title: {translated_title}")

            # Step 3: Download the video with translated filename
            # Output template: [playlist_folder]/[index]-[translated_title].[ext]
            output_template = os.path.join(
                translated_playlist_folder,
                f"{idx}-{translated_title}.%(ext)s"
            )

            download_cmd = [
                "yt-dlp",
                video_url,
                "-o", output_template,
                "--max-filesize", max_size,  # Skip files larger than 16MB
                "--restrict-filenames",  # Extra sanitization for filenames
                "--ignore-errors"  # Continue if an entry fails
            ]

            print("Starting download...")
            subprocess.run(download_cmd, check=False)  # Don't abort on skips/failures
            print("Download complete (or skipped if oversized).")

        print("\n✅ All entries processed!")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Failed to fetch playlist metadata: {e.stderr}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")

# ------------------- Example Usage -------------------
if __name__ == "__main__":
    PLAYLIST_URL = input("type YOUR_PLAYLIST_URL_HERE ->> ")  # Replace with your playlist URL
    TARGET_LANGUAGE = "en"  # Change to your desired language (e.g., "fr" for French, "es" for Spanish)
    MAX_FILE_SIZE = "16M"  # Skip files larger than 16MB

    download_playlist_with_translated_titles(PLAYLIST_URL, TARGET_LANGUAGE, MAX_FILE_SIZE)



if  __name__ == '__main__':
    try:
      if  sys.argv[1] == '-h':
          usg()
          sys.exit()
    except Exception:
      pass
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
