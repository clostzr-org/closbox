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
try:
   import pytube
except Exception:
   os.system(f'pip install pytube')
   import pytube
import os
import argparse

def browse_playlist(playlist_url):
    """
    Browses a YouTube playlist and displays the available videos.

    Args:
        playlist_url: The URL of the YouTube playlist.

    Returns:
        A list of pytube.Video objects representing the videos in the playlist.
    """
    try:
        playlist = pytube.Playlist(playlist_url)
        print(f"Playlist: {playlist.title}")
        print("------------------------------------")
        videos = []
        for i, video in enumerate(playlist.video_urls):
            try:
                v = pytube.Video(video)
                print(f"{i+1}. {v.title} ({v.length} seconds)")
                videos.append(v)
            except pytube.exceptions.RegexMatchError:
                print(f"Skipping invalid video URL: {video}")
            except Exception as e:
                print(f"Error processing video {video}: {e}")
        return videos
    except pytube.exceptions.RegexMatchError:
        print("Invalid playlist URL.")
        return []
    except Exception as e:
        print(f"Error accessing playlist: {e}")
        return []


def download_video(video, resolution="highest"):
    """
    Downloads a YouTube video.

    Args:
        video: A pytube.Video object.
        resolution: The desired resolution.  "highest" for best available.
    """
    try:
        if resolution == "highest":
            stream = video.streams.get_highest_resolution()
        else:
            try:
                stream = video.streams.filter(res=resolution).first()
                if stream is None:
                    print(f"Resolution {resolution} not available. Downloading highest resolution instead.")
                    stream = video.streams.get_highest_resolution()
            except:
                print(f"Error finding resolution {resolution}. Downloading highest resolution instead.")
                stream = video.streams.get_highest_resolution()

        if stream:
            print(f"Downloading: {video.title} ({stream.resolution})")
            stream.download(output_path=".", filename=video.title)  # Download to current directory
            print("Download complete!")
        else:
            print("No suitable stream found for download.")
    except Exception as e:
        print(f"Error downloading video: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download videos from a YouTube playlist.")
    parser.add_argument("playlist_url", help="The URL of the YouTube playlist.")
    parser.add_argument("-s", "--selection", nargs='+', type=int, help="Specific video numbers to download (e.g., -s 1 3 5)")
    parser.add_argument("-r", "--resolution", default="highest", help="Desired resolution (e.g., 720p, 360p, highest)")
    args = parser.parse_args()

    videos = browse_playlist(args.playlist_url)

    if not videos:
        return

    if args.selection:
        # Download selected videos
        for index in args.selection:
            if 1 <= index <= len(videos):
                download_video(videos[index - 1], args.resolution)
            else:
                print(f"Invalid video number: {index}")
    else:
        # Download all videos in the playlist
        for video in videos:
            download_video(video, args.resolution)


if __name__ == "__main__":
    main()

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
