
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

led_value = True

while True:
    led.value(led_value)
    led_value = not led_value
    time.sleep(1)


