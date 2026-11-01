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

#insert_your_codes_here
def hex_to_dec(hex_num):
    """Converts a hexadecimal number to decimal."""
    return int(hex_num, 16)

def dec_to_hex(dec_num):
    """Converts a decimal number to hexadecimal."""
    return hex(dec_num)

def calculate(num1, num2, operator):
    """Performs basic arithmetic calculations, accepting hex or dec."""
    try:
        num1 = int(num1, 16) if num1.startswith("0x") else int(num1)
        num2 = int(num2, 16) if num2.startswith("0x") else int(num2)
    except ValueError:
        return "Invalid input. Please enter numbers (decimal or hex)."

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by zero error"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

while True:
    choice = input("Choose action (h: hex to dec, d: dec to hex, c: calculate, q: quit): ")

    if choice.lower() == 'h':
        hex_input = input("Enter hexadecimal number: ")
        dec_result = hex_to_dec(hex_input)
        print(f"Decimal: {dec_result}")

    elif choice.lower() == 'd':
        dec_input = int(input("Enter decimal number: "))
        hex_result = dec_to_hex(dec_input)
        print(f"Hexadecimal: {hex_result}")

    elif choice.lower() == 'c':
        num1 = input("Enter first number (decimal or hex): ")
        num2 = input("Enter second number (decimal or hex): ")
        operator = input("Enter operator (+, -, *, /): ")
        result = calculate(num1, num2, operator)
        hexres = hex(result)
        print(f"Result: {result} ({hexres})")

    elif choice.lower() == 'q':
        break

    else:
        print("Invalid choice. Please enter 'h', 'd', 'c', or 'q'.")

if __name__ == '__main__':
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
