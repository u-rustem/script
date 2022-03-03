#!/bin/bash

cd /mnt/common/sysadmin
sleep 60
VPN_IP=$(more vpnIP.txt)
OLD_IP=$(more oldIP.txt)

if [ "$OLD_IP" != "$VPN_IP" ] ; then 
sudo acstat -ixe  | grep $VPN_IP | awk '{print $7, $8, $4}' | awk '!seen[$0]++' > /mnt/common/sysadmin/IPvpn.txt
#	sudo acstat -ixe  | grep $VPN_IP | awk '{print $8}' | awk '!seen[$0]++' > /mnt/common/sysadmin/Portvpn.txt
#	sudo acstat -ixe  | grep $VPN_IP | awk '{print $7}' | awk '!seen[$0]++' > /mnt/common/sysadmin/IPvpn.txt

#	while read LINE
#		   do 
			   #sh catalogsCLI_new.sh -update -service -name melon -add_port TCP:Port_based:HOST:melon:$LINE
#		   done < Portvpn.txt


#		   while read LINE
#			      do
#				      sh catalogsCLI_new.sh -update -host -name melon -add_entry IP_ADDRESS:$LINE
#			      done < IPvpn.txt




			      #echo $VPN_IP > IP.txt
			      #echo $Port_VPN >> IP.txt
fi

