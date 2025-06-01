from configuracion_red import conectar_wifi
from semaforo import encender_semaforo

# Lista de redes disponibles
REDES = [
    {'ssid': 'Turbonet.2', 'password': 'T-FORCErm'},
    {'ssid': 'iPh0ne', 'password': 'rm123456'},
    {'ssid': 'Turbonet.2', 'password': 'T-FORCErm'},
    {'ssid': 'fogel', 'password': '123456789'}
]

if conectar_wifi(REDES):
    print("Conectado a WiFi - Ejecutando programa principal")
    encender_semaforo(5)
else:
    print("Modo offline - Funcionalidades limitadas")
    