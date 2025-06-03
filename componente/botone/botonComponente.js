import { enviarDato } from "../../control/controlFireBase.js";
export function crearBoton(color,texto) {
    const boton = document.createElement('input');
    boton.type = 'button';
    boton.value = texto;
    boton.classList.add('mi-boton');
    boton.style.backgroundColor = color;

    // Evento para mostrar el color en consola
    boton.addEventListener('click', async () => {
        let contenido = boton.textContent || boton.value;
        if(contenido=="boton1"){
            enviarDato(1, contenido);
            enviarDato(0, "boton2");
            enviarDato(0, "boton3");
            enviarDato(0, "boton4");
        }else if(contenido=="boton2"){
            enviarDato(1, contenido);
            enviarDato(0, "boton1");
            enviarDato(0, "boton3");
            enviarDato(0, "boton4");
        }else if(contenido=="boton3"){
            enviarDato(1, contenido);
            enviarDato(0, "boton2");
            enviarDato(0, "boton1");
            enviarDato(0, "boton4");
        }else if(contenido=="boton4"){
            enviarDato(1, contenido);
            enviarDato(0, "boton2");
            enviarDato(0, "boton3");
            enviarDato(0, "boton1");
        }
    });

    return boton;
}
