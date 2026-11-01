#!/data/data/com.termux/files/usr/bin/bash
export cfub=/data/data/com.termux/files/usr/bin
export d0=$(dirname $0)
export b0=$(basename $0)
export red="\e[31m"
export grn="\e[32m"
export blu="\e[34m"
export yel="\e[33m"
export prp="\e[35m"
export cyn="\e[36m"
export nll="\e[0m"

usage(){
 echo -e "usage: ${b0} <file> <type>"
}

if [[ "$1" = "t" ]]; then
    arg1="$(tcg)"
else
    arg1="$1"
fi

arg2="${2:-*/*}"

if [[ -z "$arg1" ]]; then
    echo "usage: $(basename "$0") <file> <type>"
    exit 1
fi

su -c "am start -a 'android.intent.action.SEND' -d 'file://$arg1' -t '$arg2' --eu 'android.intent.extra.STREAM' 'file://$arg1'" 