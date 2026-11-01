#!/data/data/com.termux/files/usr/bin/bash
if [[ ! -s /data/data/com.termux/files/home/symlink/micro ]]; then
   ln -sv /data/data/com.termux/files/home/bin/micro.sh /data/data/com.termux/files/home/symlink/micro
   if [[ -s /data/data/com.termux/files/home/symlink/micro ]]; then
      echo -e "symlink created:\n/data/data/com.termux/files/home/symlink/micro"
   else
      echo -e "failed to create symlink:\n/data/data/com.termux/files/home/symlink/micro"
   fi
else
   echo -e "symlink exists:\n/data/data/com.termux/files/home/symlink/micro"
fi
/data/data/com.termux/files/usr/bin/micro -clipboard internal $@
