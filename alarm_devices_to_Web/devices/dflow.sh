#!/bin/bash
export PATH="$PATH:/opt/allot/scripts:/opt/allot/bin"
h=`hostname -s`

CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}');

for i in $CC_LIST; do 
	for ((k=0; k < 2; k++)); do
echo "$h, Slot $i, XLP $k, D_Flow"; ssh root@11.11.11.$i$k "RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep D_Flow | sed s/'|'/,/g | sed s/' '//g | sed s/','/' '/g |  awk  -F ' ' '{print $2}' " | awk  -F ' ' '{print $2}' |  awk '$1 > 80' ; 
	done
done
