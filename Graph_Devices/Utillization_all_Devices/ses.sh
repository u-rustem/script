#!/bin/bash

h=`hostname -s`
CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}');
date=`date '+%Y-%m-%d %H:%M'| awk -F "," '{printf $1}'`


for i in $CC_LIST; do
        for ((k=0; k < 2; k++)); do
                        echo $i'_xlp_'$k',' | tr -d '\n'
        done
done

#echo -ne '\n'
echo "hostname"','"timedate"

for i in $CC_LIST; do
        for ((k=0; k < 2; k++)); do
ssh root@11.11.11.$i$k  "RxdlClient 'Software/DataPlane/DataFlowManager/Call Backs/Dropped Frame Counters' | grep frame_dropped_session_upload_profile_B_max_on | awk '{printf \$3\",\"}'"
        done
done
echo "'$h'"','"'$date'"

