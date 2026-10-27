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

desc = inspect.cleandoc(f'''
    alias:{anco.fgr}youtube_search{anco.frs}
 function:{anco.fyl}search sumthin in youtube{anco.frs}
''')
print(f'{desc}')
    
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
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [argument]
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
import subprocess

def search_youtube(query):
    """Launches YouTube app with a search query.

    Args:
        query: The search query string.  Should be URL-encoded for safety.
    """

    # Construct the am start command.  Note the URL encoding of the query.
    # We use the official YouTube search URL to ensure reliability.
    command = [
        "am",
        "start",
        "-a",
        "android.intent.action.VIEW",
        "-d",
        f"https://www.youtube.com/results?search_query={query}"
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Launched YouTube with search query: {query}")
    except subprocess.CalledProcessError as e:
        print(f"Error launching YouTube: {e.stderr}")
    except FileNotFoundError:
        print("Error: am command not found.  Ensure Termux is properly configured.")


if __name__ == "__main__":
   search_term = input(f"Enter your {anco.frd}YouTube{anco.frs} search query: ")
   if len(search_term) < 1:
    print(f'search term is empty')
    sys.exit()
   # Basic URL encoding (replace spaces with '+') -  Consider a more robust library for complex queries.
   encoded_query = search_term.replace(" ", "+") 
   search_youtube(encoded_query)

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
