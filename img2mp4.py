#!/data/data/com.termux/files/usr/bin/python
import os, sys, time
import colorama, inspect
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

try: import osl
except: pass 

def exargs():
    return ' '.join(sys.argv[1:])

# specify your image directory path here
image_folder = exargs()

# specify the fps for the mp4 video
fps = 16

# get all file names in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
images.sort()

# specify the duration (in seconds) for each image in the video
image_duration = 2

# get the path of the last image added
last_image_path = os.path.join(image_folder, images[-1])
last_image_name = os.path.basename(last_image_path)

# specify the output video file with the last image's name
output_file = os.path.join(image_folder, last_image_name.split('.')[0] + '.mp4')
print(f'output_file: {output_file}')

# create a video from the images using FFmpeg
try:
    import subprocess
    ffmpeg_cmd = f"ffmpeg -framerate {fps} -i '{os.path.join(image_folder, 'image-%04d.%s')}' -t {len(images) * image_duration} -c:v libx264 -crf 23 -vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2' '{output_file}'"
    subprocess.call(ffmpeg_cmd, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error creating video: {e}")

if __name__ == '__main__':
    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
