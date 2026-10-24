#!/data/data/com.termux/files/usr/bin/bash
longer(){
# filename desymbolizer
usg(){
echo -e "filename desymbolizer - strip all non-alphanumerics
--usage: $(basename $0) [filename]" && exit
}
if [[ "$1" == "" ]]; then usg; fi
#echo "allparameter=$@ | parameter1=$1"
#echo -e "pwd=$(pwd)"
export on1="$*"
export nn1=$(echo "$on1" | sed \
-e 's:\[:\(:g' -e 's:\]:\):g' \
-e 's/[^a-zA-Z0-9/(/)#+~.-]/_/g' \
-e 's:(:\[:g' -e 's:):\]:g'
)
#echo -e "oldname=$on1"
#echo -e "newname=$nn1"
echo "$nn1"
exit
}

h1='
Heres a shortened version of the script:
'
if [[ "$1" == "" ]]; then 
echo -e "filename desymbolizer - strip all non-alphanumerics\n--usage: $(basename $0) [filename]" && exit; fi
echo "$*" | sed -E 's/[^a-zA-Z0-9\/\(\)\#\+~\.\-\[\]]/_/g'
h2='
This version removes the  usg()  function and 
the unnecessary  export  statements, and simplifies 
the  sed  command to use extended regular expressions with the  -E  flag.
'