#!/data/data/com.termux/files/usr/bin/bash
apt update -y
apt install busybox git python wget zsh -y
apt install silversearcher-ag -y
pip install colorama -y
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
if [[ -d $HOME/bin ]]; then
   $HOME/bin/zrcu.py
fi