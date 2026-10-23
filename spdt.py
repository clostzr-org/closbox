#!/data/data/com.termux/files/usr/bin/python
import time
start_time = time.time()
import os, sys
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
if  not hbin in sys.path:
    sys.path.append(hbin)
from ansicolors import *
spath = sys.argv[0]
if  os.path.islink(spath):
    spath = os.readlink(spath)
sdn   = os.path.dirname(spath)
sbn   = os.path.basename(spath)
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import osl; osl.osl(spath)
for message in osl.info:
    print(f'{message}')

args  = sys.argv[1:]
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
# speed_test.py
try:
 import speedtest
except Exception:
 os.system(f'pip install speedtest-cli')
 import speedtest

def test_internet_speed():
    # Initialize speedtest object
    st = speedtest.Speedtest()
    
    print("🔍 Finding best server...")
    st.get_best_server()  # Automatically select the closest/best server

    print("📥 Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbps

    print("📤 Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbps

    print("📶 Calculating ping...")
    ping_result = st.results.ping  # Latency in ms

    # Display results
    print("\n✅ Speed Test Results:")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping_result:.2f} ms")

if __name__ == "__main__":
    try:
        test_internet_speed()
    except Exception as e:
        print(f"❌ Error during speed test: {str(e)}")

if  __name__ == '__main__':
    try:
      if  sys.argv[1] == '-h':
          usg()
          sys.exit()
    except Exception:
      pass
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
