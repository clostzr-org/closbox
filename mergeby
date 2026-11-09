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
    from PIL import Image
    
    # -------------------------- CONFIGURATION --------------------------
    IMAGE_FOLDER = "./"       # Folder where your images are (current folder by default)
    OUTPUT_FOLDER = "./merged_by_year"  # Folder to save merged results
    IMAGE_EXT = ".jpeg"       # File extension of your images
    # -------------------------------------------------------------------
    
    def extract_year(filename):
        """Extract 4-digit year from filename like '202110n.jpeg' → '2021'"""
        # Get first 4 characters before any letters/extension
        year = filename.split(".")[0][:4]
        if year.isdigit() and len(year) == 4:
            return year
        return None
    
    def merge_images_vertical(image_paths, output_path):
        """Merge list of images vertically into one file"""
        if not image_paths:
            return
        
        # Open all images
        images = [Image.open(img) for img in image_paths]
        
        # Calculate total height & max width
        total_width = max(img.width for img in images)
        total_height = sum(img.height for img in images)
        
        # Create blank canvas
        merged = Image.new("RGB", (total_width, total_height), color="white")
        
        # Paste images one below another
        y_offset = 0
        for img in images:
            merged.paste(img, (0, y_offset))
            y_offset += img.height
        
        # Save result
        merged.save(output_path)
        print(f"✅ Saved merged file: {output_path}")
    
    def main():
        # Create output folder if not exists
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        
        # Group images by year
        year_groups = {}
        
        # Scan all files in folder
        for filename in os.listdir(IMAGE_FOLDER):
            if filename.lower().endswith(IMAGE_EXT):
                year = extract_year(filename)
                if year:
                    if year not in year_groups:
                        year_groups[year] = []
                    # Sort by full filename (so month order stays correct: 01,02...12)
                    year_groups[year].append(os.path.join(IMAGE_FOLDER, filename))
        
        # Sort each group properly
        for year in year_groups:
            year_groups[year].sort()  # Sorts by month then n/p type
        
        # Merge each year group
        for year, files in year_groups.items():
            output_file = os.path.join(OUTPUT_FOLDER, f"merged_{year}{IMAGE_EXT}")
            merge_images_vertical(files, output_file)
        
        print("\n🎉 All done! Merged files are in:", OUTPUT_FOLDER)
    
    if __name__ == "__main__":
        main()
    
    
    print(f"Elapsed time: {time.time() - start_time} seconds")

