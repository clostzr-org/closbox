#!/data/data/com.termux/files/usr/bin/bash
export R="\e[31m" ;
export G="\e[32m" ;
export Y="\e[33m" ;
export B="\e[34m" ;
export P="\e[35m" ;
export C="\e[36m" ;
export N="\e[0m"  ;
apt update && apt upgrade
pkg upgrade
pak_tm="
wget
busybox
git
7zip
android-tools
aapt
elinks
jpegoptim
links
man
micro
mpv
mount-utils
optipng
rclone
termux-api
translate-shell
zsh
play-audio
python
python-pip
"

for p in ${pak_tm}; do
 echo -e "${Y}installing $p ${N} ..."
 apt install "$p" -y
done

apt-get install silversearcher-ag

pak_py="
apkfile
boot
bs4
colorama
ffmpeg-python
imageio==2.0.0
numpy
pyzipper
python-android
requests
yt-dlp
"

for p in ${pak_py}; do
 echo -e "${R}now executing: pip install --upgrade $p ${N} ..."
 pip install --upgrade "$p"
done

pkg autoclean
apt autoremove

echo -e "${Y}batch install done ${N}"
