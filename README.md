# ESP32-C3_Breadboard-Adapter

_ESP32-C3 Module, power supply, and breadboard adapter combo._

<img alt="ESP32-Node PCB" src="https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/assets/ESP32-C3-BreadBoardAdapter.jpg" width="75%"/>

[Manual](https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/guide/build/latex/esp32-c3breadboardadapter.pdf)

### Features:
- compact size requires very little space on a breadboard;
- connects to the power rails on a breadboard;
- can be powered by USB-C port or external power supply;
- 3.3V and 5V power supplies;
- GPIOs arranged into 4 groups for easier identification;
- on-board ESP32-C3 Module with USB-C port allows to flash a firmware as you work with breadboard;
- debugging points;
- power pads makes it easy to connect alligators supplying voltage to the board;
- on-board system LEDs: power, and module reset mode;
- on-board push switch for Reset and Flash modes;
- on-board push switch and LED for your needs;

### ESP32-C3 Module:
- single-core
- 32-bit RISC-V MCU @ 160 MHz
- 400 KB of internal RAM
- RSA-3072-based secure boot and the AES-128/256-XTS flash encryption
- low power-mode support
- Rich connectivity for IoT applications: Wi-Fi and Bluetooth 5 (LE) with long-range support
- Bluetooth LE SIG Mesh and Wi-FI Mesh support
- 22 GPIOs

## Learning Activities
_Learn and develop new skills as you build and work with this microcontroller combo board._

## Schematic

[Schematic](https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/schematic/ESP32-C3-BreadBoardAdapter_Schematic.pdf)

### Reserved GPIOs & Pins

_The table below lists strapping and reserved pins._

ESP32-C3 has three strapping pins: GPIO2, GPIO8 and GPIO9. By default, GPIO9 is connected to the internal pull-up resistor. If GPIO9 is not connected or connected to an external high-impedance circuit, the latched bit value will be '1'.

During the chip's system reset, the latches of strapping pins samle re voltage level as strapping bits of '0' or '1', and hold these bits until the chip is powered down. After reset, the strapping pins work as normal-function pins.

| GPIO | Physical Pin | Adapter Pin | Description |
| --- | --- | --- | --- |
| EN | 1 | 2 | ESP32-C3 Enable pin |
| IO9 | 8 | 8 | Strapping pin |
| IO8 | 5 | 7 | Strapping pin |
| IO18 | 11 | 13 | USB D- |
| IO19 | 9 | 14 | USB D+ |
| IO10 | 7 | 10 | On-board LED |
| IO3 | 13 | 15 | On-board push switch |

### GPIOs & Pins

_The table below reconciles wiring of ESP32 module GPIOs with board pins._

| GPIO | Physical Pin | Type | Description |
| --- | --- | --- | --- |
| EN | 1 | I | Enable/Disable the chip (active HIGH). |
| IO4 | 2 | I/O/T | GPIO4, __ADC1_CH4__, FSPIHD, MTMS  |
| IO5 | 3 | I/O/T | GPIO5, __ADC2_CH0__, FSPIWP, MTDI |
| IO6 | 4 | I/O/T | GPIO6, FSPICLK, MTCK |
| IO8 | 5 | I/O/T | GPIO8 |
| IO7 | 6 | I/O/T | GPIO7, FSPDI, MTDO |
| IO10 | 7 | I/O/T | GPIO10, FSPICS0 |
| IO9 | 8 | I/O/T | GPIO9 |
| USB_D+ | 9 | I/O/T | GOIO19, __USB D+__ |
| RxD | 10 |  I/O/T | GPIO20, __U0RxD__ |
| USB_D- | 11 |  I/O/T | GPIO18, __USB D-__ |
| TxD | 12 |  I/O/T | GPIO21, __U0TxD__ |
| IO3 | 13 | I/O/T | GPIO3, __ADC1_CH3__ |
| IO2 | 14 |  I/O/T | GPIO2, __ADC1_CH2__, FSPIQ |
| IO1 | 15 |  I/O/T | GPIO1, __ADC1_CH1__, XTAL_32K_N |
| IO0 | 16 |  I/O/T | GPIO0, __ADC1_CH0__, XTAL_32K_P |

### ESP32-C3 Current Consumption Characteristics

|  Mode  |  Peak (mA)  |
|  ---  |  ---:  |
| RF working |  345mA  |
| Modem sleep[ the CPU is powered on @ 160 MHz |  20mA  |
| Light sleep |  130 uA  |
| Deep sleep; RTC timer + RTC memory |  5 uA  |
| Power off |  1 uA  |

## Components List (Bill of Materials)

| Reference | Value | Description | Reference |
| --- | --- | --- | --- |
| C1, C2 | 1uF | Capacitor | SMD |
| C4 | 10uF | Capacitor | SMD |
| C5 | 0.1uF | Capacitotr | SMD |
| R1, R2, R3, R7 | 5k1 | Resistor | SMD |
| R4, R5 | 10k | Resistor | SMD |
| R6, R8 | 2k2 | Resistor | SMD |
| D1, D2 | D | Diode | SMD |
| U1 | ESP32-C3-WROOM | ESP32 C3 Module | |
| U2 | AMS1117-3V3 | Voltage regulator 3.3V | [Datasheet: AMS1117](https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/assets/Voltage-Regulator_AMS1117.PDF) |
| U3 | L58M05 | Voltage regulator 5.0V | |
| SW1, SW2, SW3 | SW | Push switch | SW_PUSH_6x3.5mm |
| LED1 | RGB LED | Red, Green, Blue LED | SMD B1552USUG20D |
| LED2 | RED LED | Power LED | SMD B1552 |
| J2 | USB-C | USB 2.0 Type C power and data receptacle | [Datasheet: GCT USB4085 GF A](https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/assets/USB-C-usb4085.pdf) <br/> Footprint | 

### Blinky LED & Button Demo Code

Short code written in MicroPython that blinks on-board LED every 1.5 seconds, and interrupts the cycle when on-board tactile push-button is pressed. 

```python
# Miniature code that uses thread to blink on-board LED
# and button interrupt to reset LED thread.

from machine import Pin
from machine import Timer
from utime import sleep_ms

# GPIOs for LED and Button, as stated on the schematic
ONBOARD_LED = 10	# GPIO10, PIN 7
ONBOARD_BTN = 3		# GPIO3, 13

onboard_led = Pin(ONBOARD_LED, Pin.OUT)
onboard_button = Pin(ONBOARD_BTN, Pin.IN, Pin.PULL_UP)

# Interrupt function to toggle on/off the on-board LED
def led_interrupt(t):
    onboard_led.value(not onboard_led.value())
    
# Interrupt function to turn LED ON when on-board button is pressed
def button_interrupt(pin):
    print("Button was pressed")
    onboard_led.value(1)

def main():
    # Initialize timer
    onboard_led_timer = Timer(0)
    # Assign timer to onboard LED
    onboard_led_timer.init(mode=Timer.PERIODIC,period=1500,callback=led_interrupt)
    # Assign interrupt to onboard button
    onboard_button.irq(trigger=Pin.IRQ_FALLING, handler=button_interrupt)

# No While Loop
if __name__ == '__main__':
    main()
