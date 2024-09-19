
const params = new URLSearchParams(window.location.search); // revisa la url
        const dispositivo = params.get('dispositivo'); 

        if (dispositivo) {
            const dispositivoDiv = document.getElementById(`${dispositivo}`);
            if (dispositivoDiv) {
                dispositivoDiv.hidden = false; // Elimina el atributo 'hidden' del dispositivo deseado
            }
        }