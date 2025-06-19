---
layout: default
title: "ESP32-C3 Breadboard Adapter"
---

{{ page.title }}
================


    - __I2C__
    - __I2S__
    - Remote control
    - __Pulse counter__
    - __LED PWM__
    - Full-speed USB 2.0 OTG
    - USB Serial/JTAG controller
    - __MCPWM__
    - SDIO host controller
    - GDMA
    - TWAI® controller (compatible with ISO 11898-1)
    - ADC
    - Touch sensor
    - Temperature sensor
    - Timers and watchdogs

__Integrated Components:__
  - Crystal Oscillator: 40 MHz
  - Flash: Up to 16 MB Quad SPI flash
  - Antenna: on-board PCB antenna

__Operating Conditions:__
  - Operating Voltage: 3.0 ~ 3.6 V
  - Ambient Temperature: –40 ~ 65 °C

__Certifications:__
RF Certification: Various certifications available
Green Certification: RoHS/REACH compliant

__Applications:__
Ideal for AI and Artificial Intelligence of Things (AIoT) applications such as:
Wake word detection
Speech commands recognition
Face detection and recognition
Smart home devices
Smart appliances
Smart control panels
Smart speakers

## I2C Pins

The schematic excerpt provided below illustrates the wiring configuration for the __SDA__ and __SCL__ lines. Specifically, the __SDA__ line is connected to _GPIO 8_, while the __SCL__ line is connected to _GPIO 9_ on the ESP32-S3 module.

<img src="assets/ESP32-Uno-Board-Module-Pinout.png" width="50%"/>

The image of the PCB board below depicts the physical locations of the __SDA__ and __SCL__ terminals.
<img src="assets/ESP32-Uno-Board-GPIO.png" width="50%"/>

### Micropython LED Blinky Code

``` python
import esp, esp32, time, os, _thread
from machine import Pin, SoftI2C

# An infinite loop thread to blink LED
def status_led():
    # Blink pattern blink-blink-pause
    while True:
        led.value(1)
        time.sleep_ms(250)
        led.value(0)
        time.sleep_ms(250)
        led.value(1)
        time.sleep_ms(250)
        led.value(0)
        time.sleep_ms(750)
        
def connect_wifi():
    import network
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('IoT_bots', '208208208')
        while not wlan.isconnected():
            pass
    print('Network Config:', wlan.ipconfig('addr4'))

# Display information about ESP32S3 module
print("=====================================\n")
print(os.uname())
print("\n=====================================")
print("Flash size: ", esp.flash_size()/1024/1024, "Mb")
print("MCU Temperature: {:4.1f} C".format(esp32.mcu_temperature()))

connect_wifi()

# Configure LED pin and start the blinky loop thread
#led = Pin(45, Pin.OUT)
#led.value(0)
#_thread.start_new_thread(status_led, ())

```
