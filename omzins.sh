#!/usr/bin/env bash
apt update -y
apt upgrade -y
apt install busybox git python wget zsh -y
apt install silversearcher-ag -y
pip install colorama -y
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
if [[ -d $HOME/closbox ]]; then
   $HOME/closbox/zrcu.py
fi