#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'
import sys
if not hbin in sys.path:
   sys.path.append(hbin)
   
from ansicolors import *

import os, sys
spath = os.path.abspath(sys.argv[0])
if os.path.islink(spath):
   spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
verbose = False

import osl
osl.osl(sys.argv[0])
for message in osl.info:
    print(f'{message}')

args = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr}bjs workers attendance formatter{frs}
 function: {fyl}transform recordList.csv into readable format {frs}
    usage: {frs} {sbn} [filepath] [custom_date]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here
""" this is how the input lines formatted
'Yana,'15,'NULL,2025-09-01,19:55:01,'IN,1,5, 38,checkOut,776
'Admin,'1,'1,2025-09-01,20:04:02,'IN,1,5, 38,checkIn,779
'Esih,'11,'NULL,2025-09-01,20:04:17,'IN,1,5, 38,checkIn,783
'Jajang,'13,'NULL,2025-09-01,20:06:14,'IN,1,5, 38,checkIn,790
"""

import os

def dayname(dtime):
    import datetime
    date_string = dtime
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    day_name = date_object.strftime('%A')
    #print(day_name)
    return day_name

def modify_and_sort_csv(filepath, datelim):
    print(f'masc: filepath: {filepath}')
    #input(f'press Enter');sys.exit()
    """
    Modifies a CSV file by replacing spaces with underscores,
    and sorting numerically, and writing the output to a new file.
    """

    with open(filepath, 'r') as infile:
         lines = infile.readlines()
    print(f'lines:\n{lines}')
    #input(f'press Enter'); sys.exit()

    modified_lines = []
    nullcount = 0

    for line in lines:
        line = line.replace("'", "")
        modified_line = line.replace(' ', '_').replace("'", "")
        baris = line.strip().split(',')
        info_lb = ''
        if info_lb == 'on':
           print(f'current_line: {line}')
           print(f'current_baris: {baris}')
           #input(f'press Enter'); sys.exit
        if baris[0] == "NULL":
           nullcount = 1
           print(f'null name detected')
        if nullcount == 1:
           print(f'skipping null name{frd}{baris[0]}{frs}')
           break
        if baris[0] == 'sName':
           print(f'skipping {frd}{baris[0]}{frs}')
           continue
        print(f'beginning of for parts in baris')
        #input(f'press Enter'); sys.exit()
        nline = []
        for part in baris:
            print(f'current part: {fgr}{part}{frs}')
            #input(f'press Enter'); sys.exit()
            name=baris[0]
            jobno=int(baris[1]) - 1
            if len(str(jobno)) < 2:
               jobno = f'0{jobno}'
            sdate=str(baris[3].replace(':', '/'))
            #print(f'{fyl}sdate{frs}: {sdate}')
            current_date = str(sdate)
            currdt = current_date.replace('-', '')
            date_limit = str(datelim)
            datlim = date_limit.replace('-', '')
            #print(f'{fyl}current_dt{frs}: {currdt}')
            #print(f'{fmg}date_limit{frs}: {datlim}')
            from datetime import datetime

            date_string = str(datelim)
            date_object = datetime.strptime(date_string, "%Y%m%d")
            formatted_date = date_object.strftime("%Y-%m-%d")
            formatted_year = date_object.strftime("%Y")
            #print(f'{fbl}formatted_date: {formatted_date}{frs}')

            if sdate < formatted_date:
               #print(f'{sdate} is {frd}older{frs} than 2025-09-01')
               skip = 'yes'
            else:
               #print(f'{sdate} is {fbl}newer{frs} than 2025-09-01')
               skip = 'no'

            if int(currdt) < int(datlim):
               #print(f'{sdate} is {frd}older{frs} than 2025-09-01')
               skip = 'yes'
            else:
               #print(f'{sdate} is {fbl}newer{frs} than 2025-09-01')
               skip = 'no'
            #sys.exit()
            hari=dayname(sdate)
            stime=baris[4][:-3]  # Remove seconds
            status=baris[9]
        if skip == 'yes':
           print(f'{frd}skipping this date{frs}: {sdate}')
           continue
        else:
           print(f'{fbl}including this date{frs}: {sdate}')
           pass
        #sys.exit()
        def info_line():
            print(f'jobno: {jobno}')
            print(f'name: "{name}"')
            print(f'date: {sdate}')
            print(f'hari: {hari}')
            print(f'time: {stime}')
            print(f'status: {status}')
        print(f'infoline: {info_line}')
        #input(f'press Enter'); sys.exit()
        nline = f'{jobno},{name},{sdate},{stime},{status}\n'  # Omit day name here
        print(f'{frd}nline: {nline}')
        #input(f'press Enter');sys.exit()
        #print(f'modified_lines: {modified_lines}')
        #input(f'press Enter');sys.exit()
        modified_line=nline
        modified_lines.append(modified_line)

    # Sort numerically
    modified_lines = sorted(modified_lines)
    modified_lines.append("\n['0','1','2','3','4']")
    #print(f'modified lines:\n{modified_lines}')
    input(f'press Enter');
    mlines=modified_lines
    prevline=''
    p_cdate=''
    sumline=''
    sumlines=''
    jno='01'
    info1='on'
    info2='on'
    info3=''
    for mline in mlines:
        mline = mline.replace('\n', '')
        if info1 == 'on':
           print(f'\n{frd}1. current_mline{frs}: {mline}')
        ml=mline.split(',')
        if info2 == 'on':
           print(f'2. current_{frd}ml{frs}: {ml}')
        cjno=ml[0]
        cname=ml[1]
        cdate=ml[2]
        ctime=ml[3]
        cstat=ml[4]
        def jnostat():
            print(f'jno: {jno} | cjno: {cjno}')
            #print(f'{fgr}current prevline: {prevline}')
            #print(f'{fyl}3. current_sumline{frs}: {sumline}')
        nn=f'{cjno},{cname}'
        if not cjno in sumline:          
           #print(f'not cjno in sumline')
           sumline = mline
        else:
           #print(f'{frd}cjno is in sumline{frs}')
           cdat=f'{cdate},{ctime},{cstat}'
           cts=f'{ctime},{cstat}'
           c_cdate = cdate
           def cdatinfo():
               print(f'previous_cdat: {p_cdate}')
               print(f'current_cdat: {c_cdate}')
           if p_cdate == c_cdate:
              #sumline = sumline + f',{cts}'
              sumline = sumline + f',{cdat}'
           else:
              sumline = sumline + f',{cdat}'
        #prevline = sumline
        currentline = mline
        if cjno == jno:
           def cjnoequ():
               print(f'merging data of {cjno}')
               print(f'cjno: {cjno}')
               print(f'cname: {cname}')
               print(f'cdate: {cdate}')
               print(f'ctime: {ctime}')
               print(f'cstat: {cstat}')
               print(f'cjno({cjno}) = jno({jno})')
               print(f'4. current_sumline:{fmg}{sumline}{frs}')
               #cdat=f'{cdate},{ctime},{cstat}'
               print(f'prevline: {prevline}')
               print(f'currentline: {mline}')
           if prevline in sumline:
              #print(f'prevline is in sumline')
              pass
        else:
           #print(f'saving last sumline before resetting it...') 
           sumlines = sumlines + f'\n\n{prevline}'
           print(f'{fmg}sumline before reset{frs}: {prevline}')
           #input(f'press Enter'); sys.exit()
           #print(f'{frd}resetting the sumline{frs}')
           sumline=mline
        #print(f'{fbl}final_sumline{frs}: {sumline}')  
        prevline = sumline 
        p_cdate = cdate      
        jno = cjno
    #print(f'{frd}sumlines after the loop{frs}: {sumlines}')
    
    #print(f'{frd}sums afterloop ends{frs}')
    modified_lines = sumlines
    print(f'modified_lines: {fcy}{modified_lines}{frs}')
    #input(f'press Enter'); sys.exit()
    
    # Write to a new file with "-sorted" appended to the basename
    base, ext = os.path.splitext(filepath)
    fdn  = os.path.dirname(filepath)
    fbn  = os.path.basename(filepath)
    fbn0 = fbn.rsplit('.', 1)[0]
    print(f'fbn: {fbn}')
    ext = fbn.rsplit('.', 1)[1]
    output_basename = f"{formatted_date}-{fbn0}-sorted.{ext}"
    output_filepath = f"{fdn}/{formatted_date}-{fbn0}-sorted.{ext}"

    with open(output_filepath, 'w') as outfile:
         outfile.writelines(modified_lines)

    print(f"{frd}{sbn}{frs}:Modified and sorted data written to: {output_filepath}")
    yearmonth = date_object.strftime("%Y-%m")
    year = yearmonth.split('-')[0]
    month = yearmonth.split('-')[1]
    output_dir = f'/sdcard/bjs/attendance/{year}/{month}'
    os.makedirs(f'/sdcard/bjs/attendance/{year}/{month}', exist_ok=True)
    os.system(f'cp -v {output_filepath} {output_dir}/{output_basename}')
    os.system(f'rcopyto.py {output_filepath} gdcs:bjs/attendance/{year}/{month}')
    print(f'converting modified lines into xlsx file...')
    os.system(f'bjssum.py {output_filepath}')
    print(f'conversion to xlsx done.')        

