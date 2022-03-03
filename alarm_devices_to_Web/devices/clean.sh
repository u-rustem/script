#!/bin/bash


h=`hostname -s`

file="/root/$h.txt"

while read lineA
    do 

if [[ `echo $lineA | awk '{print $2}'` != "Slot" ]]; then
	if [[ `echo $lineB | awk '{print $2}'` == "Slot" ]]; then
		echo $lineB
		echo $lineA
	else 
		echo $lineA
	fi

fi
lineB=$lineA



done < $file
