#!/usr/bin/env python3
import os
import re
import sys
import time

def find_in_files_colored(pattern, directory):
    """Searches for a pattern in files and highlights matches in red."""
    # ANSI colors
    RED = '\033[31m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Verbose: indicate current file being processed
            print(f"{RED}Searching:{RESET} {filepath}", end='\r', flush=True)
            
            # Skip binary/compressed files
            if filename.endswith(('.pyc', '.zip', '.exe', '.bin')):
                continue

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                    found_in_file = False
                    for line_num, line in enumerate(file, 1):
                        if match := re.search(pattern, line):
                            if not found_in_file:
                                # Clear the "Searching:" line before printing result
                                print(' ' * 80, end='\r') 
                                print(f'\n{YELLOW}filepath: {filepath}{RESET}')
                                found_in_file = True
                            
                            # Highlight matching string in red
                            highlighted = line.replace(
                                match.group(0), 
                                f"{RED}{match.group(0)}{RESET}"
                            )
                            print(f"{YELLOW}{line_num}{RESET}: {highlighted.strip()}")
            except Exception:
                continue
    print('\n' + RED + 'Done' + RESET)

if __name__ == '__main__':
    start_time = time.time()
    
    # Handle arguments
    args = sys.argv[1:]
    search_term = ' '.join(args).strip() if args else ""
    
    if not search_term:
        search_term = input('search term: ').strip()
    
    if not search_term:
        print("Usage: fnst.py [search term]")
        sys.exit(1)

    find_in_files_colored(search_term, ".")
    
    elapsed_time = time.time() - start_time
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")