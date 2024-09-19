// para ver si el comentario es valido
const validate = (comentario, name) => {
    const regexName = /^[a-zA-Z\s]+$/;
    const validName = (name) => name && name.length <= 80 && name && name.length >= 3 && regexName.test(name);
    const validText = (comentario) => comentario && comentario.length >= 5;

    let isValid = validName(name) && validText(comentario);
    return {comText: comentario, name:name, isValid:isValid};
};

const agregarComentario = () => {
    const comTextArea = document.getElementById("com-text-area");
    const comTextAreaName = document.getElementById("com-text-area-name");

    let validationBox = document.getElementById("val-box");

    const {comText, name, isValid} = validate(comTextArea.value, comTextAreaName.value);

    if(!isValid) {
        validationBox.innerText = "Comentario invalido!";
        // aplicar estilos de error
        validationBox.style.backgroundColor = "#ffdddd";
        validationBox.style.borderLeftColor = "#f44336";

        // hacer visible el mensaje de validación
        validationBox.hidden = false;
        return;
    }
    else {
        validationBox.innerText = "Se ha agregado tu comentario!";
        // aplicar estilos de aceptación
        validationBox.style.backgroundColor = "#ddffdd";
        validationBox.style.borderLeftColor = "#4CAF50";

        // hacer visible el mensaje de validación
        validationBox.hidden = false;
    }

    // se crea el comentario
    const container = document.createElement("div");
    container.className = "com-container";

    const comAuthor = document.createElement("div");
    comAuthor.className = "com-author";
    const userNameParagraph = document.createElement("p");
    userNameParagraph.innerText = name;
    comAuthor.appendChild(userNameParagraph);

    const commentText = document.createElement("p");
    commentText.innerText = comText;

    container.appendChild(comAuthor);
    container.appendChild(commentText);

    const comList = document.querySelector(".com-list");
    comList.appendChild(container);

    comTextArea.value = "";
    comTextAreaName.value = "";
};

const submitBtn = document.getElementById("submit-com-btn");
submitBtn.addEventListener("click", agregarComentario);