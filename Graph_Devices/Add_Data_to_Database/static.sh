#!/bin/bash
export PATH="$PATH:/opt/allot/scripts:/opt/allot/bin"

echo "Timer","Cer_drops","Ses_drops","Date","Hostame","Slot","XLP"

h=`hostname -s`
CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}');

for i in $CC_LIST; do
        for ((k=0; k < 2; k++)); do
ssh root@11.11.11.$i$k  "RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep 'Timer\[ 5]' | awk '{printf \$4\",\" }';\
			RxdlClient 'Software/DataPlane/DataFlowManager/Call Backs/Dropped Frame Counters' | grep cer_o | awk '{printf \$3\",\"}';\
			RxdlClient 'Software/DataPlane/DataFlowManager/Call Backs/Dropped Frame Counters' | grep frame_dropped_session_upload_profile_B_max_on | awk '{printf \$3\",\"}';\
			date '+%Y-%m-%d %H:%m'| awk -F \",\" '{printf \$1\",\"}';\
			echo $h,$i,$k
#			echo  -ne '\n'" 
        done
done
