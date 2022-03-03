#!/bin/bash
h=`hostname -s`
LOGFILE=/root/$h.txt
ALLLOG=/root/$h-all.txt

sh /root/dflow.sh > $LOGFILE
sh /root/sflow.sh >> $LOGFILE
sh /root/clean.sh > $ALLLOG


if [ -s $ALLLOG ]
then
        scp $ALLLOG disp@10.0.208.3:"/home/disp/nx_rus" 
fi
