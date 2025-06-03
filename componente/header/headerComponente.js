export function header() {
    let header = document.createElement('header');
    header.style.display = 'flex';
    header.style.justifyContent = 'space-between';
    header.style.alignItems = 'center';
    header.style.padding = '10px 10px';
    header.style.boxShadow = '0 1px 3px rgba(0, 0, 0, 0.08)';

    // Sección izquierda con logo y texto
    let leftSection = document.createElement('div');
    leftSection.style.display = 'flex';
    leftSection.style.alignItems = 'center';
    let logo = document.createElement('img');
    logo.src = 'imagenes/raspberry.svg'; // Ajusta la ruta si es diferente
    logo.alt = 'Logo Raspberry Pi Pico W';
    logo.style.height = '40px';
    logo.style.marginRight = '10px';

    let title = document.createElement('span');
    title.textContent = 'Raspberry Pi Pico W';
    title.style.fontWeight = 'bold';
    title.style.fontSize = '18px';

    leftSection.appendChild(logo);
    leftSection.appendChild(title);

    // Sección derecha con versión
    let version = document.createElement('span');
    version.textContent = '1.0v';
    version.style.fontSize = '16px';

    // Añadir ambos al header
    header.appendChild(leftSection);
    header.appendChild(version);

    return header;
}

document.body.appendChild(header());