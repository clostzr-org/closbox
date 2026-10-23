#!/data/data/com.termux/files/usr/bin/bash
echo -e "= Bluetooth Fix"
echo -e "= Command:"
echo -e "
chcon u:object_r:system_data_file:s0 
/data/data 
/data/misc/profiles/cur/0 
/data/user/0 
/data/user_de/0
"
su -lmM -c "
chcon u:object_r:system_data_file:s0 /data/data /data/misc/profiles/cur/0 /data/user/0 /data/user_de/0
"
echo -e "= Bluetooth Fix done"
