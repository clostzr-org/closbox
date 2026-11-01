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
src_bne: ${src_bne}
src_ext: ${src_ext}
sym_path: ${sym_path}
sym_bne: ${sym_bne}
sym_ext: ${sym_ext}
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

apti(){
  apt update
  apt install micro
  micro -plugin install runit
  micro -plugin update runit
  apt install termux-api
}

tcget='/data/data/com.termux/files/usr/bin/termux-clipboard-get'

if command -v "$tcget" >/dev/null 2>&1; then
  # echo "termux-clipboard-get is installed."
  # Execute your command using $tcget
  # Example: 
  # clipboard_content=$( "$tcget" )
  # echo "Clipboard contents: $clipboard_content"
  echo -e "$($tcget) "
else
  echo "termux-clipboard-get is not installed."
  # You could suggest the user install it here.
  apti
fi


