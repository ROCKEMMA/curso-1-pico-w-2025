import urequests

def enviar_dato(valor, campo):
    url = f'https://semaforo-706f7-default-rtdb.firebaseio.com/{campo}'
    
    response = urequests.put(url, json=valor)
    response.close()