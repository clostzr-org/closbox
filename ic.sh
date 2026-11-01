#!/data/data/com.termux/files/usr/bin/bash
export pgc=$(ping -c 1 google.com && { echo "#connected"; })
export epg=$(echo $pgc | awk -F'#' '{print $2}')
echo $epg
