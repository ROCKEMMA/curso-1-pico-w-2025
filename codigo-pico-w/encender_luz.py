from machine import Pin
import time

def encender_led(pin, tiempo):
    led = Pin(pin, Pin.OUT)

    led.value(1)
    print("LED",pin,"Encendido ...")
    time.sleep(tiempo)
    led.value(0)
 

def encender_led_fijo(pin):
    led = Pin(pin, Pin.OUT)

    led.value(1)
    print("LED",pin,"Encendido ...")
    
def apagar_led_fijo(pin):
    led = Pin(pin, Pin.OUT)

    led.value(0)
    print("LED",pin,"Apagado ...")
