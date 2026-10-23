#!/data/data/com.termux/files/usr/bin/python
import os, subprocess, sys, time
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

import os
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = f'{home}/bak'

verbose = False

start_time = time.time()

import inspect
desc = inspect.cleandoc(f'''
    alias:{fgr}gemini prompt{frs}
 function:{fyl}ask gemini
''')
#print(f'{desc}')
    
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
       info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
       info.append(f"Failed to create symbolic link '{link_path}'.")
        
osl()
 
def usg():
    usg = inspect.cleandoc(f'''
    usage: {sbn} [option] [argument]
    options: -s speak
    ''')
    print(f'{usg}')

def exargs():
    args = ' '.join(sys.argv)
    args = args.replace(f'{sys.argv[0]} ', '')
    if args == sys.argv[0]:
       args = ''
    #os.system(f'cmd {args}')
    return args

args = sys.argv[1:]
if verbose == True:
   print(f'args: {args}')
 
#insert_your_codes_here
try:
 import requests
except Exception:
 os.system('pip install requests')
 import requests

def send_request(text):
    apikey = 'AIzaSyAjHiuSpA3cmgCDwYOCJNmI6bHLakvg2k8'
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=AIzaSyAjHiuSpA3cmgCDwYOCJNmI6bHLakvg2k8"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": text}]}]}
    response = requests.post(url, headers=headers, json=data)
    return response.text

import json

def format_json(data):
    """Formats JSON data into a stylized string with 'text' at the bottom, no borders."""

    output = ""
    
    data = json.loads(data)

    for key, value in data.items():
        output += f"{key.upper()}: \n"

        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for inner_key, inner_value in item.items():
                        if inner_key != 'text' and inner_key != 'parts' and inner_key != 'content':  # Exclude 'text', 'parts', and 'content' 
                            output += f"  {inner_key.upper()}: {inner_value}\n"
                else:
                    output += f"  {item}\n"
        elif isinstance(value, dict):
            for inner_key, inner_value in value.items():
                if inner_key != 'text' and inner_key != 'parts' and inner_key != 'content':  # Exclude 'text', 'parts', and 'content'
                    output += f"  {inner_key.upper()}: {inner_value}\n"
        else:
            output += f"  {value}\n"

    # Now print 'text' at the bottom for each candidate
    if 'candidates' in data:
        for candidate in data['candidates']:
            if 'content' in candidate and 'parts' in candidate['content']:
                for part in candidate['content']['parts']:
                    if 'text' in part:
                        output += f"  \nPROMPT:\n {text}\n"
                        output += f"  \nRESPONSE:\n {part['text']}\n"

    return output
    
try:
 from gtts import gTTS
except Exception:
 os.system(f'pip install gtts')
 from gtts import gTTS
 
import subprocess

def check_and_install_play_audio(output_file):
    """Checks if play-audio is installed and installs it if necessary."""

    try:
        # Check if play-audio is already installed.  We use a try-except block to handle potential errors.
        play = subprocess.run(['play-audio', output_file], capture_output=True, check=True, text=True)
        playout = play.stdout
        print("play-audio is already installed.")
        return 'installed'
    except FileNotFoundError:
        print("play-audio is not installed. Attempting to install...")
        try:
            # Attempt to install play-audio using apt.  The `-y` flag automatically answers "yes" to prompts.
            subprocess.run(['apt', 'update'], check=True) #update apt package list first
            play = subprocess.run(['apt', 'install', 'play-audio', '-y'], check=True)
            playout = play.stdout
            print("play-audio installed successfully.")
            print(f'{playout}')
        except subprocess.CalledProcessError as e:
            print(f"Error installing play-audio: {e}")
            print("Please check your internet connection and try again.  You may need root privileges (su).")
            return 'fail-to-install'
    except subprocess.CalledProcessError as e:
        print(f"Error checking play-audio version: {e}")
        return 'error-playing'
        
outdir = f'/sdcard/{sne}'
if not os.path.isdir(outdir):
   ods = 'not exist, creating...'
   os.makedirs(outdir, exist_ok=True)
   if os.path.isdir(outdir):
      ods = 'successfuly created'
   else:
      ods = 'makedir failed'
      print(f'outdir creation failed')
else:
   ods = 'exist'
print(f'output_dir: {outdir} | status:{fyl}{ods}{frs}')

