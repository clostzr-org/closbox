#!/data/data/com.termux/files/usr/bin/bash
if [[ ! -s /data/data/com.termux/files/home/symlink/rcabt ]]; then
   ln -sv /data/data/com.termux/files/home/bin/rcabt.sh /data/data/com.termux/files/home/symlink/rcabt
   if [[ -s /data/data/com.termux/files/home/symlink/rcabt ]]; then
      echo -e "symlink created:\n/data/data/com.termux/files/home/symlink/rcabt"
   else
      echo -e "failed to create symlink:\n/data/data/com.termux/files/home/symlink/rcabt"
   fi
else
   echo -e "symlink exists:\n/data/data/com.termux/files/home/symlink/rcabt"
fi

bn=$(basename $0)
bne=${bn%.*}
bnx=${bn##*.}
echo -e "bn=$bn\nbne=$bne\nbnx=$bnx"

logfile=~/bin/${bne}.txt
echo -e "logfile: $logfile"

for r in $(rclone listremotes); do
    echo "current remote: $r"
    abts=$(rclone about $r >/dev/null 2>&1; echo $?)
    echo "about status: $abts"
    if [[ $abts -ne '0' ]]; then
       rclone config reconnect $r
    else
       echo -e "\nabout $r:" >> logfile
       rclone about $r >> $logfile
    fi
done

echo -e "logfile content:"
cat $logfile

