from machine import Pin
from machine import Timer
from utime import sleep_ms

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
networks = wlan.scan()

ONBOARD_LED = 10	# GPIO10, PIN 7
ONBOARD_BTN = 3		# GPIO3, 13

# Configure on-board LED and push button
# Stated GPIOs correspond to the wiring schematic
onboard_led = Pin(ONBOARD_LED, Pin.OUT)
onboard_button = Pin(ONBOARD_BTN, Pin.IN, Pin.PULL_UP)

# Interrupt function to alternate on-board LED state
def led_interrupt(t):
    onboard_led.value(not onboard_led.value())
  
# Interrupt function to turn LED ON when on-board button is pressed
def button_interrupt(pin):
    print("Button was pressed")
    onboard_led.value(1)
    
def main():
    onboard_led_timer = Timer(0)
#    connect_wireless()
    
    if not wlan.isconnected():
        onboard_led_timer.init(mode=Timer.PERIODIC,period=500,callback=led_interrupt)
        print("Connecting to Wi-Fi ...")
        wlan.connect('IoT_bots', '208208208')
    
    if wlan.isconnected():
        print("Connected to Wi-Fi: " +wlan.config('ssid'))
        print("Channel: ", wlan.config('channel'))
        print("Security: ", wlan.config('hostname'))
        print(wlan.ifconfig())
        onboard_led_timer.init(mode=Timer.PERIODIC,period=1500,callback=led_interrupt)
 
    # Assign interrupt to the on-board push button
    onboard_button.irq(trigger=Pin.IRQ_FALLING, handler=button_interrupt)

if __name__ == '__main__':
    main()
