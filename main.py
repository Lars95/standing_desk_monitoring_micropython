import machine
import hcsr04
import time
import urequests as requests
import ujson

# adapt to your used pins
us = hcsr04.HCSR04(trigger_pin = 22, echo_pin = 23, echo_timeout_us=1000000)
led = machine.Pin(2, machine.Pin.OUT)
old_height = 0
mode = "sitting"
while True: 
    height = round(us.distance_cm(),2) + 11.2
    print(f'Distance: {height} cm')
    if height < 80:
        led.on()
    else:
        led.off()
    if not old_height-3 <= height <= old_height+3:    
        if height >= 100:
            mode = "standing"
        else:
            mode = "sitting"
        print(f'Distance: {height} cm - mode: {mode}')
        post_data = ujson.dumps({'height': height, 'mode': mode})
        res = requests.post('http://yourEndPoint', headers = {'content-type': 'application/json'}, data = post_data).json()
        old_height = height
    time.sleep_ms(60000)

