#!/data/data/com.termux/files/usr/bin/bash
exit
export dn0=$(dirname $0)/
export lrc=${dn0}lp.raw.csv
export lrcb=${dn0}lp.raw.csv.bak
if [[ ! -d $lrcb ]]; then
cp -v "$lrc" "$lrcb"
fi

awk1(){
for a in $(cat ${lrcb}); do
export fld1=$(echo "$a" | awk -F'_' '{print $1"+"$2"+"$3"+"$4}')
export fld11=$(echo "$a" | awk -F'_' '{print $1}')
export fld2=$(echo "$a" | awk -F'_' '{print $2}')
export fld3=$(echo "$a" | awk -F'_' '{print $3}')
export fld4=$(cat "$lrc" | awk -F'.' '{print $4}')
for b in ${fld11}; do
export a1=$(echo "$b" | awk -F'.' '{print $1}')
export a2=$(echo "$b" | awk -F'.' '{print $2}')
export a3=$(echo "$b" | awk -F'.' '{print $3}')
export a4=$(echo "$b" | awk -F'.' '{print $4}')
if [[ ${a4} = "Mon" ]]; then
 echo "$a"
else
 echo -e "${a1}.${a2}.${a4}.${a3}_${fld2}_${fld3}"
fi
done
done
}

awk1 | tee "$lrc"
