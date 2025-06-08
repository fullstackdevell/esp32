from machine import Pin
from time import sleep

# this code blinks the blue on board LED

# mpremote connect /dev/tty.usbserial-210 run pin2_led.py to run this script

# mpremote connect /dev/tty.usbserial-210 reset to stop current script

led = Pin(2, Pin.OUT)

led.on()
sleep(1)
led.off()
sleep(1)