#!/data/data/com.termux/files/usr/bin/bash

# Set the directory where the videos are located
video_dir="/path/to/video/directory"

# Loop through all files in the directory
for file in "$video_dir"/*
do
    # Check if the file is a regular file (not a directory)
    if [ -f "$file" ]; then
        # Check the file extension to make sure it's a video file
        if [[ "$file" == *.mp4 || "$file" == *.avi || "$file" == *.mov || "$file" == *.mkv ]]; then
            # Get the original resolution of the video
            resolution=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$file")
            width=$(echo $resolution | cut -d'x' -f1)
            height=$(echo $resolution | cut -d'x' -f2)

            # Check if the resolution is greater than 1000x2000 or 2000x1000
            if [[ ($width -gt 1000 && $height -gt 2000) || ($width -gt 2000 && $height -gt 1000) ]]; then
                # Calculate the new resolution
                new_width=$((width / 2))
                new_height=$((height / 2))

                # Resize the video using ffmpeg
                ffmpeg -i "$file" -vf "scale=$new_width:$new_height" -c:a copy "resized_${file##*/}"
                echo "Resized $file to $new_width x $new_height"
            else
                echo "$file is already smaller than 1000x2000 or 2000x1000, skipping..."
            fi
        fi
    fi
done
