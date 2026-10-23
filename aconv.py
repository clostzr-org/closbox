#!/data/data/com.termux/files/usr/bin/python

def ansi_color(fg=None, bg=None, reset=False):
    color_codes = {
    'black':'\033[30m', 'red'    :'\033[31m',
    'green':'\033[32m', 'yellow' :'\033[33m',
    'blue' :'\033[34m', 'magenta':'\033[35m',
    'cyan' :'\033[36m', 'white'  :'\033[37m',
    'reset':'\033[0m'
    }
    code = ''
    if reset:
       code = color_codes['reset']
    elif fg:
       code = color_codes.get(fg, '')
    elif bg:
       code = f'\033[4{color_codes.get(bg, "")[3:].replace("m", "")}m'
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

import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'

import time
start_time = time.time()

import shuw
os.system(f'shuw.py ffmpeg')

def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    info = []
    home = os.environ['HOME']
    symdir = f'{home}/symlink'
    source_path = next((arg for arg in args if os.path.isfile(arg)), sys.argv[0])
    if not source_path.endswith('.py'):
       return
    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = f'{symdir}/{lpbn}'
    if not os.path.isdir(symdir):
       os.mkdir(symdir)
    if os.path.exists(link_path):
       if not os.path.islink(link_path):
            os.remove(link_path)
    try:
       os.symlink(source_path, link_path)
    except Exception:
       pass
    if os.path.islink(link_path):
       info.append(f"Symbolic link '{link_path}' exists.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()

args = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr}audio-converter {frs}
 function: {fyl}convert audio files to different formats {frs}
    usage: {frs} {sbn} [file]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here

import os
import subprocess
import argparse
import sys

def get_clipboard_content():
    try:
        result = subprocess.run(['am', 'get-clipboard'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None
    except Exception as e:
        print(f"Error getting clipboard content: {e}")
        return None

# ... (get_clipboard_content function remains unchanged) ...

def convert_audio(input_file, output_format, bitrate, sample_rate, extra_params=""):
    """Converts an audio file with bitrate, sample rate, and additional parameters."""
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}.{output_format}"
    if output_format == 'mp3':
       encoder = 'libmp3lame'
    elif output_format == 'm4a':
       encoder = 'aac'
    elif output_format == 'flac':
       encoder = 'flac'
    elif output_format == 'ogg':
       encoder = 'vorbis'
    elif output_format == 'opus':
       encoder = 'opus'
       sample_rate = '48000'
    elif output_format == 'wav':
       encoder = 'adpcm_ima_wav'
    else:
       encoder = output_format

    if ext.lower()[1:] == output_format.lower():
        print(f"Error: Input file is already in '{output_format}' format. Skipping.")
        return True

    try:
        print(f"Converting '{input_file}' to '{output_file}' ({bitrate}, {sample_rate} Hz)...")
        #command = ["ffmpeg", "-i", input_file, "-vn", '-strict', '-2', "-acodec", encoder]
        command = ["ffmpeg", "-i", input_file, "-vn", '-strict', '-2', '-y']
        if bitrate == 'default':
           pass
        else:
           command.extend(['-ab', f'{bitrate}'])
        if sample_rate == 'default':
           pass
        else:
           command.extend(['-ar', f'{sample_rate}'])
        if extra_params == 'none':
           pass
        else:
           command.extend(extra_params.split())
        command.extend([output_file])
        subprocess.run(command, check=True)
        print(f"Conversion complete. File saved as '{output_file}'.")
        return True
    except FileNotFoundError:
        print("ffmpeg not found. Please install it using your package manager (e.g., 'pkg install ffmpeg').")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def batch_convert_directory(directory, output_format, bitrate, sample_rate, extra_params=""):
    bci = inspect.cleandoc(f'''
    dir: {directory}
    bitrate: {bitrate}
    sample_rate: {sample_rate}
    extra_params: {extra_params}
    ''')
    print(f'batch_convert_info:\n{bci}')
    #input(f'press Enter');sys.exit()
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.flac', '.mp3', '.m4a', '.ogg', '.opus', '.wav')):
            filepath = os.path.join(directory, filename)
            if convert_audio(filepath, output_format, bitrate, sample_rate, extra_params):
                pass
            else:
                return False
    return True

# ... (rest of the script remains largely the same, but you'll need to pass the sample_rate to functions) ...

if __name__ == "__main__":
    # ... (argument parsing remains the same) ...
    parser = argparse.ArgumentParser(description="Convert audio file format.")
    parser.add_argument("input", nargs="?", help="Input audio file or directory path (optional)")
    args = parser.parse_args()

    input_path = args.input
    if not input_path:
        clipboard_content = get_clipboard_content()
        if clipboard_content:
            input_path = clipboard_content
        else:
            input_path = input("Enter the path to the input audio file or directory: ")

    if not os.path.exists(input_path):
        print(f"Error: Path '{input_path}' not found.")
        sys.exit(1)

    is_directory = os.path.isdir(input_path)

    while True:
        print("\nSelect the output audio format:")
        print("1. mp3")
        print("2. m4a")
        print("3. flac")
        print("4. ogg")
        print("5. opus")
        print("6. wav")
        print("q. Quit")
        # ... (format selection remains the same) ...

        choice = input("Enter your choice: ").lower()
        if choice == 'q':
           break
        # ... (quit and invalid choice handling remains the same) ...
        elif choice in ('1', '2', '3', '4', '5', '6'):
            output_formats = {'1': 'mp3', '2': 'm4a', '3': 'flac', '4': 'ogg', '5': 'opus', '6': 'wav'}
            output_format = output_formats[choice]
            
            params = inspect.cleandoc(f'''
            \nSelect parameter profile:
             1. no_parameters
             2. custom_parameters
            ''')
            choice = input(f'{params}\nEnter your choice: ')
            if choice in '1':
               bitrate = 'default'
               sample_rate = 'default'
               extra_params = 'none'
            else:
               bitrate = input("Enter the desired bitrate (e.g., 128k, 192k, 320k, default is 128k): ") or "128k"
               sample_rate = input("Enter the desired sample rate (e.g., 44100, 48000, default is 44100): ") or "44100"
               extra_params = input("Enter any additional ffmpeg parameters (e.g., '-filter:a \"volume=2\"' ): ")

            if is_directory:
                if batch_convert_directory(input_path, output_format, bitrate, sample_rate, extra_params):
                    print("Batch conversion complete.")
                    break
                else:
                    print("Batch conversion failed. See error messages above.")
                    break
            else:
                if convert_audio(input_path, output_format, bitrate, sample_rate, extra_params):
                    break
        # ... (rest of the while loop remains the same) ...
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
