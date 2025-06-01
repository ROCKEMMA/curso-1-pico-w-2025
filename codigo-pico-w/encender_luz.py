from machine import Pin
import time

def encender_led(pin, tiempo):
    led = Pin(pin, Pin.OUT)

    led.value(1)
    print("LED",pin,"Encendido ...")
    time.sleep(tiempo)
    led.value(0)
 
