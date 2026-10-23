#!/data/data/com.termux/files/usr/bin/bash
#termux-change-repo
export cfub=/data/data/com.termux/files/usr/bin
export h=/data/data/com.termux/files/home
export hc=/data/data/com.termux/files/home/.cache/pip
export hb=/data/data/com.termux/files/home/bin
export tca=/data/data/com.termux/cache/apt
export tcapc=/data/data/com.termux/cache/apt/pkgcache.bin
export tcaspc=/data/data/com.termux/cache/apt/srcpkgcache.bin
export tca=/data/data/com.termux/cache/apt
export tcaa=/data/data/com.termux/cache/apt/archives
export tcpip=/data/data/com.termux/cache/pip
export tmpt=/data/data/com.termux/files/usr/tmp
export eche="echo -e"
export sulm="su -lm -c"

_fch(){
export wai=$(whoami)
chown -Rv $wai:$wai $h
chown -Rv $wai:$wai $hb
chown -Rv $wai:$wai_cache $tca
if [[ -d "$hc" ]]; then
 chmod -v 755 $hc
 chown -Rv $wai:$wai_cache $hc
fi
if [[ -d "$tcpip" ]]; then
 chmod -v 755 $tcpip
 chown -Rv $wai:$wai_cache $tcpip
fi
chmod -v 755 $tmpt
chown -Rv $wai:$wai $tmpt

$eche "==done."
sleep 2

if [[ -f "$h/.profile" ]]; then
	$eche "==.profile exist"
	sleep 2
fi
$eche "==updating .profile..."

cat >"$h/.profile"<<EOF
export hb=\$HOME/bin
export PATH=\$PATH:\$hb
export fub=/data/data/com.termux/files/usr/bin
export xst=\$(extSd)
export R="\e[31m"
export G="\e[32m"
export B="\e[34m"
export Y="\e[33m"
export P="\e[35m"
export C="\e[36m"
export N="\e[0m"
export micro="micro -clipboard internal"
EOF
$eche "==new.profile.content:"
cat $h/.profile
$eche "==all.done"
}

_appendz(){
cat >>"$h/.zshrc"<<EOF
export PATH=\$PATH:~/bin
export fub=/data/data/com.termux/files/usr/bin
export xst=\$(extSd)
mkdir -p "$HOME/.bookmarks"
if [ -d "$HOME/.bookmarks" ]; then
    export CDPATH=".:$HOME/.bookmarks:/"
    alias goto="cd -P"
fi
_goto()
{
local IFS=$'\n'
COMPREPLY=( $( compgen -W "$(/bin/ls ~/.bookmarks)" ${COMP_WORDS [COMP_CWORD]}))
} && complete -F _goto goto
pfb(){ printf "%b\n" "$@"; }
export R="\e[31m"
export G="\e[32m"
export B="\e[34m"
export Y="\e[33m"
export P="\e[35m"
export C="\e[36m"
export N="\e[0m"
export micro="micro -clipboard internal"
cd ~/bin
EOF
}

_fch

if [[ $(grep "fub=" "$h/.zshrc") ]]; then
 export found="true"
 _appendz
else
 export found="false"
 _appendz
fi
#echo "found=$found"
#cat "$h/.zshrc"
