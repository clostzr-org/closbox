#!/usr/bin/env python3
import time
start_time = time.time()
import os
import sys

# Fast paths definition
home = '/data/data/com.termux/files/home'
hbak = os.path.join(home, 'bak')
hbin = os.path.join(home, 'bin')
hsym = os.path.join(home, 'symlink')

if hbin not in sys.path:
    sys.path.append(hbin)

# Lazy imports for better performance
from ansicolors import *

# Path parsing for the current script
spath = os.readlink(sys.argv[0]) if os.path.islink(sys.argv[0]) else os.path.abspath(sys.argv[0])
sdn = os.path.dirname(spath)
sbn = os.path.basename(spath)
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'

import osl
osl.osl(spath)
for i in osl.info:
    print(i)

args = sys.argv[1:]

def usg():
    import inspect
    usg_text = inspect.cleandoc(f'''
    alias: {fgr} make-script{frs}
 function: {fyl} make a script with some environment preset in it{frs}
    usage: {frs} {sbn} [-py|-sh] [filename]{frs}
    ''')
    print(usg_text)
    sys.exit()

header_py = """#!/usr/bin/env python3
import time
start_time = time.time()
import os, sys

home  = '/data/data/com.termux/files/home'
hbak  = os.path.join(home, 'bak')
hbin  = os.path.join(home, 'bin')
if hbin not in sys.path:
    sys.path.append(hbin)

from ansicolors import *
spath = os.readlink(sys.argv[0]) if os.path.islink(sys.argv[0]) else os.path.abspath(sys.argv[0])
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
verbose = False

import osl; osl.osl(spath)
for message in osl.info:
    print(message)

args  = sys.argv[1:]
jargs = ' '.join(args).strip()

def usg():
    import inspect
    usg_text = inspect.cleandoc(f'''
    alias: {fgr} {frs}
 function: {fyl} {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(usg_text)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        usg()
        sys.exit()
    
    # insert_your_codes_here
    
    print(f"Elapsed time: {time.time() - start_time} seconds")
"""

def hdsh(src_file, sym_file, ext):
    return f"""#!/data/data/com.termux/files/usr/bin/bash
if [[ ! -d {hsym} ]]; then
    mkdir -p {hsym}
    chmod 755 {hsym}
fi

if [[ ! -s {sym_file} ]]; then
    symstat="doesnt-exists"
    ln -sv {src_file} {sym_file}
    if [[ -s {sym_file} ]]; then
        symstat="newly-created"
        echo -e "symlink created:\\n{sym_file}"
    else
        symstat="failed-to-create"
        echo -e "failed to create symlink:\\n{sym_file}"
    fi
else
    symstat="exists"
fi

bnz=$(basename $0)
if [[ "${{bnz##*.}}" == "{ext.strip('.')}" ]]; then
    echo -e "source-file : $(readlink {sym_file})"
    echo -e "symlink-file: {sym_file}"
    echo -e "symlink-stat: $symstat"
fi

echo -e "usage: $(basename $0) [command]"
"""

def create(file_base, ext):
    clean_base = file_base.strip().replace(' ', '_')
    src_file = os.path.join(hbin, f"{clean_base}{ext}")
    sym_file = os.path.join(hsym, clean_base)
    
    match ext:
        case '.py':
            header = header_py
            hdlang = 'python'
        case '.sh':
            header = hdsh(src_file, sym_file, ext)
            hdlang = 'shell'
        case '.txt':
            header = ''
            hdlang = 'text'
        case _:
            header = ''
            hdlang = 'unknown'

    print(f'header language:\n{hdlang}')
    print(f'source_file: {src_file}')
    
    if not os.path.isfile(src_file):
        with open(src_file, 'w') as owsf:
            owsf.write(f'{header}\n')
            
    os.chmod(src_file, 0o755)
    os.system(f'micro {src_file}')

if __name__ == '__main__':
    if not args or args[0] in ('-h', '--help'):
        usg()

    ext = '.txt'
    bname = None

    for a in args:
        a_low = a.lower()
        if len(a_low) < 2:
            continue
        if a_low.startswith('.'):
            print(f'length: {len(a_low)} | current a will be the {fmg}extension{frs} ({a_low})')
            ext = a_low
        else:
            print(f'length: {len(a_low)} | current a will be the {fgr}basename{frs} ({a_low})')
            bname = a_low

    if not bname:
        print("Error: No valid filename / basename provided.")
        sys.exit(1)

    if '.' in bname:
        bnox, parsed_ext = bname.rsplit('.', 1)
        ext = f".{parsed_ext}"
    else:
        bnox = bname

    cnfrm = input(f'do you wanna create this file: {bnox}{ext}? (y/n): ').strip().lower()
    if cnfrm != 'y':
        sys.exit()

    create(bnox, ext)
    print(f"Elapsed time: {time.time() - start_time} seconds")
