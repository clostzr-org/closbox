#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import time
from datetime import datetime

def usg():
    print(f"Usage {sys.argv[0]} <file_path>")

try:
    a1 = sys.argv[1]
except Exception:
    usg()
    sys.exit()

ct = os.path.getctime(a1)
mt = os.path.getmtime(a1)
now = datetime.now()
now_timestamp = time.time()  # Store as a timestamp

dff = now_timestamp - mt
dffh = dff / 86400  # Calculate days

# Format timestamps for readability
ct_dt = datetime.fromtimestamp(ct)
mt_dt = datetime.fromtimestamp(mt)
now_dt = datetime.fromtimestamp(now_timestamp)

nfo = f"""
File: {a1}
Creation Time     : {ct_dt.strftime('%Y-%m-%d %H:%M:%S')}
Modification Time : {mt_dt.strftime('%Y-%m-%d %H:%M:%S')}
Current Time      : {now_dt.strftime('%Y-%m-%d %H:%M:%S')}
Modification Age  : {dff:.2f} seconds ({dffh:.2f} day(s))
"""

print(f"Info:\n{nfo}")
