from machine import Pin
import time

# this code blinks an external LED connected to GPIO 22 once

# mpremote connect /dev/tty.usbserial-210 run lesson1/blink_led.py to run this script

# mpremote connect /dev/tty.usbserial-210 reset to stop current script

# Define the LED pin.
LED_PIN = 22

# Initialize the LED pin as an output
led = Pin(LED_PIN, Pin.OUT)

print("LED will blink once...")

# Turn the LED ON
led.value(1) # or led.on()
print("LED ON")
time.sleep(1) # Wait for 1 second

# Turn the LED OFF
led.value(0) # or led.off()
print("LED OFF")

print("Blink sequence complete.")