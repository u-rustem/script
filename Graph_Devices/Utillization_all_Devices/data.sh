#!/bin/bash
LOG=`hostname -s`
timer=/mnt/common/sysadmin/anomal/$LOG.timer
cer=/mnt/common/sysadmin/anomal/$LOG.cer
ses=/mnt/common/sysadmin/anomal/$LOG.ses
cd /mnt/common/sysadmin/anomal/


sh /mnt/common/sysadmin/anomal/timer.sh > /mnt/common/sysadmin/anomal/$LOG.timer
sh /mnt/common/sysadmin/anomal/cer.sh > /mnt/common/sysadmin/anomal/$LOG.cer
sh /mnt/common/sysadmin/anomal/ses.sh > /mnt/common/sysadmin/anomal/$LOG.ses

scp $timer root@192.168.1.31:"/rus/load2/data"
scp $cer root@192.168.1.31:"/rus/load2/data"
scp $ses root@192.168.1.31:"/rus/load2/data"

#rm -rf /mnt/common/sysadmin/anomal/lab-tera-1.*

sh data1.sh

