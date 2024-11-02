from flask import Flask, request, render_template, redirect, url_for, jsonify
from utils.validacion import validarDonante, validarDispositivo, validarComentario
from database.db import *
from datetime import datetime
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid


UPLOAD_FOLDER = 'static/uploads'




app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  

@app.route("/")
def index():
    return render_template("html/index.html")


@app.route("/agregar-donacion", methods=["GET", "POST"])
def agregarDonacion() :
    if request.method == "POST":
        print(request.form)
        # usuario
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")
        region = request.form.get("region")
        comuna = request.form.get("comuna")

        print(f"Nombre: {nombre}, Email: {email}, Celular: {celular}, Región: {region}, Comuna: {comuna}")

        # dispositivo
        dispositivo = request.form.get("dispositivo")
        descripcion = request.form.get("descripcion")
        tipo = request.form.get("tipo")
        años = request.form.get("años")
        estado = request.form.get("estado")
        imgs = request.files.getlist("imagenes")

        print(f"estado: {estado}")

        # hora
        fecha_creacion = datetime.now()






        if validarDonante(nombre, celular, email):
            if not (validarDispositivo(dispositivo, años, imgs)):
                msg = "Error al ingresar dispositivo"
                return msg
            contacto = agregar_contacto(nombre, email, celular, comuna, fecha_creacion)
            disp = agregar_dispositivo(contacto, dispositivo, descripcion, tipo, años, estado)

            # subir foto
            for img in imgs:
                _filename_hash = hashlib.sha256(
                    secure_filename(img.filename).encode("utf-8")
                    ).hexdigest()

                _extension = filetype.guess(img).extension

                img_filename = f"{_filename_hash}_{str(uuid.uuid4())}.{_extension}" 

                # guardar
                img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                arch = insertar_archivo("UPLOAD_FOLDER", img_filename, disp)
            
        else: 
            msg = "Error al ingresar contacto"
            return msg
    regiones = obtener_regiones()
    return render_template("html/agregar-donacion.html", regiones=regiones)

@app.route("/informacion-dispositivo/<int:id>", methods=["GET", "POST"])
def informacionDispositivo(id):
    
    dispositivo = obtener_dispositivo_por_id(id)  
    donante = obtener_donante_por_dispositivo(id) 

    if dispositivo is None:
        return "Dispositivo no encontrado", 404 
    
    if donante is None:
        return "Donante no encontrado", 404
    
    # mostrar info

    id_dispositivo, _, nombreDispositivo, descripcion, tipo, años, estado = dispositivo
    nombre, email, numero, comunaID = donante

    fotos = obtener_fotos_por_dispositivo(id_dispositivo) 
    comuna = obtener_comuna_por_id(comunaID)
    region = obtener_region_por_comuna_id(comunaID)
    print("1")
    data = {
        "nombre":nombre, 
        "email":email,
        "numero":numero,
        "region":region,
        "comuna":comuna,
        "dispositivo":nombreDispositivo,
        "dispositivo_id": id_dispositivo,
        "descripcion":descripcion,
        "tipo":tipo,
        "años":años,
        "estado":estado,
        "fotos":fotos
    }
    print("2")
    dir_fotos = [url_for('static', filename=f'uploads/{foto[0]}') for foto in fotos]
    print("3")

    # mostrar comentarios
    comentarios = obtener_comentario(id_dispositivo)
    data2 = []
    for comm in comentarios:
        nombre, texto, fecha = comm
        data2.append({
            "nombre":nombre,
            "texto":texto,
            "fecha": fecha
        })

    # agregar comentarios

    if request.method == "POST":
        print(request.form)
        nombre_form = request.form.get("com-text-area-name")
        comentario_form = request.form.get("com-text-area")
        fecha = datetime.now()
        print(f"Nombre: {nombre_form}, Comentario: {comentario_form}, Fecha: {fecha} se tienen los valores")
        if validarComentario(nombre_form, comentario_form):
            print(f"Nombre: {nombre_form}, Comentario: {comentario_form}, Fecha: {fecha} se valido")
            insertar_comentario(nombre_form, comentario_form, fecha, id_dispositivo)
            
            return redirect(url_for('informacionDispositivo', id=id))
        

        
    
    return render_template("html/informacion-dispositivo.html", data=data, dir_fotos=dir_fotos, data2=data2)

@app.route("/ver-dispositivos", methods=["GET"])
def verDispositivos():

    # parametro de pagina 
    page = int(request.args.get('page', 1))
    limit = 5
    offset = (page - 1) * limit

    dispositivos = obtener_dispositivos_paginados(offset, limit)

    hay_siguiente = len(dispositivos) == limit

    data = []
    for disp in dispositivos:
        id_dispositivo, id_donante, nombre, _, tipo, _, estado = disp
        comuna = obtener_comuna_por_contacto(id_donante)[0]  
        fotos = obtener_fotos_por_dispositivo(id_dispositivo)

        # lista de URLs
        dir_fotos = [url_for('static', filename=f'uploads/{foto[0]}') for foto in fotos]

        data.append({
            "tipo": tipo,
            "nombreDispositivo": nombre,
            "estado": estado,
            "comuna": comuna,
            "dirFotos": dir_fotos,
            "id": id_dispositivo
        })

    return render_template("html/ver-dispositivos.html", data=data, page=page, hay_siguiente=hay_siguiente)


@app.route("/comunas/<int:region_id>")
def obtener_comunas(region_id):
    
    comunas = obtener_comunas_por_region(region_id)  
    return jsonify(comunas)