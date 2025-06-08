from machine import Pin
from time import sleep

# This script turns the onboard blue LED on

# Initialize GPIO2 as an output pin for the LED.
# GPIO2 is connected to the blue onboard LED on ESP32
led = Pin(2, Pin.OUT)

# Turn the LED ON
led.on()
sleep(1) # Wait for 1 second

# Turn the LED OFF
led.off()
sleep(1) # Wait for 1 second before the script finishes