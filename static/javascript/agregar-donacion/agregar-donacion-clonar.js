const btnClonar = document.getElementById("agregar-dispositivos");
const container = document.getElementById("informacion-producto");

let fragmentCount = 0;

btnClonar.addEventListener("click", () => {
    // Clonar el fragmento
    const fragmentOriginal = document.getElementById("informacion-producto");
    const clonedFragment = fragmentOriginal.cloneNode(true);

    // Incrementar el contador para los id y nombres unicos
    fragmentCount++;

    // Modificar los id y nombres del fragmento clonado
    const inputs = clonedFragment.querySelectorAll("input, select, textarea");
    inputs.forEach((input, index) => {
        input.id = `${input.id}-${fragmentCount}`;
        input.name = `${input.name}-${fragmentCount}`;
        if (input.tagName === "INPUT" || input.tagName === "TEXTAREA") {
            input.value = ""; // vaciar el valor del input clonado
        }
    });

    // Añadir el fragmento clonado debajo del original
    fragmentOriginal.after(clonedFragment);
});