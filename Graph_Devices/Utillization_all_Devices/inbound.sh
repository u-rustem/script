#!/bin/bash


h=`hostname -s`
date=`date '+%Y-%m-%d %H:%M'| awk -F "," '{printf $1}'`

in=`sudo /opt/allot/bin/acmon -c 1 | grep -e SB -e LAG -e Total  | awk '{print $1","}' | tr -d '\n'` 
echo $in"hostname"','"timedate"
in1=`sudo /opt/allot/bin/acmon -c 1 | grep -e SB -e LAG -e Total  | awk '{print $5","}' | tr -d '\n'`
echo $in1"'$h'"','"'$date'"
