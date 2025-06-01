import urequests
from encender_luz import encender_led
from control_firebase import enviar_dato

def encender_semaforo(intervalo_de_tiempo):
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

    while True:
        # Luz roja
        enviar_dato(encender, campos["rojo"])
        encender_led(pines["rojo"], intervalo_de_tiempo)
        enviar_dato(apagar, campos["rojo"])

        # Luz amarilla
        enviar_dato(encender, campos["amarillo"])
        encender_led(pines["amarillo"], intervalo_de_tiempo)
        enviar_dato(apagar, campos["amarillo"])

        # Luz verde
        enviar_dato(encender, campos["verde"])
        encender_led(pines["verde"], intervalo_de_tiempo)
        enviar_dato(apagar, campos["verde"])

