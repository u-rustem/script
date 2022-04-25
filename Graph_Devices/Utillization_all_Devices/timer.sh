#!/bin/bash

h=`hostname -s`
CC_LIST=$(/opt/allot/bin/go config view network  |  grep CC | tr -d '|' | awk '{print $1}');
date=`date '+%Y-%m-%d %H:%M'| awk -F "," '{printf $1}'`


for i in $CC_LIST; do
        for ((k=0; k < 2; k++)); do
                        echo $i'_xlp_'$k',' | tr -d '\n'
        done
done
echo "hostname"','"timedate"

#echo -ne '\n'

for i in $CC_LIST; do
        for ((k=0; k < 2; k++)); do
ssh root@11.11.11.$i$k  "RxdlClient 'Infra/Thread/Call Backs/Utilization' | grep 'Timer\[ 5]' | awk '{printf \$4\",\" }'"
        done
done

echo "'$h'"','"'$date'"
