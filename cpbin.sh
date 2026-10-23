#!/data/data/com.termux/files/usr/bin/bash
if [[ ! -d /data/data/com.termux/files/home/symlink ]]; then
   mkdir /data/data/com.termux/files/home/symlink
   chmod -R 755 /data/data/com.termux/files/home/symlink
fi

if [[ ! -s /data/data/com.termux/files/home/symlink/cpbin ]]; then
   symstat="doesnt-exists"
   ln -sv /data/data/com.termux/files/home/bin/cpbin.sh /data/data/com.termux/files/home/symlink/cpbin
   if [[ -s /data/data/com.termux/files/home/symlink/cpbin ]]; then
      symstat="newly-created"
      echo -e "symlink created:\n/data/data/com.termux/files/home/symlink/cpbin"
   else
      symstat="failed-to-create"
      echo -e "failed to create symlink:\n/data/data/com.termux/files/home/symlink/cpbin"
   fi
else
   symstat="exists"
   #echo -e "symlink exists:\n/data/data/com.termux/files/home/symlink/cpbin"
fi

bnz=$(basename $0)
if [[ "${bnz##*.}" == "sh" ]]; then
   echo -e "source-file : $(readlink /data/data/com.termux/files/home/symlink/cpbin)"
   echo -e "symlink-file: /data/data/com.termux/files/home/symlink/cpbin"
   echo -e "symlink-stat: $symstat"
fi

if [[ -z $1 ]]; then
   usage="usage: $(basename $0) [bin-directory-path]"
   echo -e "$usage"
   exit
fi
   
if [[ ! -d $1 ]]; then
   echo -e "is-not-a-dir: $1"
   exit
else
   echo -e "import-source: $1"
   dname=$(basename "$1")
   if [[ ! "$dname" == "bin" ]]; then
      echo -e "dirpath must endswith 'bin' "
      exit
   fi
fi

cd $HOME
hbin="$HOME/$(basename $1)"
echo -e "copying $1 to $hbin"
#cp -rv "$1" "$hbin"
echo -e "executing chmod -Rv 755 $hbin"
#chmod -Rv 755 $hbin
if [[ -d $hbin ]]; then
   cd $hbin
   ls $hbin
fi
   