#!/data/data/com.termux/files/usr/bin/python
import ansicolors as anco
import inspect, os, subprocess, sys, time

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'
start_time = time.time()
    
try:
 import osl
 osl.osl(sys.argv[0])
except Exception:
 print(f'{anco.frd}unable to import osl{anco.frs}')

desc = inspect.cleandoc(f'''
    alias:{anco.fgr}youtube_dl_playlist{anco.frs}
 function:{anco.fyl}download a youtube playlist{anco.frs}
''')
print(f'{desc}')

def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [youtube-playlist-link]
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
#!/data/data/com.termux/files/usr/bin/python
import subprocess
import re



def download_playlist(playlist_url):
    command = ['yt-dlp', playlist_url, '--simulate', '-x', '-c', '-i', '-o', '/sdcard/Download/%(playlist)s/%(playlist_index)s_-_%(title)s.%(ext)s', '--geo-bypass', '--geo-bypass-country', 'US', '--restrict-filenames', '-f', 'bestaudio', '--progress']
    print(f'command: {command}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    pl = playlist_url
    file_count = 0
    fc = 0
    fd = 'none'
    st = 'ongoing'
    tnot = subprocess.run(['termux-notification', '--title', 'YouTube Downloader', '--content', f"playlist: {pl}\nfile_count: {fc}\ndestination: {fd}\nstatus: {st}"])
    for line in iter(process.stdout.readline, ''):
        print(f'line: {line}')
        if 'Downloading playlist:' in line:
         pl = line.split('Downloading playlist:')[1]
        if 'Downloading item' in line:
         fc = line.split('Downloading item')[1]
         tnot
        if 'Destination:' in line:
         fd = line.split('Destination:')[1]
        if 'Finished downloading playlist:' in line:
         st = 'finished'
         tnot
    process.wait()

# Usage
#playlist_url = 'https://www.youtube.com/playlist?list=PLAYLIST_ID'
try:
 print(f'args: {sys.argv[1]}')
except Exception:
 usg()
 sys.exit()
 
try:
    playlist_url = f'{sys.argv[1]}'
except Exception:
    print(f'''yt-dlp playlist downloader
usage: {sys.argv[0]} <youtube-playlist-link>''')
    sys.exit()
download_playlist(playlist_url)

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
