from flask import Flask, request, render_template, redirect, url_for, jsonify
from utils.validacion import validarDonante, validarDispositivo, validarForm
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

            msg = "Donación exitosa"
            return msg
        msg = "Error al ingresar contacto"
        return msg
    regiones = obtener_regiones()
    return render_template("html/agregar-donacion.html", regiones=regiones)

@app.route("/informacion-dispositivo")
def informacionDispositivo():
    return render_template("html/informacion-dispositivo.html")

@app.route("/ver-dispositivos")
def verDispositivos():
    return render_template("html/ver-dispositivos.html")


@app.route("/comunas/<int:region_id>")
def obtener_comunas(region_id):
    # Asumiendo que tienes una función que obtiene las comunas por región
    comunas = obtener_comunas_por_region(region_id)  # Asegúrate de que esta función esté implementada
    return jsonify(comunas)