# This file is executed on every boot (including wake-boot from deepsleep)

import network, utime


wifi = network.WLAN(network.STA_IF)
wifi.active(False)
wifi.active(True)
try:
    wifi.connect('wifi name', 'wifi password')
    print('Searching Wifi')
    for i in range(10):
        utime.sleep(1)
        if wifi.isconnected():
            break
    if wifi.isconnected():
        print('Connected')
        print(f'Network config: {wifi.ifconfig()}')
    else:
        print('Wifi error')
    
except Exception as e: print(e)
