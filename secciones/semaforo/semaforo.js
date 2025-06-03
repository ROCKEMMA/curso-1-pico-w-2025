import { luz } from "../../componente/luz/luzComponente.js";

function seccionSemaforo() {
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
    setInterval(datosFireBase,500)

    section.appendChild(semaforo);
    return section;
}



document.body.appendChild(seccionSemaforo());
