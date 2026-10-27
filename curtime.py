#!/data/data/com.termux/files/usr/bin/python
import inspect, os, subprocess, sys, time

sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'

import os, sys
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
ddbne = sdbne

def info():
    print(f'ddbne: {ddbne}')
    print(f'spath: {spath}')
    print(f'sdbne: {sdbne}')
    
import osl; 
oslout = osl.osl(spath)
if  not oslout == "link exists":
    print(f'osl output: {oslout}')
    for message in osl.info:
        print(f'{message}')
    
def exargs():
 args = ' '.join(sys.argv)
 args = args.replace(sys.argv[0], '')
 #os.system(f'cmd {args}')
 
def usg():
 usg = inspect.cleandoc(f'''
 == {sne} (currentTime) ==
 usage: {sne} [time_format]
 format:
  %%   a literal %
  %a   locale's abbreviated weekday name (e.g., Sun)
  %A   locale's full weekday name (e.g., Sunday)
  %b   locale's abbreviated month name (e.g., Jan)
  %B   locale's full month name (e.g., January)
  %c   locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
  %C   century; like %Y, except omit last two digits (e.g., 20)
  %d   day of month (e.g., 01)
  %D   date; same as %m/%d/%y
  %e   day of month, space padded; same as %_d
  %F   full date; like %+4Y-%m-%d
  %g   last two digits of year of ISO week number (see %G)
  %G   year of ISO week number (see %V); normally useful only with %V
  %h   same as %b
  %H   hour (00..23)
  %I   hour (01..12)
  %j   day of year (001..366)
  %k   hour, space padded ( 0..23); same as %_H
  %l   hour, space padded ( 1..12); same as %_I
  %m   month (01..12)
  %M   minute (00..59)
  %n   a newline
  %N   nanoseconds (000000000..999999999)
  %p   locale's equivalent of either AM or PM; blank if not known
  %P   like %p, but lower case
  %q   quarter of year (1..4)
  %r   locale's 12-hour clock time (e.g., 11:11:04 PM)
  %R   24-hour hour and minute; same as %H:%M
  %s   seconds since the Epoch (1970-01-01 00:00 UTC)
  %S   second (00..60)
  %t   a tab
  %T   time; same as %H:%M:%S
  %u   day of week (1..7); 1 is Monday
  %U   week number of year, with Sunday as first day of week (00..53)
  %V   ISO week number, with Monday as first day of week (01..53)
  %w   day of week (0..6); 0 is Sunday
  %W   week number of year, with Monday as first day of week (00..53)
  %x   locale's date representation (e.g., 12/31/99)
  %X   locale's time representation (e.g., 23:13:48)
  %y   last two digits of year (00..99)
  %Y   year
  %z   +hhmm numeric time zone (e.g., -0400)
  %:z  +hh:mm numeric time zone (e.g., -04:00)
  %::z  +hh:mm:ss numeric time zone (e.g., -04:00:00)
  %:::z  numeric time zone with : to necessary precision (e.g., -04, +05:30)
  %Z   alphabetic time zone abbreviation (e.g., EDT)
 ''')
 print(usg)
 
def ctm(*args):
 from datetime import datetime
 now = datetime.now()
 ctm_custom = now.strftime("%Y.%m%d.%H%M%S")
 ctm_Y = now.strftime("%Y")
 ctm_YB = now.strftime("%Y.%B")
 ctm_Ym = now.strftime("%Y.%m")
 for a in args:
  #print(f'__calledWith: {a}')
  match a:
   case ('-h' | '--help'):
    usg()
   case '':
    print(f'usage: {sne} [-h|custom|Y|YB|Ym|(time_format)]')
   case 'custom':
    print(ctm_custom)
    return ctm_custom
   case 'Y':
    print(ctm_Y)
    return ctm_Y
   case 'YB':
    print(ctm_YB)
    return ctm_YB
   case 'Ym':
    print(ctm_Ym)
    return ctm_Ym
   case _:
    ctm_fmt = now.strftime(f"{a}")
    print(ctm_fmt)
    return ctm_fmt

if __name__ == '__main__':
   try:
    arg = sys.argv[1]
   except Exception:
    arg = ''
   if arg.lower() == '-h':    
    usg()
    sys.exit()
   else:
    ctm(arg)
   