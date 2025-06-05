import urequests
from encender_luz import *
from control_firebase import *
import time

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

# semaforo_programado
# semaforo_en_verde
# semaforo_intermitente
# semaforo_en_rojo
contador_programas = [0,0,0,0]

# resetear contadores
def resetear_contadores(excepto):
    global contador_programas
    for i in range(len(contador_programas)):
        if i != excepto:
            contador_programas[i] = 0

def semaforo_programado(intervalo_de_tiempo):
    global contador_programas
    resetear_contadores(0)
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
    global contador_programas
    if contador_programas[1] == 0:
        resetear_contadores(1)
        enviar_datos({
            "rojo": 0,
            "verde": 1,
            "amarillo": 0
        })
        
        apagar_led_fijo(pines["amarillo"])
        apagar_led_fijo(pines["rojo"])
        encender_led_fijo(pines["verde"])
        contador_programas[1] = 1
    
def semaforo_intermitente():
    global contador_programas
    if contador_programas[2] == 0:
        resetear_contadores(2)
        contador_programas[2] = 1
        enviar_datos({
            "rojo": 0,
            "verde": 0,
            "amarillo": 1
        })
        apagar_led_fijo(pines["verde"])
        apagar_led_fijo(pines["rojo"])

    else:
        encender_led_fijo(pines["amarillo"])
        enviar_dato(encender, campos["amarillo"])
        #time.sleep(0.5)
        apagar_led_fijo(pines["amarillo"])
        enviar_dato(apagar, campos["amarillo"])
        #time.sleep(0.5)
    
def semaforo_en_rojo():
    global contador_programas
    if contador_programas[3] == 0:
        resetear_contadores(3)
        enviar_datos({
            "rojo": 1,
            "verde": 0,
            "amarillo": 0
        })
        apagar_led_fijo(pines["verde"])
        apagar_led_fijo(pines["amarillo"])
        encender_led_fijo(pines["rojo"])
        contador_programas[3] = 1
