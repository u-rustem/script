#!/bin/bash
 
CLI="/home/disp/nx_rus/WSCLi"
cd /home/disp/nx_rus
cat *.txt > /home/disp/nx_rus/all.log
pushd $CLI > /dev/null

file="/home/disp/nx_rus/all.log"

while read lineA
    do
if [[ `echo $lineA | awk '{print $2}'` == "Slot" ]]; then

./ConfigurationCLI.sh -setGenericEvent "Device critical $lineA high 80%" -severity critical  > /dev/nulla

fi

done < $file

cd /home/disp/nx_rus
rm -rf *.txt
