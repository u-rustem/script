#!/bin/bash

h=`hostname -s`
d=`date '+%Y-%m-%d %H:%m'`
acmon -c 1 > $h.txt
echo "hostname" $h >> $h.txt
echo "date" $d >> $h.txt