# Get user input for the file path
def transf():
    from tcget import tcget
    try:
       inpuT = tcget()
       print(f'{fyl}input from tcget{frs}: {inpuT}')
    except Exception:
       try:
          inpuT = sys.argv[1]
       except Exception:
          inpuT = input(f'inpuT: ')
    print(f'{fgr}inpuT{frs}: {inpuT}')
    
    try:
       datelim = sys.argv[2]
    except Exception:
       datelim = ''
       
    if len(datelim) == 0:
       datelim = 20250901
    
    if len(inpuT) > 0:
       print(f'{fgr}inpuT length is bigger than zero{frs}')
       #inpuT_ext = inpuT.rsplit('.', 1)[1]
       #print(f'inpuT_ext: {inpuT_ext}')
       #if not inpuT_ext == 'xlsx':
       #   print(f'{frd}inpuT file is not a xlsx{frs}')
       #   sys.exit()
    else:
       print(f'{frd}inpuT is empty{frs}')
       #sys.exit()
    if os.path.isfile(inpuT):
       filepath = inpuT
    else:
       filepath = '/sdcard/bjs/recordList.csv'
       from xsdc import xsd_df
       extsd = xsd_df()
       print(f'extsd: {extsd}')
       if os.path.isdir(extsd):
          xsdir = f'{extsd}/bjs/attendance'
          filepath = f'{xsdir}/recordList.csv'
          print(f'external filepath: {filepath}')
          
       #input(f'press Enter'); sys.exit()
       if not os.path.isdir(f'/sdcard/bjs'):
          os.makedirs('/sdcard/bjs', exist_ok=True)
       try:
          datelim = sys.argv[2]
       except Exception:
          datelim = input(f'oldest date to include: ')
          
       if len(datelim) == 0:
          datelim = 20250901
    #filepath = input("Enter the path to the CSV file: ")

    # Call the function to modify and sort the CSV file
    print(f'current filepath: {filepath}')
    #input(f'press Enter'); sys.exit()
    modify_and_sort_csv(filepath, datelim)

if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   transf()
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")