#!/data/data/com.termux/files/usr/bin/python
import subprocess, fnmatch, string, json, re
import   colorama, inspect,   stat,  csv
import   datetime,  shutil,   time,  sys, os
import   requests,  random, socket, glob
from bs4 import BeautifulSoup
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
bbk = Back.BLACK; brd = Back.RED
bgr = Back.GREEN; byl = Back.YELLOW
bbl = Back.BLUE;  bmg = Back.MAGENTA
bcy = Back.CYAN;  bwh = Back.WHITE
fbk = Fore.BLACK; frd = Fore.RED
fgr = Fore.GREEN; fyl = Fore.YELLOW
fbl = Fore.BLUE;  fmg = Fore.MAGENTA
fcy = Fore.CYAN;  fwh = Fore.WHITE
frs = Fore.RESET
stdm  = Style.DIM;    stnr = Style.NORMAL
stbr  = Style.BRIGHT; stra = Style.RESET_ALL
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'
start_time = time.time()

try:
 import osl
except Exception:
 print(f'{frd}unable to import osl{frs}')

if os.path.exists(sdbne) and os.path.islink(sdbne):
 print(f'{fbl}islink{frs}: {sne}')
 pass
elif os.path.exists(sdbne) and not os.path.islink(sdbne):
 print(f'{frd}isnotlink{frs}: {sne}')
 os.remove(sdbne)
 os.symlink(__file__, sdbne)
else:
 os.symlink(__file__, sdbne)
 print(f'{fgr}created symlink{frs}: {sdbne}')

def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [html-file-or-url]
           {sbn} -f <html file name with spaces allowed, or a url>

    input resolution order:
      1) termux-clipboard-get, if it holds either:
         - a url (starts with http:// or https://), or
         - a path to an existing supported file (.html/.htm)
      2) command-line argument(s) (supports unquoted spaces)
      3) -f flag, explicitly followed by a filename or url (spaces
         allowed, everything after -f is joined into one string)
      if none of the above yield a usable input, this usage is shown.
    ''')
    print(f'{usg}')

args = sys.argv[1:]

SUPPORTED_EXTS = ('.html', '.htm')
URL_RE = re.compile(r'^https?://\S+$', re.IGNORECASE)

def is_url(s):
    if not s:
        return False
    return bool(URL_RE.match(s.strip()))

def is_supported_file(path):
    if not path:
        return False
    path = path.strip()
    if is_url(path):
        return True
    if not os.path.isfile(path):
        return False
    return path.lower().endswith(SUPPORTED_EXTS)

def get_clipboard_file():
    try:
        cb = subprocess.run(
            ['termux-clipboard-get'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True
        )
    except FileNotFoundError:
        return None
    clip = (cb.stdout or '').strip()
    if is_supported_file(clip):
        return clip
    return None

def resolve_input_file():
    # 1) -f explicit flag: everything after -f is the filename (spaces ok)
    if '-f' in args:
        idx = args.index('-f')
        rest = args[idx + 1:]
        if not rest:
            usg()
            sys.exit(1)
        fname = ' '.join(rest).strip()
        if not fname:
            usg()
            sys.exit(1)
        return fname

    # 2) termux-clipboard-get, if it's a supported existing file
    clip_file = get_clipboard_file()
    if clip_file:
        print(f'{fcy}using clipboard as input{frs}: {clip_file}')
        return clip_file

    # 3) fall back to whatever was passed as arguments (join for spaces)
    if args:
        fname = ' '.join(args).strip()
        if fname:
            return fname

    # 4) nothing usable
    usg()
    sys.exit(1)

#insert_your_codes_here
subprocess.run(['apt', 'install', 'pango'])
try:
 import weasyprint
except Exception:
 cmd = 'pip install weasyprint'
 subrun = subprocess.run(cmd.split(), stdout=subprocess.PIPE, universal_newlines=True, check=True)
 print(f'{subrun.stdout}')
 import weasyprint

html_file = resolve_input_file()

if is_url(html_file):
    from urllib.parse import urlparse
    url_path = urlparse(html_file).path
    htmf_bn = os.path.basename(url_path) or urlparse(html_file).netloc
    if not htmf_bn:
        htmf_bn = 'webpage'
else:
    htmf_bn = os.path.basename(html_file)

pdf_file = f'/sdcard/{htmf_bn}.pdf'  # Replace with your desired PDF file path

try:
    if is_url(html_file):
        weasyprint.HTML(url=html_file).write_pdf(pdf_file)
    else:
        weasyprint.HTML(string=open(html_file, 'r').read()).write_pdf(pdf_file)
    print(f"HTML input '{html_file}' converted to PDF '{pdf_file}' successfully.")
except Exception as e:
    print(f"Error converting HTML to PDF: {e}")


if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
