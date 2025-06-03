export function luz(color, estado) {
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
