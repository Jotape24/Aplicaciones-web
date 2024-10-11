function cargarComunas() {
    const regionId = document.getElementById("region").value;
    const comunaSelect = document.getElementById("comuna");

    // Limpiar las opciones existentes
    comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';

    if (regionId) {
        fetch(`/comunas/${regionId}`)
            .then(response => response.json())
            .then(data => {
                data.forEach(comuna => {
                    const option = document.createElement("option");
                    option.value = comuna.id; // o el campo que uses como identificador
                    option.textContent = comuna.nombre; // o el campo que quieras mostrar
                    comunaSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error al cargar comunas:', error));
    }
}