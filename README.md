# README Aplicación web

Alumno: José Pablo Canales

## Organizacion de archivos

El proyecto se organizo en base a las carpetas *database*, *static*, *templates* y *utils*, donde en database esta todo lo relacionado a la base de datos, en template se encuentran archivos css, js e imagenes, en templates se encuentran los archivos html y en utils un archivo de validación en python.

A continuación se muestra una guia de navegación por el proyecto:

    - database
        - db.py
        - querys.json
        - region-comuna.sql
        - sentencias.sql
        - tarea2.sql

    - static
        - css // se incluyen los archivos de tipo css
            - agregar-donacion.css
            - graficos.css
            - index.css
            - informacion-dispositivos.css
            - ver-dispositivos.css
    - imagenes // imagenes de la tarea 1
    - javascript // se incluyen los archivos de tipo javascript
        - agregar-donacion
            - agregar-donacion-clonar.js
            - agregar-donacion-validacion.js
            - cargar-comunas.js
        - graficos
            - grafico-contactos.js
            - grafico-dispositivos-js
        - informacion-dispositivos
            - informacion-dispositivo-agrandar-imagen.js
            - informacion-dispositivo-validar-comm.js
            - informacion-dispositivos-mostrar-correcto.js
        - redirect.js
    - uploads // carpeta a donde van las imagenes subidas

    - templates
        - html // se incluyen los archivos de tipo html
            - agregar-donacion.html
            - grafico-contactos.html
            - grafico-dispositivos.html
            - index.html
            - informacion-dispositivos.html
            - ver-dispositivos.html
    - utils
        - validacion.py
    - app.py


## Decisiones  de diseño

En esta sección se hablara sobre las desiciones tomadas en el diseño de cada pestaña.

### General

Ambas pestañas de graficos se realizaron de forma similar, se uso highcharts para generar el grafico y fetch para llenarlo con la información correcta desde la base de datos, eso se ve el los archivos js dentro de la carpeta static/javascript/graficos.

### Información dispositivos

En esta pestaña ocurrieron modificaciones, ahora el formulario es funcional, este tiene un boton que llama al archivo js informacion-dispositivo-validar-comm, cuando ya esta validado el formulario, se hace el submit para revisarlo en app.py y agregarlo a la base de datos.

Para mostrar los comentarios adecuados en la base de datos se agrego una variable data2 en app.py para luego llamarla desde el template y asi seleccionarl la información correcta, esto usando una consulta de base de datos implementada en db.py.


