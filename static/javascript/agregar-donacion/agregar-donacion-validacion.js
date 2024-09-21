// Validaciones

//nombre

const validadorNombreDonante = (input) => {
    let valido = false;
    const nombreValido = /^[a-zA-Z\s]+$/
    if(input && input.trim().length >= 3 && input.trim().length <= 80 && nombreValido.test(input)){
        valido = true;
    }
    return valido;
};



// email


const validadorEmailDonante = (input) => {
    let valido = false;
    const emailValido = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (input && emailValido.test(input)) {
        valido = true;
    }
    return valido;
};



// telefono

const validadorTelefonoDonante = (input) => {
    let valido = false;
    const telefonoValido = /^(\+56|56)?[ -]*(2|9)[ -]*([0-9][ -]*){8}$/;
    if (telefonoValido.test(input) || !input) {
        valido = true;
    }
    return valido;
};



// nombre dispositivo


const validadorNombreDispositivo = (input) => {
    let valido = false;
    if(input && input.trim().length >= 3 && input.trim().length <= 80){
        valido = true;
    }
    return valido;
};


// años de uso


const validadorAñosUso = (input) => {
    let valido = false;
    const numero = años.value;
    if (input && input>=1 && input<= 99 && !isNaN(numero) && numero-Math.trunc(numero) == 0) {
        valido = true
    }
    return valido
};



// campos con menu de seleccion

const validadorMenu = (input) => {
    let valido = false;
    if (input && input !== "") {
        valido = true;
    }
    return valido;
};

// fotos

const validadorFotos = (input) => {
    let valido = false;
    const cantidad = input.files.length;
    if (input && cantidad <=3 && cantidad >=1) {
        valido = true;
    }
    return valido;
};




