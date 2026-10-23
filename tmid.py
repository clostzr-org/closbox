#!/data/data/com.termux/files/usr/bin/python
import csv, datetime, fnmatch, inspect, json
import os, re, shutil, stat, string
import subprocess, sys, time
import csv, inspect, os, re, socket
import subprocess, sys, time
import shutil

def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
        'black':  '\033[30m',        'red':    '\033[31m',
        'green':  '\033[32m',        'yellow': '\033[33m',
        'blue':   '\033[34m',        'magenta':'\033[35m',
        'cyan':   '\033[36m',        'white':  '\033[37m',
        'reset': '\033[0m'
    }

    code = ''
    if reset:
        code = color_codes['reset']
    elif fg:
        code = color_codes.get(fg, '')
    elif bg:
        code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'  # Background code adjustment

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

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'
script_dn = os.path.dirname(sys.argv[0])
script_bn = os.path.basename(sys.argv[0])
script_ne = os.path.splitext(script_bn)[0]
dnoext = f'{script_dn}/{script_ne}'
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
start_time = time.time()
 
def usg():
 usg = inspect.cleandoc(f'''
 usage: {script_ne} <argument>
 arguments: mnu    month_num to month_longname
            mns    month_name_short
            dlo    day_longname
            dsh    day_shortname
 {script_ne}(dname_l2l="Monday")      get.dname long to long
 {script_ne}(dname_s2s="Mon")         get.dname short to short
 {script_ne}(mname_l2l="February")    get.mname long to long
 {script_ne}(mname_n2l="1")           get.mname number to long
 {script_ne}(mname_n2s="1")           get.mname number to short
 {script_ne}(mname_s2s="Feb")         get.mname short to short
            
 ''')
 print(f'{usg}')

def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(f'{sys.argv[0]} ', '')
 #os.system(f'cmd {args}')
 return args

args = sys.argv[1:]
 
#insert_your_codes_here
day_names_long = {
'Monday'   : 'Senin',
'Tuesday'  : 'Selasa',
'Wednesday': 'Rabu',
'Thursday' : 'Kamis',
'Friday'   : 'Jumat',
'Saturday' : 'Sabtu',
'Sunday'   : 'Minggu'
}

day_names_short = {
'Mon': 'Sen', 'Tue': 'Sel',
'Wed': 'Rab', 'Thu': 'Kam',
'Fri': 'Jum', 'Sat': 'Sab',
'Sun': 'Min'
}
 
month_names_long = {
'01': 'Januari',   '02': 'Februari',
'03': 'Maret',     '04': 'April',
'05': 'Mei',       '06': 'Juni',
'07': 'Juli',      '08': 'Agustus',
'09': 'September', '10': 'Oktober',
'11': 'November',  '12': 'Desember',
'January': 'Januari',    'February': 'Februari',
'March': 'Maret',           'April': 'April',
'May': 'Mei',                'June': 'Juni',
'July': 'Juli',            'August': 'Agustus',
'September': 'September', 'October': 'Oktober',
'November': 'November',  'December': 'Desember'
}

month_names_short = {
'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
'05': 'Mei', '06': 'Jun', '07': 'Jul', '08': 'Agu',
'09': 'Sep', '10': 'Okt', '11': 'Nov', '12': 'Des',
'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr',
'May': 'Mei', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Agu',
'Sep': 'Sep', 'Oct': 'Okt', 'Nov': 'Nov', 'Dec': 'Des'
}

def tmid(*args, **kwargs):
    tsft = time.strftime
    tsYm = tsft("%Y.%m")
    tsa = tsft("%a")
    tsA = tsft("%A")
    tsb = tsft("%b")
    tsB = tsft("%B")
    tsm = tsft("%m")
    args = ' '.join(args)
    apairs = args.split(',')
    try:
     key, value = apairs
     print(f'key={key}, value={value}')
     if apairs[0] == 'dname_l2l':
      idv = day_names_long.get(apairs[1], tsA)
      return idv
     if apairs[0] == 'dname_s2s':
      idv = day_names_short.get(apairs[1], tsa)
      return idv
     if apairs[0] == 'mname_l2l':
      idv = month_names_long.get(apairs[1], tsB)
      return idv
     if apairs[0] == 'mname_n2l':
      idv = month_names_long.get(apairs[1], tsB)
      return idv
     if apairs[0] == 'mname_n2s':
      idv = month_names_short.get(apairs[1], tsb)
      return idv
     if apairs[0] == 'mname_s2s':
      idv = month_names_long.get(apairs[1], tsb)
      return idv
    except Exception:
     pass
    for arg in apairs:
     if __name__ == "__main__":
      print(f'args: {args}\napairs: {apairs}\narg: {arg}')
      for a in arg.split(' '):
       print(f'a: {a}')
    for key, value in kwargs.items():
     print(f'key_{key}: value_{value}')
     if key == 'dname_l2l':
      idv = day_names_long.get(value, tsA)
      return idv
     if key == 'dname_s2s':
      idv = day_names_short.get(value, tsa)
      return idv
     if key == 'mname_l2l':
      idv = month_names_long.get(value, tsB)
      return idv
     if key == 'mname_n2l':
      idv = month_names_long.get(value, tsB)
      return idv
     if key == 'mname_n2s':
      idv = month_names_short.get(value, tsb)
      return idv
     if key == 'mname_s2s':
      idv = month_names_long.get(value, tsb)
      return idv
    dlo = day_names_long.get(tsA, tsA)
    dsh = day_names_short.get(tsa, tsa)
    mnu = month_names_long.get(tsm, tsm)
    mns = month_names_short.get(tsm, tsb)
    for arg in apairs:
     for a in arg.split(' '):
      if a == 'dlo':
       return dlo
      if a == 'dsh':
       return dsh
      if a == 'mnu':
       return mnu
      if a == 'mns':
       return mns

if __name__ == "__main__":
 try:
  arg1 = sys.argv[1]
 except Exception:
  usg(); sys.exit()
 print(tmid(exargs()))
 #print(tmid(str(args)))
 end_time = time.time()
 elapsed_time = end_time - start_time
 #print(f"Elapsed time: {elapsed_time} seconds")

