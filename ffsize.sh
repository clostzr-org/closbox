#!/data/data/com.termux/files/usr/bin/bash
. color
export cfub=/data/data/com.termux/files/usr/bin
export bbds=$(busybox date -D %z | sed -e 's/  /./g' -e 's/ /./g' -e 's/://g' )
export xst=/storage/0403-0201
export pgc=$(ping -c 1 www.google.com && { echo "#connected"; })
export epg=$(echo $pgc | awk -F'#' '{print $2}')
export slm="su -lmM -c"
export e="echo -e"
export d0=$(dirname $0)
export b0=$(basename $0)
export a1="$a1"
export a2="$a2"
export a3="$a3"
export a4="$a4"

usg(){
$e "usage: $b0 <dir|file|t> <size>"
}

if [[ -z "$1" ]]; then
usg; exit
fi

if [[ "$a1" = "t" ]]; then
export arg1="$(tcg)"
fi

vsize(){
if [[ -f "$1" ]]; then
ffprobe \
-v error \
-select_streams v:0 \
-show_entries stream=width,height \
-of csv=s=x:p=0 \
"$1"
fi
}

vsinfo(){
vw(){ $e "$(vsize $1)" | awk -F'x' '{print $1}'; }
vh(){ $e "$(vsize $1)" | awk -F'x' '{print $2}'; }
export vwNew=$(($(vw $1)/8*6))
export vhNew=$(($(vh $1)/8*6))
$e "...file:${G}$(basename $1)${N}"
$e "oldSize:$(vw $1)x$(vh $1)"
$e "newSize:${vwNew}x${vhNew}\n"
}

sel1(){
PS3="Your.command: "
select act in confirm quit; do
case $act in
confirm) break;;
quit) exit;;
esac
done
}

ffrs(){
if [[ -n "$(echo $1 | grep '.vSize(')" ]]; then
export avs=$(echo $1 | awk -F'.vSize(' '{print $1}')
fi
if [[ -n "$avs" ]]; then
export file="$avs.${1##*.}"
else
export file="$1"
fi
if [[ -f "$1" ]]; then
ffmpeg \
-i "$file" \
-s ${vwNew}x${vhNew} \
"${file%.*}.vSize(${vwNew}x${vhNew}).${file##*.}"
fi
}

if [[ -d "$arg1" ]]; then
cd "$arg1"
fd "$arg1"
for a in *.*; do
vsinfo "$a"
done

sel1

for a in *.*; do
vsinfo "$a"
ffrs "$a"
done

fi

if [[ -f "$arg1" ]]; then
vsinfo "$arg1"
sel1
ffrs "$arg1"
fi
