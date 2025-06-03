export function enviarDato(valor, campo) {
    fetch(`https://semaforo-706f7-default-rtdb.firebaseio.com/${campo}.json`, {
        method: 'PUT',
        body: JSON.stringify(valor)
    })
    .then(res => res.json())
    .then(data => console.log('Enviado:', data))
    .catch(err => console.error('Error:', err));
}

