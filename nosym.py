#!/data/data/com.termux/files/usr/bin/python
from ansicolors import *

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

import osl
osl.osl(sys.argv[0])
for i in osl.info:
    print(f'{i}')
    
args = sys.argv[1:]
jargs = ' '.join(args).replace(' ', '_')

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias    : {fgr} {frs}
    function : {fyl} {frs}
    usage    : {frs} {sbn} [argument]
    ''')
    print(f'{usg}')

import string

def nosym(some_string):
    SPECIAL_CHARS = '_-[].+(),'
    PERMITTED_CHARS = string.digits + string.ascii_letters + SPECIAL_CHARS
    some_string = "".join(c for c in some_string if c in PERMITTED_CHARS)
    return some_string

if __name__ == '__main__':
   ns_out = nosym(jargs)
   print(f'{ns_out}')
