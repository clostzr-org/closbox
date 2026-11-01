#!/data/data/com.termux/files/usr/bin/python
import os
import sys
from ansicolors import *
info = []  # Initialize info outside the function
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'


def osl(*args):
    """Creates a symbolic link for the given file in the symlink directory."""
    global info
    home = os.environ.get('HOME')  # Use get to avoid KeyError if HOME is not set
    if  not home:
        info.append("Error: HOME environment variable not set.")
        return

    symdir = os.path.join(home, 'symlink')  # Use os.path.join for cross-platform compatibility
    
    # Determine the source path. If arguments are provided and one of them is a file, use that.
    # Otherwise, if the script is run directly, use the script's path.
    if args:
        source_path = next((arg for arg in args if os.path.isfile(arg)), None)
    else:
        source_path = sys.argv[0] if __name__ == "__main__" else None  # Only use script path if run directly

    if  not source_path:
        info.append("No valid source file provided.")
        return

    if not source_path.endswith('.py'):
       import inspect
       extinfo = inspect.cleandoc(f'''[{sdbne}]
       Source file must have a .py extension.
       ''')
       info.append(extinfo)
       return

    lpbn = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = os.path.join(symdir, lpbn)

    # Ensure the symlink directory exists
    if not os.path.isdir(symdir):
        try:
            os.makedirs(symdir, exist_ok=True)  # Create directory and handle potential errors
        except OSError as e:
            info.append(f"Error creating directory {symdir}: {e}")
            return

    # Handle existing files/links
    if os.path.exists(link_path):
       if os.path.islink(link_path):
          readln = os.readlink(link_path)
          print(f'current symlink source: {readln}')
          return
       if not os.path.islink(link_path):
          try:
              os.remove(link_path) # Remove non-link file
          except OSError as e:
              info.append(f"Error removing existing file {link_path}: {e}")
              return
       else:
          info.append(f'[{sne}]-{fbl}{link_path}{frs} exists')
          return "link exists"

    # Create the symbolic link
    try:
        os.symlink(os.path.abspath(source_path), link_path)  # Use absolute path
    except OSError as e:
        info.append(f"Failed to create symbolic link '{link_path}': {e}")
        return

    if  os.path.islink(link_path):
        info.append(f"Symbolic link '{link_path}' created successfully.")
    else:
        info.append(f"Failed to create symbolic link '{link_path}'.")


if  __name__ == "__main__":
    osl(*sys.argv[1:])  # Pass command line arguments to osl
    for message in info:
        print(message)
        
''' usage:
import osl
osl.osl(sys.argv[0])
for message in osl.info:
    print(message)
'''