def text_to_speech(response_data, language='en', output_file=f'{outdir}/{sne}-speech.mp3'):
    """Converts text to speech using gTTS."""
    #print(f'{frd}tts-response_data: {response_data}{frs}')
    if len(response_data) == 0:
       print(f'{frd}text_to_speech is not activated{frs}')
       return 1
    tts = gTTS(text=response_data["text"], lang=response_data["language"])
    tts.save(output_file)
    playstat = check_and_install_play_audio(output_file)
    print(f'play-audio_status: {playstat}')
    if playstat == 'installed':
       pass
    else:
       os.system(f"play-audio {output_file}")
    
def prompt_text(data):
    prompt_help = inspect.cleandoc(f'''
    \nGemini AI Assisstant
    type "-s[language-code] [text]" to activate tts mode
    default language: en
    type "exit" to quit
    ''')
    print(f'{prompt_help}')
    speech = data["speech"]
    if '-s' in speech:
     data["speech"] = speech
     language = speech[2:]
     data["language"] = language
    else:
     language = data["language"]
    text = data["text"]
    if text == '':
     rawdata = input("Enter your prompt: ")
    if verbose == True:
       print(f'rawdata: {rawdata}')
    try:
     if '-s' in rawdata.split()[0]:
      data["speech"] = rawdata.split()[0]
      data["language"] = rawdata.split()[0][2:]
      data["text"] = " ".join(rawdata.split()[1:])
     else:
      data["speech"] = ''
      data["language"] = ''
      data["text"] = " ".join(rawdata.split())
    except Exception:
     pass
    if data["language"] == '':
       data["language"] = 'en'
    info = inspect.cleandoc(f'''
    prompt_text var:
    speech: {data["speech"]}
    language: {data["language"]}
    text: {data["text"]}
    ''')
    if verbose == True:
     print(f'prompt_text data: {data}')
     print(f'prompt_text info:\n{info}')
    #sys.exit()
    return data
    
def response(data):
    speech = data["speech"]
    language = data["language"]
    text = data["text"]
    response = send_request(text)
    #print(f'{response}')
    json_data = response
    output = format_json(json_data)
    # Find the start of the "RESPONSE:" section
    start_index = output.find("RESPONSE:") + len("RESPONSE:")
    # Extract the text after "RESPONSE:"
    response_text = output[start_index:].strip()
    print(f'\nRESPONSE:\n\n{response_text}\n')
    if '-s' in speech:
     response_data = {"text":response_text.replace('*', ''), "language":language}
     #text_to_speech(response_data)
    else:
     response_data = ''
    return {"rt":response_text, "rd":response_data}
    
if __name__ == "__main__":
   try:
    speech = sys.argv[1]
    if '-s' in speech:
     language = speech[2:]
    else:
     language = ''
   except Exception:
    speech = ' '
   try:
    text = " ".join(sys.argv[2:])
   except Exception:
    text = ' '
   if '-s' in speech:
    language = language if 2 <= len(language) <= 5 or '-' in language else ''
   if not '-s' in speech:
    arg = f'{speech} '
    speech = ''
    language = ''
    text = f'{arg}' + text
   text = text.strip()
   if verbose == True:
      print(f'{frd}main args:\nspeech: {speech}\nlanguage: {language}\ntext: {text}')
      print(f'text.strip: "{text}" ')
   data = {"speech":speech, "language":language, "text":text}
   while True:
    if data["text"] == '':
     prompt = prompt_text(data)
    else:
     prompt = data
    speech = prompt['speech']
    language = prompt['language']
    text = prompt['text']
    info = inspect.cleandoc(f'''
    [info]
    prompt: {prompt}
    speech: {speech}
    language: {language}
    text: {text}
    ''')
    if verbose == True:
       print(f'{fmg}while true info:\n{info}')
    if text == 'exit':
       sys.exit()
    else:
       if not text.strip() == '':     
          resp = response(prompt)
          respt = resp["rt"]
          respd = resp["rd"]
          #print(f'{frd}resp:{resp}{frs}')
          sdgo = f'{outdir}/{sne}-output.md'
          with open(sdgo, 'w') as gout:
               gout.write(respt)
          act = 'com.lonelycatgames.Xplore/.ui.TextViewer'
          xtv = os.system(f'am start -n {act} -d file://{sdgo} --activity-clear-task')
          text_to_speech(respd)
       data = {'speech':'', 'language':'', 'text':''}

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
