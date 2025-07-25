---
layout: default
title: "ESP32-C3 Breadboard Adapter"
---

{{ page.title }}
================

<i>Discover new opportunities with the ESP32-C3 UNO Development Board</i>
<p>Unlock a world of innovative possibilities with the ESP32-C3 Breadboard Development Board. This versatile platform empowers developers to create cutting-edge applications, leveraging its advanced features and robust performance. Whether you're working on IoT projects, embedded systems, or automation tasks, the ESP32-C3 Development Board offers the flexibility, power and quick implementation needed to bring your ideas to life.</p>
<p>Explore its capabilities and push the boundaries of your creativity and technical expertise.</p>

<img src="assets/ESP32-C3-BreadBoardAdapter-001.jpg" width="100%"/>

<h2>Key Features:</h2>
<ul>
  <li>compact size; requires a very little space on a breadboard</li>
  <li>flash a firmware without external adapters as you work with your project</li>
  <li>supplies 3.3V or 5V to the breadboard power rails</li>
  <li>can be powered either by USB-C or external powersupply</li>
  <li>GPIOs are arranged into 4 groups for easier indentification</li>
  <li>on-board power and user-controlled LEDs</li>
  <li>on-board RESET and BOOT push-button switches</li>
</ul>

## Schematic

[Schematic](schematic.md)

## Specifications Details

[Specs](specs.md)

[Troubleshooting Steps](troubleshooting.md)

## Compatibility with MicroPython

Integrating the ESP32-C3 Development Board with MicroPython offers several compelling benefits:

1. __Ease of Use:__
MicroPython simplifies the development process by allowing developers to write code in Python, a high-level, easy-to-read programming language. This reduces the learning curve for beginners and accelerates development for experienced programmers.

2. __Rapid Prototyping:__
With MicroPython, developers can quickly prototype and test their ideas. The interactive REPL (Read-Eval-Print Loop) enables immediate feedback and debugging, making it easier to iterate and refine projects.

3. __Extensive Libraries:__
MicroPython comes with a rich set of libraries that support various functionalities, including networking, sensor interfacing, and data processing. This extensive library support allows developers to leverage pre-built modules and focus on the unique aspects of their projects.

4. __Cross-Platform Compatibility:__
MicroPython code can be easily ported across different hardware platforms that support MicroPython. This cross-platform compatibility ensures that projects developed on the ESP32-S3 UNO can be adapted to other MicroPython-compatible boards with minimal changes.

5. __Community Support:__
The MicroPython community is active and growing, providing a wealth of resources, tutorials, and forums for troubleshooting and collaboration. This community support can be invaluable for both novice and experienced developers.

6. __Efficient Resource Management:__
MicroPython is designed to run efficiently on microcontrollers, making it well-suited for resource-constrained environments. It allows developers to manage memory and processing power effectively, ensuring optimal performance of their applications.

7. __Enhanced Connectivity:__
The ESP32-C3 Development Board offers robust connectivity options, including Wi-Fi and Bluetooth. MicroPython's networking libraries make it straightforward to implement IoT applications, enabling seamless communication between devices.

8. __Versatility:__
Combining the ESP32-C3 Development Board with MicroPython opens up a wide range of applications, from simple sensor monitoring to complex automation systems. The versatility of this fusion allows developers to explore diverse project ideas and innovate freely.

9. __Educational Value:__
MicroPython's simplicity and the ESP32-C3's capabilities make this combination an excellent educational tool. It provides a practical platform for learning programming, electronics, and IoT concepts, fostering a deeper understanding of technology.

10. __Cost-Effective Development:__
Both the ESP32-C3 Development Board and MicroPython are cost-effective solutions, making them accessible to hobbyists, educators, and professionals alike. This affordability encourages experimentation and innovation without significant financial investment.


## Features and Specifications of the ESP32-C3 WROOM Module
__Core Components:__
  - Microprocessor: RISC-V® single-core 32-bit microprocessor, operating up to 160 MHz.
  - Memory:
    - 384 KB ROM
    - 400 KB SRAM
    - 8 KB SRAM in RTC

__Connectivity:__
  - Wi-Fi:
    - 802.11b/g/n, up to 150 Mbps (802.11n), frequency range: 2412 ~ 2484 MHz
    - Four virtual Wi-Fi interfaces
    - simultaneous support SoftAP mode, Station + SoftAP mode and promiscuous mode
  - Bluetooth:
    - Bluetooth 5, Bluetooth mesh, 125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps
    - Features: Advertising extensions, multiple advertisement sets, channel selection algorithm #2
  - Co-existence mechanism: Internal co-existence mechanism between Wi-Fi and Bluetooth to share the same antenna

__Security:__
  - RSA-3072-based secure boot and the AES-128/256-XTS flash encryption
__Peripherals:__
  - GPIOs: Up to 22 GPIOs, including 4 strapping GPIOs
  - Interfaces:
    - SPI
    - Two __UART__
    - __I2C__
    - __I2S__
    - __LED PWM__, up to 6 channels
    - Full-speed USB 2.0 OTG
    - USB Serial/JTAG controller
    - TWAI® controller (compatible with ISO 11898-1)
    - 12-bit __ADC__, up to 6 channels
    - Touch sensor
    - Temperature sensor
    - Two 54-bit general purpose timers
    - Three digital and one analog watchdog timers

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

## Reserver GPIOs and Pins

|  GPIO  |  ESP32-C3 Module Pin  |  Breadboard Pin  |  Designation  |
|  ---  |  ---  |  ---  |  ---  |
| EN  | 1  | 2  | Enable pin  |
| IO9  | 8  | 8  | Strapping pin  |
| IO8  | 5  | 7  | Strapping pin |
| IO18  | 11  | 13  | USB D-  |
| IO19  | 9  | 14  | USB D+  |
| IO10  | 7 | 10  | On-board user LED  |
| IO3  | 13  | 15  | On-board user tactile switch  |

## I2C Pins

The schematic excerpt provided below illustrates the wiring configuration for the __SDA__ and __SCL__ lines. Specifically, the __SDA__ line is connected to _GPIO 8_, while the __SCL__ line is connected to _GPIO 9_ on the ESP32-C3 Wroom module. 

<img src="assets/ESP32-C3-Breadboard-USB-C.png" width="90%"/>

The image of the PCB board below depicts the physical locations of the __SDA__ and __SCL__ terminals.

<img src="assets/ESP32-C3-BreadBoardAdapterPinout.png" width="50%"/>

``` C
i2c_config_t conf = {
    .mode = I2C_MODE_MASTER,
    .sda_io_num = 8,
    .scl_io_num = 9,
    .sda_pullup_en = GPIO_PULLUP_ENABLE,
    .scl_pullup_en = GPIO_PULLUP_ENABLE,
    .master.clk_speed = 100000,
};
i2c_param_config(I2C_NUM_0, &conf);
i2c_driver_install(I2C_NUM_0, conf.mode, 0, 0, 0);
```

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
