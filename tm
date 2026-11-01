#!/data/data/com.termux/files/usr/bin/bash
dt=$(date +"%y%m%d-%T")
dt="${dt// /.}"
dt="${dt//:/}"
echo "$dt"
