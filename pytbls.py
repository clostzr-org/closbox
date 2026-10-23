#!/data/data/com.termux/files/usr/bin/python

def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
    'black':'\033[30m', 'red'    :'\033[31m',
    'green':'\033[32m', 'yellow' :'\033[33m',
    'blue' :'\033[34m', 'magenta':'\033[35m',
    'cyan' :'\033[36m', 'white'  :'\033[37m',
    'reset':'\033[0m'
    }
    code = ''
    if reset:
       code = color_codes['reset']
    elif fg:
       code = color_codes.get(fg, '')
    elif bg:
       code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'
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

import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'

import time
start_time = time.time()

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    info = []
    home = os.environ['HOME']
    symdir = f'{home}/symlink'
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    if not source_path.endswith('.py'):
       return
    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = f'{symdir}/{lpbn}'
    if not os.path.isdir(symdir):
       os.mkdir(symdir)
    if os.path.exists(link_path):
       if not os.path.islink(link_path):
            os.remove(link_path)
    try:
       os.symlink(source_path, link_path)
    except Exception:
       pass
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' exists.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()

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

import os
import subprocess
import re
from pytube import Playlist

def get_playlist_videos(playlist_url):
    """Fetches video information from a YouTube playlist."""
    try:
        playlist = Playlist(playlist_url)
        playlist.populate() # This is the correct method now
        return [video.watch_url for video in playlist.videos]  #Extract URLs
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []

def display_playlist(videos):
    """Displays the playlist with options to select videos."""
    print("\nSelect videos to download:")
    for i, video in enumerate(videos):
        title = extract_title_from_url(video)
        print(f"{i+1}. {title}")
    return videos


def extract_title_from_url(url):
    """Extracts video title from URL using regular expressions and yt-dlp."""
    match = re.search(r"v=(.+?)&", url) or re.search(r"v=(.+)", url)
    if match:
        video_id = match.group(1)
        try:
            output = subprocess.check_output(["yt-dlp", "-j", "--no-warnings", f'https://www.youtube.com/watch?v={video_id}']).decode()
            data = eval(output)  #Parse JSON
            return data["title"]
        except Exception as e:
            print(f"Error extracting title: {e}")
            return f"Title extraction failed for {url}"
    else:
        return "Invalid Video URL"



def download_video(video_url, output_dir="."):
    """Downloads a single video using yt-dlp."""
    try:
        title = extract_title_from_url(video_url)
        print(f"Downloading: {title}")
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", f"{output_dir}/%(title)s.%(ext)s", video_url], check=True)
        print("Download complete.")
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_user_selection(videos):
    """Gets video selections from the user."""
    while True:
        try:
            choice = input("Enter the number(s) of the video(s) to download (comma-separated for multiple, or 'a' for all), or 'q' to quit: ")
            if choice.lower() == 'q':
                return []
            if choice.lower() == 'a':
                return videos
            selected_indices = [int(x.strip()) - 1 for x in choice.split(',')]
            # Validate that indices are within the range
            if all(0 <= i < len(videos) for i in selected_indices):
                return [videos[i] for i in selected_indices]
            else:
                print("Invalid selection. Please enter numbers within the valid range.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas or 'a' or 'q'.")


if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    videos = get_playlist_videos(playlist_url)

    if videos:
        videos = display_playlist(videos)
        selected_videos = get_user_selection(videos)

        if selected_videos:
            os.makedirs("downloads", exist_ok=True)
            for url in selected_videos:
                download_video(url, output_dir="./downloads")

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
