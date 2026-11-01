#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import time
import inspect
import subprocess
import shutil  # Moved to the top for consistency
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed 
from ansicolors import *  

# 1. Immediate CLI Argument Handling
def usg(sbn):
    usg_text = inspect.cleandoc(f'''
    alias    : {fgr} {frs}
    function : {fyl} {frs}
    usage    : {frs} {sbn} [argument]
    ''')
    print(usg_text)

sbn = os.path.basename(sys.argv[0])
if len(sys.argv) > 1 and sys.argv[1] == '-h':
    usg(sbn)
    sys.exit(0)

# 2. Initialization & Metrics
start_time = time.time()

try:
    import osl
    osl.osl(sys.argv[0])
    for message in osl.info:
        print(message)
except ImportError:
    pass

try:
    from tcget import tcget
except ImportError:
    tcget = lambda: ""

# Constants
ALLOWED_EXTS = {'.jpg', '.jpeg', '.png'}
MAX_WORKERS = 4  

def subp(cmd_list):
    spr = subprocess.run(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"sout": spr.stdout, "serr": spr.stderr, "sret": spr.returncode}

def check_and_install_dependencies():
    for cmd in ['jpegoptim', 'optipng', 'pngquant', 'ffmpeg']:
        print(f'{fbl}checking the status of{frs} {cmd}')
        if shutil.which(cmd) is not None:
            print(f'installed: {fgr}{cmd}{frs}')
        else:
            print(f'{frd}{cmd} missing. Installing via apt...{frs}')
            subp(['apt', 'install', '-y', cmd])

def format_size(bytes_size):
    """Converts bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} GB"

def optm(file_path: Path):
    """Optimizes single image files. Returns log string if processed, None otherwise."""
    file_ext = file_path.suffix.lower()
    if file_ext not in ALLOWED_EXTS:
        return None
    
    # Track initial size and name
    orig_name = file_path.name
    orig_size = file_path.stat().st_size
    target_jpeg = file_path.with_suffix('.jpeg')
    
    if file_ext == '.png':
        subprocess.run(['optipng', '-quiet', str(file_path)])
        
        fq = file_path.with_name(f"{file_path.stem}-qnt.png")
        subprocess.run(['pngquant', '--ext', '-qnt.png', '--skip-if-larger', str(file_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if fq.exists() and fq.stat().st_size > 0:
            subprocess.run(['rm', str(file_path)])
            subprocess.run(['ffmpeg', '-y', '-i', str(fq), str(target_jpeg)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if target_jpeg.exists() and target_jpeg.stat().st_size > 0:
                subprocess.run(['rm', str(fq)])
        else:
            subprocess.run(['ffmpeg', '-y', '-i', str(file_path), str(target_jpeg)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if target_jpeg.exists() and target_jpeg.stat().st_size > 0:
                subprocess.run(['rm', str(file_path)])
                
    if file_path.suffix.lower() in {'.jpg', '.jpeg'} or (file_ext == '.png' and target_jpeg.exists()):
        active_file = target_jpeg if file_ext == '.png' else file_path
        subprocess.run(['jpegoptim', '-fsq', str(active_file)])
    
    # Determine the final active file to check size
    final_file = target_jpeg if file_ext == '.png' else file_path
    
    if final_file.exists():
        final_size = final_file.stat().st_size
        saved = orig_size - final_size
        pct = (saved / orig_size * 100) if orig_size > 0 else 0
        
        # Build a verbose breakdown string for this file
        out_name = final_file.name
        return (f"  {fyl}{orig_name}{frs} -> {fgr}{out_name}{frs}\n"
                f"  Size: {format_size(orig_size)} -> {format_size(final_size)} "
                f"({fbl}Saved: {format_size(saved)} / {pct:.1f}%{frs})")
    return f"  {frd}Failed to optimize {orig_name}{frs}"

def draw_progress_bar(current, total):
    """Prints a dynamic, self-refreshing inline progress bar."""
    bar_length = 30
    fraction = current / total if total > 0 else 0
    filled_length = int(bar_length * fraction)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    percent = int(fraction * 100)
    
    sys.stdout.write(f"\r{fbl}Optimizing: {fmg}[{bar}] {percent}% ({current}/{total}){frs}")
    sys.stdout.flush()

def process_path(target_path: Path):
    """Processes target paths, tracking background threads with a progress bar."""
    if target_path.is_file():
        if target_path.suffix.lower() in ALLOWED_EXTS:
            draw_progress_bar(0, 1)
            result = optm(target_path)
            draw_progress_bar(1, 1)
            print("\n")
            if result:
                print(result)
    elif target_path.is_dir():
        files_to_process = [item for item in target_path.rglob('*') if item.is_file() and item.suffix.lower() in ALLOWED_EXTS]
        total_files = len(files_to_process)
        
        if total_files == 0:
            print("No valid images found.")
            return

        print(f"{fbl}Processing {total_files} images across {MAX_WORKERS} threads...{frs}")
        draw_progress_bar(0, total_files)
        
        results = []
        completed_count = 0
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(optm, f): f for f in files_to_process}
            
            for future in as_completed(futures):
                completed_count += 1
                draw_progress_bar(completed_count, total_files)
                res = future.result()
                if res:
                    results.append(res)
                    
        print("\n\n" + f"{fmg}=== Reduction Report ==={frs}")
        for report in results:
            print(report)
        print("========================")

if __name__ == '__main__':
    check_and_install_dependencies()

    input_target = sys.argv[1] if len(sys.argv) > 1 else tcget()
    if not input_target or not os.path.exists(input_target):
        input_target = input(f'image file/folder: ')
        
    target_path = Path(input_target)
    if not target_path.exists():
        print(f'not exists: {target_path}')
        sys.exit(1)
        
    process_path(target_path)

    elapsed_time = time.time() - start_time
    print(f"\n{fgr}All done!{frs} Total time: {elapsed_time:.2f} seconds")
