#!/bin/bash

cd /opt/allot/conf
export PATH="$PATH:/opt/allot/scripts:/opt/allot/bin"
CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}')

k=0;

for i in $CC_LIST; do
count=`ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep HDR | wc -l"`

if (( $count == 2 )); then
echo root@11.11.11.$i$k ;
ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep dataExp_HDR | head -n2 | tail -n1 | awk '{print \$1}'" > /mnt/common/sysadmin/test.txt
num=`cat /mnt/common/sysadmin/test.txt`
ssh root@11.11.11.$i$k "sed -i $num' s/HDR/VDR/g' /opt/allot/conf/ccKeeper.ini";
ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep HDR";
ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep VDR";
elif (( $count > 2 )); then
echo root@11.11.11.$i$k ;
ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep HDR";
else (( $count < 2 ));
echo root@11.11.11.$i$k ;
ssh root@11.11.11.$i$k "cat -n /opt/allot/conf/ccKeeper.ini | grep HDR";
fi
done
rm -rf /mnt/common/sysadmin/test.txt
