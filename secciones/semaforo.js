export function seccionSemaforo() {
    let section = document.createElement('section');
    section.className = "sectio-semaforo"

    let semaforo = document.createElement('div');
    semaforo.className = "semaforo";

    const colores = ['#c51a4a', '#eaaa00', '#008f39'];

    async function datosFireBase() {
        try {
            let respuesta = await fetch('https://semaforo-706f7-default-rtdb.firebaseio.com/.json');
            let datos = await respuesta.json();
            semaforo.innerHTML = '';
            
            semaforo.appendChild(luz(colores[0],datos.rojo));
            semaforo.appendChild(luz(colores[1],datos.amarillo));
            semaforo.appendChild(luz(colores[2],datos.verde));
        } catch (error) {
            console.log("Error al obtener datos de Firebase:", error);
        }
    }

    datosFireBase();

    // Actualización en tiempo real
    setInterval(datosFireBase,1000)

    section.appendChild(semaforo);
    return section;
}

function luz(color, estado) {
    let div = document.createElement('div');
    div.className = 'luz';
    div.style.backgroundColor = color;

    if (estado === 1) {
        div.style.boxShadow = `0 0 20px 8px ${color}`;
    } else {
        div.style.boxShadow = 'none';
    }

    return div;
}



document.body.appendChild(seccionSemaforo());
