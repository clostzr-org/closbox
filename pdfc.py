#!/data/data/com.termux/files/usr/bin/python
import os
import shutil
import subprocess
import sys
import time

# Timing start
start_time = time.time()

# Define paths
home = '/data/data/com.termux/files/home'
hbak = f'{home}/bak'
hbin = f'{home}/bin'

# Append to sys.path if needed
if  hbin not in sys.path:
    sys.path.append(hbin)

# Import local or custom modules safely
try:
    from ansicolors import *
except ImportError:
    pass

try:
    import osl
    # FIX: Use index [0] to get the script path string instead of the whole list
    spath = sys.argv[0]
    if os.path.islink(spath):
        spath = os.readlink(spath)
    
    osl.osl(spath)
    for message in osl.info:
        print(message)
except ImportError:
    pass

# Initialize variables
verbose = False

def bootstrap_dependencies():
    """Ensures ghostscript tool is installed once before processing files."""
    # FIX: Use python's native shutil instead of running external 'which'
    if shutil.which('gs') is None:
        print("Installing ghostscript dependencies... please wait.")
        try:
            subprocess.run(['pkg', 'install', 'ghostscript', '-y'], check=True)
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'ghostscript'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Warning: Dependency installation encountered an issue: {e}")

def get_input_path():
    """Determines the target path via fallback strategies."""
    # 1. Try resolving path from 'tcget' command line call
    # FIX: Use python's native shutil instead of running external 'which'
    if shutil.which('tcget') is not None:
        try:
            path = subprocess.run(['tcget'], capture_output=True, check=True, text=True).stdout.strip()
            if os.path.exists(path):
                return path
        except subprocess.SubprocessError:
            pass

    # 2. Use command line argument if provided
    if len(sys.argv) > 1:
        # FIX: Access index [1] to grab the first argument path provided
        arg_path = sys.argv[1]
        if os.path.exists(arg_path):
            return arg_path

    # 3. Prompt user directly
    user_input = input("Enter a file or directory path: ").strip()
    if os.path.exists(user_input):
        return user_input
    
    print("Error: Provided path does not exist.")
    sys.exit(1)

def process_pdf(file_path):
    """Compresses a single PDF using ghostscript."""
    print(f"Processing file: {file_path}")
    
    base_path, _ = os.path.splitext(file_path)
    output_pdf = f"{base_path}.compressed.pdf"
    
    cmd = [
        'gs', 
        '-sDEVICE=pdfwrite', 
        '-dCompatibilityLevel=1.4', 
        '-dPDFSETTINGS=/ebook', 
        '-dNOPAUSE', 
        '-dBATCH', 
        f'-sOutputFile={output_pdf}', 
        file_path
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"Successfully Compressed -> {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file_path}:\n{e.stderr}")

def main():
    path = get_input_path()
    
    if os.path.isfile(path):
        if path.lower().endswith('.pdf'):
            bootstrap_dependencies()
            process_pdf(path)
        else:
            print("The specified file is not a PDF.")
    elif os.path.isdir(path):
        pdf_files = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.pdf') and not file.endswith('.compressed.pdf'):
                    pdf_files.append(os.path.join(root, file))
        
        if pdf_files:
            bootstrap_dependencies()
            for pdf in pdf_files:
                process_pdf(pdf)
        else:
            print("No PDF files found in the directory.")
    else:
        print("Invalid path type.")
        sys.exit(1)

    if verbose:
        print(f"Execution finished in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
