#!/data/data/com.termux/files/usr/bin/bash
if [[ $1 = "t" ]]; then
arg1=$(tcg)
else
arg1="$1"
fi

if [[ -f $arg1 ]]; then
ffmpeg -i "$arg1" -filter:a volumedetect -f null /dev/null
else
echo -e "__missing arguments."
fi
