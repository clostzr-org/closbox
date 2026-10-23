#!/usr/bin/env python3
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
    import os
    import subprocess
    subprocess.run(['pip', 'install', 'pypdf'])
    import os
from pypdf import PdfWriter  # Use PdfWriter instead of PdfMerger

def merge_pdfs_in_directory(output_filename="merged_output.pdf"):
    # Initialize the modern writer object
    writer = PdfWriter()
    
    # Get and sort all PDF files in the current working directory
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and f != output_filename]
    pdf_files.sort()
    
    if not pdf_files:
        print("No PDF files found to merge.")
        return

    print(f"Found {len(pdf_files)} PDF files. Merging...")
    
    # Append each PDF file to the writer
    for pdf in pdf_files:
        print(f"Appending: {pdf}")
        writer.append(pdf)
    
    # Write the combined pages to the final output file
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)
        
    # Clean up resources
    writer.close()
    print(f"Success! All PDFs merged into '{output_filename}'.")

if __name__ == "__main__":
    merge_pdfs_in_directory()

    print(f"Elapsed time: {time.time() - start_time} seconds")

