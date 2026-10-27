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
    #!/usr/bin/env python3
    """
    Merge JPEG files into separate PDFs grouped by year.
    
    Filename examples:
        202110n.jpeg
        202110p.jpeg
        202201n.jpeg
    
    Output:
        2021.pdf
        2022.pdf
    """
    
    from pathlib import Path
    from collections import defaultdict
    from PIL import Image
    
    
    def create_pdf(images, output_pdf):
        pdf_pages = []
    
        for img_file in images:
            img = Image.open(img_file)
    
            # Convert to RGB because PDF does not support RGBA
            if img.mode != "RGB":
                img = img.convert("RGB")
    
            pdf_pages.append(img)
    
        if not pdf_pages:
            return
    
        pdf_pages[0].save(
            output_pdf,
            save_all=True,
            append_images=pdf_pages[1:]
        )
    
    
    def main():
        folder = Path(".")
    
        groups = defaultdict(list)
    
        for file in folder.glob("*.jp*g"):
            stem = file.stem
    
            # First 4 digits = year
            if len(stem) >= 4 and stem[:4].isdigit():
                year = stem[:4]
                groups[year].append(file)
    
        for year, files in sorted(groups.items()):
            # Sort filenames alphabetically
            files.sort(key=lambda p: p.name)
    
            output_pdf = folder / f"{year}.pdf"
    
            print(f"Creating {output_pdf.name} ({len(files)} images)")
            create_pdf(files, output_pdf)
    
        print("Done.")
    
    
    if __name__ == "__main__":
        main()
    
    
    print(f"Elapsed time: {time.time() - start_time} seconds")

