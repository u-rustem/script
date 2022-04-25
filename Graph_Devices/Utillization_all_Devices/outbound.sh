#!/bin/bash


h=`hostname -s`
date=`date '+%Y-%m-%d %H:%M'| awk -F "," '{printf $1}'`

out=`sudo /opt/allot/bin/acmon -c 1 | grep -e SB -e LAG -e Total  | awk '{print $1","}' | tr -d '\n'` 
echo $out"hostname"','"timedate"
out1=`sudo /opt/allot/bin/acmon -c 1 | grep -e SB -e LAG -e Total  | awk '{print $7","}' | tr -d '\n'`
echo $out1"'$h'"','"'$date'"
