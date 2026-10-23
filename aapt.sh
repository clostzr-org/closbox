#!/data/data/com.termux/files/usr/bin/bash
src_path=$0
src_bn=$(basename ${src_path})
src_bne=${src_bn%.*}
src_ext=${src_bn##*.}
sym_dir="${HOME}/symlink"
sym_path="${sym_dir}/${src_bne}"
sym_bn=$(basename ${sym_path})
sym_bne=${sym_bn%.*}
sym_ext=${sym_bn##*.}

src_file=$src_path
sym_file=$sym_path

info="
src_path: ${src_path}
src_bne : ${src_bne}
src_ext : ${src_ext}
sym_path: ${sym_path}
sym_bne : ${sym_bne}
sym_ext : ${sym_ext}
"
#echo "${info}"

mksl(){
if [[ ! -s ${sym_file} ]]; then
   ln -sv ${src_file} ${sym_file}
   if [[ -s ${sym_file} ]]; then
      echo -e "symlink created:\\n${sym_file}"
   else
      echo -e "failed to create symlink:\\n${sym_file}"
   fi
else
   echo -e "symlink exists:\\n${sym_file}"
fi
}

if [[ $src_ext == 'sh' ]]; then
   mksl
fi

xfile="/data/data/com.termux/files/usr/bin/aapt"
xtest=$($xfile; echo $?)
w_aapt = $(which aapt)
if [[ -z $w_aapt ]]; then
   echo -e "aapt not found"
   apt install aapt
fi
echo "xtest=$xtest"
if [[ ! "$xtest" == "" ]]; then
   apt install aapt
fi
/data/data/com.termux/files/usr/bin/aapt "$@"
