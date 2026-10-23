#!/data/data/com.termux/files/usr/bin/bash
export cfub=/data/data/com.termux/files/usr/bin
export e="echo -e"
export red="\e[31m"
export grn="\e[32m"
export yel="\e[33m"
export blu="\e[34m"
export prp="\e[35m"
export cyn="\e[36m"
export nll="\e[0m"
export ldir="/sdcard/Documents/linksdump"

if [[ ! -d $ldir ]]; then
 mkdir -p "$ldir"
fi

if [[ -n "$*" ]]; then
 export arg="$*"
fi

xsd(){
dfx=$(df | grep -E "/storage/*-*" | awk '{print $6}')
for d in ${dfx}; do
    if [[ ${d} == *-* ]]; then
       xsd=${d}
    fi
done
echo -e "$xsd"
}

apt install ffmpeg deno nodejs yt-dlp -y
pip install yt-dlp


xsd=$(xsd)
cfg_file="${0%.*}.txt"
echo "external_sd: ${xsd}"
echo "config_file: ${cfg_file}"

cat > "${cfg_file}" <<EOF
-c -i -o ${xsd}/Music/%(playlist_title)s/%(title)s.%(ext)s
EOF

loop(){
 $e "--${red}termux.url.opener$nll"
 echo -e "--${cyn}xsdcard: $(xsd)${nll}"
 echo -e "--${grn}url$nll: $arg"
 PS3="--what do you want with the url? "
 select action in \
 yt-dlp.noPlaylist \
 yt-dlp.yesPlaylist \
 yt-dlp.dlVideo \
 linksDump \
 play \
 quit
 do
 case $action in
      yt-dlp.noPlaylist)
        echo "--no-playlist"
        $HOME/bin/ytd.sh -x --no-overwrites --no-playlist "$arg" 
        loop "$arg"
      ;;
      yt-dlp.yesPlaylist)
        echo "--yes-playlist"
        jsr='--js-runtimes deno'
        cio="-c -i -o ${xsd}/Music/%(playlist_title)s/%(title)s.%(ext)s"
        ypl='-x --no-overwrites --yes-playlist --windows-filenames --max-filesize 16m'
        yt-dlp --config-location "${cfg_file}" $jsr $ypl "$arg"
        loop "$arg"
      ;;
      yt-dlp.dlVideo)
        $HOME/bin/ytd.sh -f mp4 "$arg"
        loop "$arg"
      ;;
      linksDump)
        apt update
        apt install links
        bn=$(basename $*)
        #nosym=$(dirname $0)/nosym
        #bnos=$($nosym "${bn}")
        bnos=$(echo "$bn" | sed -E 's/[^a-zA-Z0-9\/\(\)\#\+~\.\-\[\]]/_/g')
        links -dump "$*" | tee $ldir/${bnos}.txt
        links -source "$*" | tee $ldir/${bnos}.htm
        loop "$*"
      ;;
      play) 
        apt update
        apt upgrade -y
        apt install mpv
        mpv --loop-playlist --no-video --shuffle "$arg"
      ;;
      quit) 
        exit
      ;;
 esac
 done
}

loop "$arg"
