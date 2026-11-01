#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import inspect

# Standard ANSI escape codes for clean Termux output
BLUE = '\033[94m'
RESET = '\033[0m'

def osl(*args):
    """Creates or updates a symbolic link for a file in the ~/symlink directory."""
    messages = []
    home = os.environ.get('HOME')
    
    if not home:
        return ["Error: HOME environment variable not set."]

    symdir = os.path.join(home, 'symlink')
    
    # Determine absolute source path
    if args:
        source_path = os.path.abspath(args[0])
    else:
        source_path = os.path.abspath(sys.argv[0])

    if not os.path.isfile(source_path):
        return [f"Error: Source file '{source_path}' does not exist."]

    if not source_path.endswith('.py'):
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        extinfo = inspect.cleandoc(f'''[{os.path.join(script_dir, script_name)}]
        Source file must have a .py extension.
        ''')
        return [extinfo]

    # Target link path preparation (removes .py extension for the symlink name)
    link_name = os.path.basename(source_path).rsplit('.', 1)[0]
    link_path = os.path.join(symdir, link_name)

    # Ensure symlink target directory exists
    try:
        os.makedirs(symdir, exist_ok=True)
    except OSError as e:
        return [f"Error creating directory {symdir}: {e}"]

    # Handle pre-existing files or links
    if os.path.exists(link_path) or os.path.islink(link_path):
        if os.path.islink(link_path):
            current_target = os.readlink(link_path)
            
            # If it already points to the correct file, do nothing
            if os.path.abspath(current_target) == source_path:
                messages.append(f"Symlink already up to date: '{link_path}' -> '{source_path}'")
                return messages
            
            # If it points to a WRONG file, delete it so it can be overwritten
            try:
                os.remove(link_path)
                messages.append(f"Removed outdated symlink pointing to: {current_target}")
            except OSError as e:
                return [f"Error removing outdated symlink {link_path}: {e}"]
        else:
            # Handle the case where a regular file blocks the symlink path
            try:
                os.remove(link_path)
                messages.append(f"Removed blocking non-link file at {link_path}")
            except OSError as e:
                return [f"Error removing blocking file {link_path}: {e}"]

    # Create the symbolic link
    try:
        os.symlink(source_path, link_path)
        if os.path.islink(link_path):
            messages.append(f"Symbolic link '{link_path}' updated successfully to target '{source_path}'.")
        else:
            messages.append(f"Failed to verify symbolic link '{link_path}'.")
    except OSError as e:
        messages.append(f"Failed to create symbolic link '{link_path}': {e}")

    return messages

if __name__ == "__main__":
    cli_args = sys.argv[1:]
    results = osl(*cli_args) if cli_args else osl()
    
    for message in results:
        print(message)
