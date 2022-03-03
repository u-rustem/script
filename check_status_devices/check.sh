#!/bin/bash
LOG=`hostname -s`
LOGFILE=/mnt/common/sysadmin/anomal/$LOG.log


sh /mnt/common/sysadmin/anomal/CC_status.sh > $LOGFILE

sh=/mnt/common/sysadmin/anomal/5.sh
acstat | grep Both | awk  -F " " '{print $1,$8}' | awk '$2 > 80' > /mnt/common/sysadmin/anomal/2.txt
sed 's/\./\ /' /mnt/common/sysadmin/anomal/2.txt > /mnt/common/sysadmin/anomal/3.txt
file="/mnt/common/sysadmin/anomal/3.txt"
cat 3.txt | awk '{print $1, $2}' > /mnt/common/sysadmin/anomal/4.txt
while read lineA
    do echo $lineA > 4.txt
    lineB=`cat 4.txt | awk '{print $2}'`;
    lineC=`cat 4.txt | awk '{print $1}'`;    
echo "sudo /opt/allot/products/bin/default/default/host/default/run_on_all_units -s $lineC -c $lineB -- acstat.local -ix -m 100000 | awk '{ print \$1\" \"\$2\  \"\$5\" \"\$6}' | sort | uniq -c| sort -rn | head"  >> $sh
done < $file

sh /mnt/common/sysadmin/anomal/5.sh >> $LOGFILE
echo "#!/bin/bash" > $sh
run_on_all_dpics "RxdlClient 1/3/1/2 |  awk  '\$8==256 && \$10==100.0'" >> $LOGFILE


date >> $LOGFILE
echo "**********************************************END******************************************************"  >> $LOGFILE

cat $LOGFILE >> /mnt/common/sysadmin/anomal/"$LOG"-all.log

if [ `date +%H` = 21 ]; then
scp $LOGFILE admin@10.0.208.4:"/opt/admin/nur/`date +%d%m%Y`"
fi
