document.getElementById('agregar-serpiente').addEventListener('click', function() {
    const container = document.getElementById('serpientes-container');
    const count = container.getElementsByClassName('serpiente').length + 1;

    const div = document.createElement('div');
    div.classList.add('serpiente');

    div.innerHTML = `
    
        <label for="serpiente-nombre-${count}">Nombre:</label>
        <input type="text" id="serpiente-nombre-${count}" name="serpiente-nombre" required><br>
        <label for="serpiente-longitud-${count}">Longitud:</label>
        <input type="number" id="serpiente-longitud-${count}" name="serpiente-longitud" required><br>
        <label for="serpiente-especie-${count}">Especie:</label>
        <input type="text" id="serpiente-especie-${count}" name="serpiente-especie" required><br>`;
    
    container.appendChild(div);
});

document,getElementById('terrario-form').addEventListener('submit', function(event){
    event.preventDefault();

    const formData = new formData(event.target);
    const terrario
}

)