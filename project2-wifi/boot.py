import os
import sys
import esp
# import get_libs

# esp.osdebug(esp.LOG_DEBUG)

import gc
gc.collect()

import network

AP = False

if AP:
    ssid = 'my-esp' # Change this if you are working in a classroom
    password = ''
    station = network.WLAN(network.AP_IF)
    station.active(True)
    station.config(essid=ssid, password=password)
    print('connecting in AP mode...')
    while not station.active():
        pass
    print('Connection successful')
    print(station.ifconfig())

else:   

    MY_SSID = '<insert-your-ssid-here>' 
    MY_PW = '<your-password>'

    station = network.WLAN(network.STA_IF)
    station.active(True)

    if not station.isconnected():
        station.connect(MY_SSID, MY_PW)

    print('connecting to :',MY_SSID)
    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())

import webrepl
webrepl.start()
