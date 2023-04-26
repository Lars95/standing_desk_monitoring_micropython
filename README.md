# Standing Desk Monitoring Project

This project is designed to monitor the height of a standing desk using an ESP32 microcontroller and an HC-SR04 Ultrasonic Distance Sensor. 

The data collected is sent to an HTTP endpoint (e.g. a Node-RED flow) over WiFi, which can then be used to track standing/sitting behavior and encourage healthier habits.

## Requirements
1. ESP32 microcontroller with MicroPython
2. HC-SR04 Ultrasonic Distance Sensor
3. WiFi network
4. HTTP endpoint service to receive and further process data (e.g. Node-RED)

## Installation
1. Connect the HC-SR04 Ultrasonic Distance Sensor to the ESP32 microcontroller. Connect the trigger pin to any available digital output pin (e.g. P22) and the echo pin to any available digital input pin (e.g. P23). Also connect VCC to 5V pin and Gnd to ground pin
2. Upload the files *'boot.py'*, *'main.py'*, and *'hcsr04.py'* to the ESP32 board.
3. Modify boot.py with your WiFi network name and password.
4. Modify main.py with the HTTP endpoint address. Check the ip address of your home assistant device and the port Node-Red addon is accessible (Probably 1880)
5. Configure the pins used for the HC-SR04 sensor if necessary.

## Usage
- Power on the ESP32 microcontroller.
- The microcontroller will connect to the configured WiFi network and start monitoring the height of the desk.
- The height data will be checked every 60 seconds.
- If the height changes by more than 3cm, the mode (sitting/standing) will be updated and sent to the HTTP endpoint server.
- The LED on the ESP32 board will light up if the height is less than 80cm.

## Usage with Home Assistant
To use this project with Home Assistant, please follow the instructions below:

1. Install the Node-RED add-on in Home Assistant.
2. Import the *'standing-desk-monitoring-node-red-flow.json'* file into Node-RED.
3. Modify the HTTP endpoint address in the standing-desk-monitoring node with the address used in the ESP32 board.
4. Deploy the Node-RED flow.
5. Create an automation in Home Assistant to receive a notification when the user has been sitting for more than 2 hours. See the yaml file *'ha_automation.yaml'* for inspiration.

## License
This project is released under the MIT license. Please see the LICENSE file for more information.