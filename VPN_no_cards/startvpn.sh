#!/bin/bash

cd /home/unixsun/vpncard/platform-tools
./adb shell curl -s https://2ip.ru > /home/unixsun/vpncard/oldIP.txt
./adb shell monkey -p com.nocardteam.nocardvpn -c android.intent.category.LAUNCHER 1
sleep 15
./adb shell input tap 532 1289
sleep 20
./adb shell curl -s https://2ip.ru > /home/unixsun/vpncard/vpnIP.txt
./adb shell am start -a android.intent.action.VIEW "https://www.youtube.com/watch?v=_oQLKN2aIb4&t=1027s"
sleep 120
