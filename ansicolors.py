def ansi_color(fg=None, bg=None, reset=False):
    """
    Generates ANSI escape codes for text color.

    Args:
        fg: Foreground color (string, e.g., 'red', 'green').
        bg: Background color (string, e.g., 'red', 'green').
        reset: If True, returns the reset code.

    Returns:
        ANSI escape code string.
    """
    color_codes = {
        'black': '\033[30m', 'red'    : '\033[31m',
        'green': '\033[32m', 'yellow' : '\033[33m',
        'blue' : '\033[34m', 'magenta': '\033[35m',
        'cyan' : '\033[36m', 'white'  : '\033[37m',
        'reset': '\033[0m'
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
frs = ansi_color(reset=True)  # More efficient way to get the reset code

bbk = ansi_color(bg='black')
brd = ansi_color(bg='red')
bgr = ansi_color(bg='green')
bcy = ansi_color(bg='yellow')
bbl = ansi_color(bg='blue')
bmg = ansi_color(bg='magenta')
bwh = ansi_color(bg='white')
brs = ansi_color(reset=True) # More efficient way to get the reset code

""" how to use:
from ansicolors import frd, fgr, frs  # Import the specific colors you need
from ansicolors import * # if u want to import all

print(f"{frd}This is red text{frs}")
print(f"{fgr}This is green text{frs}")
"""