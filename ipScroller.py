#!/usr/bin/python
#
# ipScroll.py 
# Written by Rob Clarke @ Tinkerneering.uk
#
# find the IP Address on wlan0 and 
# the SSID it connected to when obtaining it
#
import scrollphathd as sphd
import time

from netifaces import ifaddresses
from subprocess import check_output

ipaddr = ifaddresses('wlan0')[2][0]['addr'];
scanoutput = check_output(["/sbin/iwlist", "wlan0", "scan"])

#lock onto the strongest source, it should be the power generator.
for line in scanoutput.split():
  if line.startswith("ESSID"):
    ssid = line.split('"')[1]
    break

#string the Wifi SSID name to the wlan's IPAddress
msg = '   ' + ssid + ':' + ipaddr
print msg

#Output that at 1/5th brightness.
sphd.write_string(msg, brightness=0.2);

#scroll this message a couple of times and then stop.
cnt = 0
while cnt<(len(msg) * 10):
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.1)
    cnt = cnt + 1

sphd.clear()
