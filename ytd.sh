#!/data/data/com.termux/files/usr/bin/bash
dfx=$(df | grep -E "/storage/*-*" | awk '{print $6}')

for d in ${dfx}; do
    if [[ ${d} == *-* ]]; then
       xsd=${d}
    fi
done

cfg_file="${0%.*}.txt"
echo "external_sd: ${xsd}"
echo "config_file: ${cfg_file}"

cat > "${cfg_file}" <<EOF
-c -i -o ${xsd}/Music/%(playlist_title)s/%(title)s.%(ext)s
EOF

echo "config_file_content:"
cat ${cfg_file}

checkpy=$(python -h > /dev/null; echo $?)
#echo "checkpy: ${checkpy}"
if [[ ! "$checkpy" == 0 ]]; then
   apt update; apt upgrade; apt install python;
fi

checkyt=$(yt-dlp -h > /dev/null; echo $?)
#echo "checkpy: ${checkpy}"
if [[ ! "$checkyt" == 0 ]]; then
   apt update; apt upgrade; pip install yt-dlp
fi

yt-dlp \
--config-location "${cfg_file}" \
"$@"
