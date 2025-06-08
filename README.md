# MicroPython ESP32 Projects

This repository has code examples for ESP32 projects.

Each example comes with a Wokwi diagram. Wokwi is a free online tool that lets you run and see your code work right in your web browser, so you don't even need your physical ESP32 board to start!

## lesson 1
### [`lesson1/blue_led.py`](https://github.com/fullstackdevell/esp32/blob/main/lesson1/blue_led.py)

This script shows you how to turn the onboard blue LED (GPIO2) on for one second and then turn it off. Since we're using the LED built into your ESP32, no external wiring diagram is needed for this lesson!

### [`lesson1/blink_led.py`](https://github.com/fullstackdevell/esp32/blob/main/lesson1/blink_led.py)

This script shows you how to blink an external LED connected to GPIO22 once. A Wokwi diagram is provided for this lesson to guide you through the wiring of your LED and resistor to GPIO22 and GND.
![blink_led](/images/blink_led.png)

### [`lesson1/while_true_blink.py`]
(https://github.com/fullstackdevell/esp32/blob/main/lesson1/while_true_blink.py)

This script shows you how to make an external LED connected to GPIO22 blink continuously. This lesson uses the same Wokwi duagram as blink_led.py.

