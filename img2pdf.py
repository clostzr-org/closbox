#!/usr/bin/env python3
"""Convert images in a folder to a single PDF (newest image first)."""
import sys
import time
from datetime import datetime
from pathlib import Path

from PIL import Image

IMAGE_EXTS = {'.jpg', '.jpeg', '.png'}


def convert_images_to_pdf(image_folder: str) -> None:
    folder = Path(image_folder)
    if not folder.is_dir():
        sys.exit(f"Error: '{image_folder}' is not a valid directory.")

    # Sort by modification time, newest first
    images = sorted(
        (p for p in folder.iterdir() if p.suffix.lower() in IMAGE_EXTS),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not images:
        print("No images found in the specified folder.")
        return

    # Setup output directory relative to current working directory
    output_dir = Path.cwd() / "img2pdf.output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"scanned_{timestamp}.pdf"

    # Open lazily and close properly to keep memory usage low
    opened = []
    try:
        # Convert to RGB to ensure compatibility with PDF format (handles RGBA/PNG)
        first = Image.open(images[0]).convert('RGB')
        opened.append(first)
        
        for path in images[1:]:
            img = Image.open(path).convert('RGB')
            opened.append(img)
            
        first.save(output_file, save_all=True, append_images=opened[1:])
    except Exception as e:
        sys.exit(f"Error creating PDF: {e}")
    finally:
        for img in opened:
            img.close()

    print(f"PDF created successfully: {output_file} ({len(images)} pages)")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).stem} <image_folder>")
        sys.exit(1)

    start = time.time()
    convert_images_to_pdf(sys.argv[1])
    print(f"Elapsed time: {time.time() - start:.2f} seconds")
