#!/data/data/com.termux/files/usr/bin/bash
apt update
apt install jq
export bn0=$(basename $0)
export dn0=$(dirname $0)
export red="\e[31m"
export grn="\e[32m"
export blu="\e[34m"
export yel="\e[33m"
export prp="\e[35m"
export cyn="\e[36m"
export nll="\e[0m"
export arg="$*"
tdt(){ termux-dialog text -t $1 -i $2; }

if [[ "$arg" = "t" ]]; then export arg=$(tcg); fi
if [[ -d "$arg" ]]; then cd "$arg"; fi
echo -e "--BatchRenamer"
echo -e "--usage: $bn0 [dir|t|\$(tcg)]"
echo -e "--current dir: $(pwd)"
echo -e "--press Enter "
read
fd
ls

PS3="--[ batch.rename ].Command: "
select action in replace quit; do
case $action in
replace)
r1r2(){
export r1=$(
echo $(tdt replace.this.word word.to.replace) | \
awk -F'"' '{print $6}')
echo -e "r1=$r1"

export r2=$(
echo $(tdt replace.with.this.word replacement) | \
awk -F'"' '{print $6}')
echo -e "r2=$r2"
}

export reps=$(
termux-dialog text -i 'type here' \
-m -t 'line1=text-to-replace,line2=replacement-entry' | \
jq -r '.text' \
)
echo "reps=${reps}"
var1=0
for r in ${reps}; do
    if [[ ${var1} == 0 ]]; then
       var1=${r}
       echo "var1:${var1}"
       continue
    fi
    if [[ ! ${var1} == 0 ]]; then
       var2=${r}
    fi
done

echo "var1=${var1},var2=${var2}"
if [[ -s ${var2} ]]; then
   echo "var2 is empty"
   exit
fi
break
;;
quit) exit;;
esac
done

echo -e "replace ($var1) with ($var2)"
for a in *; do
export nn=$(echo -e "$a" | sed "s/$var1/$var2/g")
if [[ "$a" = "$nn" ]]; then
echo -e "${blu}no.change${nll}: $a"
else
echo -e "--${yel}oldname${nll}: $a"
echo -e "--${prp}newname${nll}: $nn${nll}"
fi
done

PS3="--[ awaiting.your ].Command: "
select a1 in execute quit; do
case $a1 in
execute) export exe=yes; 
for a in *; do
export nn=$(echo $a | sed "s/$var1/$var2/g")
#$ee "renaming ($a) to ($nn)"
[[ "$a" = "$nn" ]] || mv -v "$a" "$nn"
done
break;;
quit) exit;;
esac
done
