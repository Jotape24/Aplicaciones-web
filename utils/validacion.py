import re 

def validarNombreDonante(nombre):
    regex = r'^[a-zA-Z\s]+$'
    trimmed = nombre.strip()
    bool = (re.match(regex, nombre) and len(trimmed) >= 3 and len(trimmed <=80))
    return bool

def validarNumeroTelefonico(numero):
    regex = r'^(\+56|56)?[ -]*(2|9)[ -]*([0-9][ -]*){8}'
    bool = (re.match(regex, numero) and len(numero) >= 8)
    return bool

def validarCorreo(correo):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]'
    bool = (re.match(regex, correo))
    return bool

def validarNombreDispositivo(nombre):
    trimmed = nombre.strip()
    bool = (len(trimmed) >= 3 and len(trimmed <=80))
    return bool

def validarAñosDeUso(años):
    añosVal = int(años)
    bool = añosVal >= 1 and añosVal <= 99
    return bool

def validarImg(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if img is None:
        return False

    # check if the browser submitted an empty file
    if img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validarImgs(imgs):
    for img in imgs:
        if not validarImg(img):
            return False
    return True

def validarDonante(nombre, numero, correo):
    return validarNombreDonante(nombre) and validarNumeroTelefonico(numero) and validarCorreo(correo)

def validarDispositivo(nombre, años, imgs):
    return validarNombreDispositivo(nombre) and validarAñosDeUso(años) and validarImgs(imgs)

def validarForm(nombreDonante, numero, correo, nombreDispositivo, años, imgs):
    return validarDonante(nombreDonante, numero, correo) and validarDispositivo(nombreDispositivo, años, imgs)