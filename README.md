# MicroPython Lesson 1: Basic Single LED Blink on ESP32

This lesson shows the most fundamental way to control an LED using MicroPython on an ESP32 development board: turning it on, waiting, and turning it off a single time. We'll use the **onboard blue LED**, which is typically connected to **GPIO2**.

---

## 1. Hardware Setup

* **ESP32 Development Board:** An ESP32 DevKitC (or similar board with an ESP32-WROOM-32 module).
* **USB Cable:** A USB-C cable to connect your ESP32 to your computer.

No external wiring is needed for this lesson, as we're using the LED built right into your ESP32 board.

---

## 2. The Code (`lesson1/blink_once.py`)

The `blink_once.py` script is straightforward. It sets up GPIO2 as an output, turns the LED on for 1 second, then turns it off for 1 second. After this, the script completes execution.

```python
# from machine import Pin
# from time import sleep

# # This script turns the onboard blue LED on, waits, then turns it off.
# # It runs once and then finishes.

# # Initialize GPIO2 as an output pin for the LED.
# # GPIO2 is commonly connected to the blue onboard LED on ESP32 DevKitC boards.
# led = Pin(2, Pin.OUT)

# # Turn the LED ON
# led.on()
# sleep(1) # Wait for 1 second

# # Turn the LED OFF
# led.off()
# sleep(1) # Wait for 1 second before the script finishes