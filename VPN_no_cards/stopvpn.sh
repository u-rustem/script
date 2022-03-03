#!/bin/bash

cd /home/unixsun/vpncard
file="/home/unixsun/vpncard/sgve1/mnt/common/sysadmin/IPvpn.txt"
cd /home/unixsun/vpncard/WSCli

while read lineA
  do echo $lineA > vpn.txt
	  lineB=`cat vpn.txt | awk '{print $1}'`;
	  lineC=`cat vpn.txt | awk '{print $2}'`;
	  lineD=`cat vpn.txt | awk '{print $3}'`;
sh catalogsCLI.sh -update -service -name nocards -add_port $lineD:Port_based:HOST:nocards:$lineC
sh catalogsCLI.sh -update -host -name nocardsvpn -add_entry IP_ADDRESS:$lineB
echo $lineB, $lineC, $lineD
done < $file



cd /home/unixsun/vpncard/platform-tools
./adb shell am force-stop com.nocardteam.nocardvpn
./adb shell am force-stop com.google.android.youtube
