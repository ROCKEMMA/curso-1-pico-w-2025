import urequests
from encender_luz import *
from control_firebase import enviar_dato

# Variables
encender = 1
apagar = 0

campos = {
    "rojo": "rojo.json",
    "amarillo": "amarillo.json",
    "verde": "verde.json"
}

pines = {
    "rojo": 15,
    "amarillo": 14,
    "verde": 13
}

def semaforo_programado(intervalo_de_tiempo):    
    # Luz verde
    enviar_dato(encender, campos["verde"])
    encender_led(pines["verde"], intervalo_de_tiempo)
    enviar_dato(apagar, campos["verde"])
        
    # Luz amarilla
    enviar_dato(encender, campos["amarillo"])
    encender_led(pines["amarillo"], intervalo_de_tiempo)
    enviar_dato(apagar, campos["amarillo"])

    # Luz roja
    enviar_dato(encender, campos["rojo"])
    encender_led(pines["rojo"], intervalo_de_tiempo)
    enviar_dato(apagar, campos["rojo"])
    
def semaforo_en_verde():
    enviar_dato(encender, campos["verde"])
    
    enviar_dato(apagar, campos["rojo"])
    apagar_led_fijo(pines["rojo"])
    enviar_dato(apagar, campos["amarillo"])
    apagar_led_fijo(pines["amarillo"])
    
    encender_led_fijo(pines["verde"])
    
def semaforo_intermitente():
    enviar_dato(encender, campos["amarillo"])
    
    enviar_dato(apagar, campos["verde"])
    apagar_led_fijo(pines["verde"])
    enviar_dato(apagar, campos["rojo"])
    apagar_led_fijo(pines["rojo"])
    
    encender_led(pines["amarillo"], 1)
    enviar_dato(apagar, campos["amarillo"])
    
def semaforo_en_rojo():
    enviar_dato(encender, campos["rojo"])
    
    enviar_dato(apagar, campos["verde"])
    apagar_led_fijo(pines["verde"])
    enviar_dato(apagar, campos["amarillo"])
    apagar_led_fijo(pines["amarillo"])
    
    encender_led_fijo(pines["rojo"])