const validarForm = () => {
    console.log("Enviando...");

    const myForm = document.querySelector(".formulario");
    const nombreDonante = document.getElementById("nombre"); // nombre del donante
    const email = document.getElementById("email"); // email del donante
    const tel = document.getElementById("celular"); // numero del donante
    const region = document.getElementById("region"); // region del donante
    const comuna = document.getElementById("comuna"); // comuna del donante
    const dispositivo = document.getElementById("dispositivo"); // nombre del dispositivo
    const años = document.getElementById("años"); // años de uso
    const tipo = document.getElementById("tipo"); // tipo de dispositivo
    const estado = document.getElementById("estado"); // estado del dispositivo
    const foto = document.getElementById("image") // fotos de productos

    const tituloPrincipal = document.getElementById("titulo-principal");
    const infoDonante = document.getElementById("informacion-donante");
    const infoProducto = document.getElementById("informacion-producto");
    const menu = document.querySelector(".opciones-menu");

    

    // variables para validación
    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };


    if(!validadorNombreDonante(nombreDonante.value)) {
        nombreDonante.style.borderColor = "red";
        setInvalidInput("Nombre Donante");
        nombreDonante.setCustomValidity(
            "Nombre invalido",
        );
    } else {
        nombreDonante.style.borderColor = "";
        nombreDonante.setCustomValidity("");
    }

    if(!validadorEmailDonante(email.value)) {
        email.style.borderColor = "red";
        setInvalidInput("Email Donante");
        email.setCustomValidity(
            "Dirección invalida de correo electrónico"
        );
    } else {
        email.style.borderColor = "";
        email.setCustomValidity("");
    }

    if(!validadorTelefonoDonante(tel.value)) {
        tel.style.borderColor = "red";
        setInvalidInput("Número Celular Donante");
        tel.setCustomValidity(
            "Número de telefono invalido"
        );
    } else {
        tel.style.borderColor = "";
        tel.setCustomValidity("");
    }

    if(!validadorMenu(region.value)) {
        region.style.borderColor = "red";
        setInvalidInput("Región");
        region.setCustomValidity(
            "Debe seleccionar una región."
        );
    } else {
        region.style.borderColor = "";
        region.setCustomValidity("");
    }

    if(!validadorMenu(comuna.value)) {
        comuna.style.borderColor = "red";
        setInvalidInput("Comuna");
        comuna.setCustomValidity(
            "Debe seleccionar una comuna."
        );
    } else {
        comuna.style.borderColor = "";
        comuna.setCustomValidity("");
    }


    if(!validadorNombreDispositivo(dispositivo.value)) {
        dispositivo.style.borderColor = "red";
        setInvalidInput("Nombre dispositivo");
        dispositivo.setCustomValidity(
            "Nombre de dispositivo invalido"
        );
    } else {
        dispositivo.style.borderColor = "";
        dispositivo.setCustomValidity("");
    }

    if(!validadorMenu(tipo.value)) {
        tipo.style.borderColor = "red";
        setInvalidInput("Tipo");
        tipo.setCustomValidity(
            "Debe seleccionar un tipo."
        );
    } else {
        tipo.style.borderColor = "";
        tipo.setCustomValidity("");
    }

    if(!validadorAñosUso(años.value)) {
        años.style.borderColor = "red";
        setInvalidInput("Años de uso");
        años.setCustomValidity(
            "Debe ser un número entero entre 1 y 99"
        );
    } else {
        años.style.borderColor = "";
        años.setCustomValidity("");
    }

    if(!validadorMenu(estado.value)) {
        estado.style.borderColor = "red";
        setInvalidInput("Estado funcionamiento");
        estado.setCustomValidity(
            "Debe seleccionar un estado."
        );
    } else {
        estado.style.borderColor = "";
        estado.setCustomValidity("");
    }

    if(!validadorFotos(foto)) {
        foto.style.borderColor = "red";
        setInvalidInput("Fotos de Productos");
        foto.setCustomValidity(
            "Debe seleccionar entre 1 y 3 fotos."
        );
    } else {
        foto.style.borderColor = "";
        foto.setCustomValidity("");
    }

 
  let validationBox = document.getElementById("val-box");
  let validationMessageElem = document.getElementById("val-msg");
  let validationListElem = document.getElementById("val-list");
  let formContainer = document.querySelector(".container");

  if (!isValid) {
    validationListElem.textContent = "";
    // agregar elementos invalidos
    for (input of invalidInputs) {
      let listElement = document.createElement("li");
      listElement.innerText = input;
      validationListElem.append(listElement);
    }
    // establecer mensaje
    validationMessageElem.innerText = "Los siguientes campos son inválidos:";

    // aplicar estilos de error
    validationBox.style.backgroundColor = "#ffdddd";
    validationBox.style.borderLeftColor = "#f44336";

    // hacer visible el mensaje
    validationBox.hidden = false;
  }
  else {
    tituloPrincipal.style.display = "none";  // Oculta el título principal
    infoDonante.style.display = "none";  // Oculta el contenedor de información del donante
    infoProducto.style.display = "none"; // Oculta el contenedor de producto
    menu.style.display = "none";

    // establecer mensaje de aceptacion
    validationMessageElem.innerText = "¿Confirma que desea publicar esta donación?";
    validationListElem.textContent = "";

    validationBox.style.backgroundColor = "#ddffdd";
    validationBox.style.borderLeftColor = "#4CAF50";

    let menuButton = document.createElement("button");
    menuButton.innerText = "Ir al Menú Principal";
    menuButton.hidden = true;
    menuButton.addEventListener("click", () => {
      window.location.href = "../html/index.html"; // Redirige al menú principal
    });

    // Agregar botones para enviar el formulario o volver
    let submitButton = document.createElement("button");
    submitButton.innerText = "Sí, confirmo";
    submitButton.style.marginRight = "10px";
    submitButton.addEventListener("click", () => {
      // hacer que se vea el boton de regreso al menu
      // cambiar el texto de val-box
      submitButton.hidden = true;
      backButton.hidden = true;
      validationMessageElem.innerText = "Hemos recibido la información de su donación. Muchas gracias.";
      menuButton.hidden = false;
    });

    let backButton = document.createElement("button");
    backButton.innerText = "No, quiero volver al formulario";
    backButton.addEventListener("click", () => {
        // Mostrar el formulario nuevamente
        tituloPrincipal.style.display = "block";
        infoDonante.style.display = "block";
        infoProducto.style.display = "block";
        menu.style.display = "block";
        validationBox.hidden = true;
    });
    validationListElem.appendChild(menuButton);
    validationListElem.appendChild(submitButton);
    validationListElem.appendChild(backButton);

    validationBox.hidden = false;
  }
};




const boton1 = document.getElementById("publicar-donacion");

boton1.addEventListener("click", validarForm);


