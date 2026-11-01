#!/data/data/com.termux/files/usr/bin/python
import os, sys, time, inspect, shutil, string, subprocess
try:
  import apkfile
except Exception:
  os.system(f'pip install apkfile')
  import apkfile
from apkfile import ApkFile, XapkFile, ApkmFile, ApksFile
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if not hbin in sys.path:
   sys.path.append(hbin)
from ansicolors import *
if os.path.islink(sys.argv[0]):
   spath = os.readlink(sys.argv[0])
else:
   spath = sys.argv[0]
   
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'

import osl
osl.osl(spath)
for message in osl.info:
    print(f'{message}')
    
import time
start_time = time.time()

args = sys.argv[1:]
jargs = ' '.join(args).strip()

def nosym(someString):
 import string
 #print(f'someString: {someString}')
 SPECIAL_CHARS = '_-[].+()'
 PERMITTED_CHARS = string.digits + string.ascii_letters + SPECIAL_CHARS
 someString = "".join(c for c in someString if c in PERMITTED_CHARS)
 print(someString)
 return someString
  
def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 #os.system(f'cmd {args}')
 return args
 
def apkrenamer(apk):
 print(f'{fgr}apk: \n{os.path.basename(apk)} {frs}')
 import zipfile, re
 from bcek import is_bash_program_installed as isbash
 if not isbash('aapt'):
    os.system('apt install aapt')
 with zipfile.ZipFile(apk, 'r') as apkz:
  abils = []
  afs1 = ''
  ar7 = 0
  ar8 = 0
  x86 = 0
  x86_64 = 0
  for a in apkz.infolist():
   afn = a.filename
   if re.search('lib', afn):
    #print(f'__afn: {afn}')
    afs = afn.split('/')
    #print(f'__afs1: {afs[1]} __afsx64: ({afsx64})')
    match afs[1]:
     case 'armeabi-v7a':
      if ar7 == 0:
       abils.append('ar7')
       ar7 = 1
     case 'arm64-v8a':
      if ar8 == 0:
       abils.append('ar8')
       ar8 = 1
     case 'x86':
      if x86 == 0:
       abils.append('x86')
       x86 = 1
     case 'x86_64':
      if x86_64 == 0:
       abils.append('x64')
       x86_64 = 1
 apk_file = ApkFile(path=f'{apk}')
 #print(apk_file.package_name, apk_file.version_name, apk_file.version_code)
 #print(apk_file.as_dict())
 apnm = apk_file.package_name
 avnm = apk_file.version_name
 abis = '+'.join(abils)
 if abis == '':
  abis = 'all'
 adict = apk_file.as_dict()
 akeys = adict.keys()
 apath = adict["path"]
 alab = adict["labels"]
 alen = alab["en"]
 if len(alen) == 0:
  alen = "label"
 nn = f'{apnm}_[{abis}]_{alen}_[{avnm}].apk'
 nn = nosym(f"{nn}")
 apkInfo = inspect.cleandoc(f'''
 --keys: {akeys}
 --path: {apath}
 --package.name: {apnm}
 --abis: {abis}
 --label: {alen}
 --version.name: {avnm}
 --newname: {nn}
 ''')
 #print(f'apkInfo: {apkInfo}')
 oldname = apk
 opdo = f'{os.path.dirname(oldname)}'
 newname = f'{opdo}/{nn}'
 skip = False
 if os.path.exists(newname):
  ope = f'{fbk} exists {frs}'
  #print(f'__{fmg}exists{frs}: {os.path.basename(newname)}')
  skip = True
 if oldname == newname:
  oen = f'{fbk} src=dst {frs}'
  #print(f'__{fbl}src=dst{frs}: {os.path.basename(oldname)}')
  skip = True
 else:
  oen = f'{fbk} newNameReady {frs}'
 if skip == True:
  print(f'{ope} {oen}')
  print(f'__{fcy}skipped{frs}: {os.path.basename(oldname)}')
 else:
  print(f'__{fgr}renaming{frs}: {oldname} {frd}to{frs} {newname}')
  try:
   shutil.move(oldname, newname)
  except Exception:
   shutil.copy2(oldname, newname)
   if os.path.exists(newname):
    os.remove(oldname)
  
def apkr_batch():
 dirlist()
  
def apkren(arg1):
 ida1 = os.path.isdir(arg1)
 ifa1 = os.path.isfile(arg1)
 if ida1 == True:
  os.chdir(arg1)
  apkr_batch()
 if ifa1 == True:
  os.chdir(os.path.dirname(arg1))
  if arg1.endswith('.apk'):
   print(f'__arg1.type: ApkFile \n__path: {gcb}')
   apkrenamer(gcb)
  else:
   print(f'__{frd}isNotApk{frs}: {gcb}')
  
def dirlist():
 old = os.listdir(os.getcwd())
 print(f'__{fmg}apkRenamer{frs}\n__{fcy}currentDir{frs}:{os.getcwd()}')
 for f in old:
  f = f'{os.getcwd()}/{f}'
  bnf = f'{os.path.basename(f)}'
  print(f'\n__{brd} file {frs}:{bgr} {bnf} {frs}')
  if f.endswith('.apk'):
   print(f'__{fgr}endsWithApk{frs}: {f}')
   apkrenamer(f)
  
print(f'{fyl}APK.RENAMER{frs}')
gcb = subprocess.run(
 ['termux-clipboard-get'], check=True, 
 stdout=subprocess.PIPE, universal_newlines=True
 )
gcb = gcb.stdout
idgcb = os.path.isdir(gcb)
ifgcb = os.path.isfile(gcb)
try:
 arg1 = sys.argv[1]
except Exception:
 arg1 = gcb
match arg1:
 case '.':
  apkr_batch()
 case _:
  apkren(arg1)

time.sleep(1)
input(f'{fyl}press Enter')
