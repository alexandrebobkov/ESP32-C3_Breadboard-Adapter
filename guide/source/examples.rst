Examples
=========

MicroPython Blinky Example
----------

The following code written in MicroPython runs a timer to periodically blink the on-board LED wired to the GPIO10 (Pin 7). 
Button wired to the GPIO3 (Pin 13) interrupts the pulse cycle.

.. code-block:: python
    :linenos:

    import machine
    from machine import Pin
    import time, math

    ONBOARD_LED = 10    # GPIO10, PIN 7
    ONBOARD_BTN = 3     # GPIO3, PIN 13

    # Configure on-board LED and push button
    # Stated GPIOs correspond to the wiring schematic
    onboard_button = Pin(ONBOARD_BTN, Pin.IN, Pin.PULL_UP)

    # Assign on-board LED to the PWM and cycle its brightness.
    led = machine.PWM(ONBOARD_LED, freq=1000)
    def pulse(l, t):
        for i in range(20):
            l.duty(int(math.sin(i/10 * math.pi) * 500 + 500))
            time.sleep_ms(t)
        l.duty(0)
        
    # Interrupt function to turn LED ON when on-board button is pressed
    def button_interrupt(pin):
        pulse(led, 70)
        
    def main():
    
        # Assign interrupt to the on-board push button
        onboard_button.irq(trigger=Pin.IRQ_FALLING, handler=button_interrupt)
    
    if __name__ == '__main__':
        main()