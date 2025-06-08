from machine import Pin
import time

# This code blinks an external LED connected to GPIO 22 continuously

# mpremote connect /dev/tty.usbserial-210 run while_true_blink.py to run this script

# mpremote connect /dev/tty.usbserial-210 reset to stop current script

LED_PIN = 22
led = Pin(LED_PIN, Pin.OUT)

print(f"Starting LED blink on GPIO {LED_PIN}...")

try:
    while True:
        led.value(1) # Turn the LED ON
        print("LED ON")
        time.sleep(0.5) # Wait for 0.5 seconds

        led.value(0) # Turn the LED OFF
        print("LED OFF")
        time.sleep(0.5) # Wait for 0.5 seconds

except KeyboardInterrupt:
    # This block runs if you press Ctrl+C in the MicroPython REPL
    print("Stopping LED blink. LED should turn off.")
    led.value(0) # Ensure LED is off when stopping