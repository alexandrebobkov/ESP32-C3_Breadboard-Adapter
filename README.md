# ESP32-C3_Breadboard-Adapter

_ESP32-C3, power supply and breadboard adapter combo._

<img alt="ESP32-Node PCB" src="https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/assets/ESP32-C3-BreadBoardAdapter.jpg" width="75%"/>

## Schematic

Schematic is availabe for [download](https://github.com/alexandrebobkov/ESP32-C3_Breadboard-Adapter/blob/main/schematic/ESP32-C3-BreadBoardAdapter_Schematic.pdf)

### Reserved GPIOs & Pins

| GPIO | Physical Pin | Adapter Pin | Description |
| --- | --- | --- | --- |
| EN | 1 | 2 | ESP32-C3 Enable pin |
| IO9 | 8 | 8 | Strapping pin |
| IO8 | 5 | 7 | Strapping pin |
| IO10 | 7 | 10 | On-board LED |
| IO3 | 13 | 15 | On-board push switch |

## Components List (Bill of Materials)

| Reference | Value | Description | Item Description |
| --- | --- | --- | --- |
| C1, C2 | 1uF | Capacitor | SMD |
| C4 | 10uF | Capacitor | SMD |
| C5 | 0.1uF | Capacitotr | SMD |
| R1, R2, R3, R7 | 5k1 | Resistor | SMD |
| R4, R5 | 10k | Resistor | SMD |
| R6, R8 | 2k2 | Resistor | SMD |
| D1, D2 | D | Diode | SMD |
| U1 | ESP32-C3-WROOM | ESP32 C3 Module | |
| U2 | AMS1117-3V3 | Voltage regulator 3.3V | |
| U3 | L58M05 | Voltage regulator 5.0V | |
| SW1, SW2, SW3 | SW | Push switch | SW_PUSH_6x3.5mm |
| LED1 | RGB LED | Red, Green, Blue LED | SMD B1552USUG20D |
| LED2 | RED LED | Power LED | SMD B1552 |
| J2 | USB-C | USB-C power and data reciptacle | USB-C_GCT_USB4085-GF-A | 