#!/usr/bin/env python3
"""
PDF → Image Converter for Termux
--------------------------------
- Clipboard first: if clipboard contains a PDF file path → convert that file.
                   if clipboard contains a directory path → convert all PDFs inside.
- Arguments second:
    d {dir}       → convert all PDFs in directory
    f {file}      → convert single PDF
    fmt={ext}     → set output format (png/jpg)
- Output images are named <pdfname>_page_<n>.<ext> in the same location.
- Auto-installs dependencies if missing.
"""

import os, sys, subprocess, time

start_time = time.time()

# Dependencies
REQUIRED_PYTHON_PACKAGES = ["pdf2image"]
REQUIRED_TERMUX_PACKAGES = ["poppler"]

def install_termux_packages():
    for pkg in REQUIRED_TERMUX_PACKAGES:
        try:
            subprocess.run(["pkg", "install", "-y", pkg], check=True)
        except Exception as e:
            print(f"Failed to install {pkg}: {e}")

def install_python_packages():
    for pkg in REQUIRED_PYTHON_PACKAGES:
        try:
            __import__(pkg)
        except ImportError:
            print(f"Installing Python package: {pkg}")
            subprocess.run([sys.executable, "-m", "pip", "install", pkg], check=True)

def get_clipboard():
    try:
        result = subprocess.run(["termux-clipboard-get"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Clipboard read failed: {e}")
        return ""

def convert_pdf(pdf_path, fmt="png"):
    from pdf2image import convert_from_path
    if not os.path.isfile(pdf_path) or not pdf_path.lower().endswith(".pdf"):
        print(f"Invalid PDF file: {pdf_path}")
        return
    print(f"Processing: {pdf_path}")
    try:
        pages = convert_from_path(pdf_path)
        base_name = os.path.splitext(pdf_path)[0]

        # Normalize format: Pillow expects "JPEG" not "JPG"
        fmt_map = {"jpg": "JPEG", "jpeg": "JPEG", "png": "PNG"}
        fmt_upper = fmt_map.get(fmt.lower(), fmt.upper())

        for i, page in enumerate(pages, start=1):
            img_name = f"{base_name}_page_{i}.{fmt.lower()}"
            page.save(img_name, fmt_upper)
            print(f"Saved: {img_name}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        
def convert_dir(dir_path, fmt="png"):
    if not os.path.isdir(dir_path):
        print(f"Invalid directory: {dir_path}")
        return
    pdfs = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.lower().endswith(".pdf")]
    if not pdfs:
        print("No PDF files found in directory.")
        return
    for pdf in pdfs:
        convert_pdf(pdf, fmt)

def parse_args(args):
    fmt = "png"
    target = None
    mode = None
    for arg in args:
        if arg.startswith("fmt="):
            fmt = arg.split("=", 1)[1].lower()
        elif arg == "f" and len(args) > args.index(arg)+1:
            mode = "file"
            target = args[args.index(arg)+1]
        elif arg == "d" and len(args) > args.index(arg)+1:
            mode = "dir"
            target = args[args.index(arg)+1]
    return mode, target, fmt

def main():
    install_termux_packages()
    install_python_packages()

    args = sys.argv[1:]
    mode, target, fmt = parse_args(args)

    # Clipboard first
    clip = get_clipboard()
    if clip:
        if os.path.isfile(clip) and clip.lower().endswith(".pdf"):
            convert_pdf(clip, fmt)
        elif os.path.isdir(clip):
            convert_dir(clip, fmt)
        else:
            print("Clipboard does not contain a valid PDF file or directory path.")
            if mode == "file" and target:
                convert_pdf(target, fmt)
            elif mode == "dir" and target:
                convert_dir(target, fmt)
            else:
                print("Usage: f {file} or d {dir} [fmt=png|jpg]")
    else:
        # No clipboard, fallback to arguments
        if mode == "file" and target:
            convert_pdf(target, fmt)
        elif mode == "dir" and target:
            convert_dir(target, fmt)
        else:
            print("No clipboard content and no valid arguments provided.")

    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()