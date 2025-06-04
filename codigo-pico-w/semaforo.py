import urequests
from encender_luz import *
from control_firebase import *
from programas_del_semaforo import *

def encender_semaforo():
    
    while True:
        if leer_dato("boton4") == 1:
            print("semaforo programado")
            semaforo_programado(5)
        elif leer_dato("boton1") == 1:
            print("Semaforó en verde")
            semaforo_en_verde()
            
        elif leer_dato("boton2") == 1:
            print("Modo intermitente")
            semaforo_intermitente()
            
        elif leer_dato("boton3") == 1:
            print("Semaforo en rojo")
            semaforo_en_rojo()
