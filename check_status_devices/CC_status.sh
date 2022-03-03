#!/bin/bash
export PATH="$PATH:/opt/allot/scripts:/opt/allot/bin"

awk 'BEGIN { format = "|%-15s|%5s|%5s|%6s|%14s|%14s|%20s|%20s|%20s|\n"; \
        print  "+---------------+-----+-----+------+--------------+--------------+--------------------+--------------------+--------------------+" ;\
        printf format, "Hostame", "Slot", " XLP ", "Timer ", "Cer_drops", "Ses_drops", "Uptime", "D_Flow > 80%", "S_Flow > 80%" ;\
        print  "+---------------+-----+-----+------+--------------+--------------+--------------------+--------------------+--------------------+" }';

CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}');

for i in $CC_LIST; do 
	for ((k=0; k < 2; k++)); do
ssh root@11.11.11.$i$k	"RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep 'Timer\[ 5]' | awk '{printf \$4\";\" }';\
			RxdlClient 'Software/DataPlane/DataFlowManager/Call Backs/Dropped Frame Counters' | grep cer_o | awk '{printf \$3\";\"}';\
			RxdlClient 'Software/DataPlane/DataFlowManager/Call Backs/Dropped Frame Counters' | grep frame_dropped_session_upload_profile_B_max_on | awk '{printf \$3\";\"}';\
			uptime | awk -F \",\" '{printf \$1\";\"}' ;\
			RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep D_Flow | sed s/' '//g |  awk -F\"|\" ' \$2 > 80 { printf \$2\",\"}' ; printf ';' ;\
			RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep S_Flow | sed s/' '//g |  awk -F\"|\" ' \$2 > 80 { printf \$2\",\"}' ; printf ';' "|
	awk -F ";" -v hn=`hostname -s` -v i=$i -v k=$k 'BEGIN { format = "|%-15s|%5s|%5s|%6s|%14s|%14s|%20s|%20s|%20s|\n"; }\
                                        { printf format , hn, i, k, $1, $2, $3, $4, $5, $6}'
        echo "+---------------+-----+-----+------+--------------+--------------+--------------------+--------------------+--------------------+" ;
	done
done
	awk 'BEGIN { format = "|%-15s|%15s|\n"; \
        print  "+---------------+---------------+" ;\
        printf format, "Acmon In","Acmon Out";\
        print  "+---------------+---------------+" }';

	acmon -c 1 | grep Total | awk '{printf $5,$7}'|
#	acmon -c 1 | grep Total | awk '{printf $7}'|

#	awk -F ";" -v hn=`hostname -s` 'BEGIN { format = "|%-15s|%15s|\n"; }\
	awk 'BEGIN { format = "|%-15s|%15s|\n"; }\
        { printf format ,  $0, $1 }';
        echo "+---------------+---------------+" ;
