#!/data/data/com.termux/files/usr/bin/bash
apt update
apt install busybox git python wget zsh
apt install silversearcher-ag
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
if [[ -d $HOME/bin ]]; then
   $HOME/bin/zrcu.py
fi