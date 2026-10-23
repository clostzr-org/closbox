#!/data/data/com.termux/files/usr/bin/bash
func1(){
dfx=$(df | grep -E "/storage/*-*" | awk '{print $6}')
for d in ${dfx}; do
    if [[ ${d} == *-* ]]; then
       xsd=${d}
    fi
done
echo -e "${xsd}"
}

# Find external SD card mount point
dfga=$(df -h | grep -i "-" | awk '{print $6}')
for s in $dfga; do
  if [[ "$s" =~ "/storage/" && "$s" =~ "-" ]]; then
    #echo "Directory '$s' contains '/storage/' and '-'"
    echo "$s"
    break
  fi
done
