from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("html/index.html")


@app.route("/agregar-donacion")
def agregarDonacion():
    return render_template("html/agregar-donacion.html")

@app.route("/informacion-dispositivo")
def informacionDispositivo():
    return render_template("html/informacion-dispositivo.html")

@app.route("/ver-dispositivos")
def verDispositivos():
    return render_template("html/ver-dispositivos.html")