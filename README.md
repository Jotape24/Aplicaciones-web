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
            - index.css
            - informacion-dispositivos.css
            - ver-dispositivos.css
    - imagenes // imagenes de la tarea 1
    - javascript // se incluyen los archivos de tipo javascript
        - agregar-donacion
            - agregar-donacion-clonar.js
            - agregar-donacion-validacion.js
            - cargar-comunas.js
        - informacion-dispositivos
            - informacion-dispositivo-agrandar-imagen.js
            - informacion-dispositivo-validar-comm.js
            - informacion-dispositivos-mostrar-correcto.js
        - redirect.js
    - uploads // carpeta a donde van las imagenes subidas

    - templates
        - html // se incluyen los archivos de tipo html
            - agregar-donacion.html
            - index.html
            - informacion-dispositivos.html
            - ver-dispositivos.html
    - utils
        - validacion.py
    - app.py


## Decisiones  de diseño

En esta sección se hablara sobre las desiciones tomadas en el diseño de cada pestaña.

## General

Para toda la tarea tuve que crear consultas adicionales a las entregadas para la tarea, estas se encuentran en el archivo json y fueron implementadas a python en el archivo db.py para luego ser ocupadas en las distintas rutas de la app.

Fue muy util usar diccionarios en app.py para luego poder acceder a caracteristicas deseadas en cada template.


### Index

Cumple el rol de menú principal en la pagina, este contiene los botones principales para navegar por esta, con un estilo basado en lo visto en clases auxiliares.

### Agregar donación

En esta sección se trabajo un POST de información a la base de datos y se implemento que los campos region y comuna se poblen basados en la base de datos, region se poblo con un if de jinja y comuna en el archivo cargar-comunas.js. El retorno de una donación exitosa es una pagina que usando js hace que luego de un tiempo determinado redirige al menu principal.

### Ver dispositivos

Ahora las filas son clickables y envian a una pagina Informacion dispositivos para cada una. Se logro recuperar de la base de datos los dispositivos donados para luego se mostrados en pantalla, implementando ademas un boton para avanzar en los dispositivos mostrados, aunque no supe como eliminarlo cuando no quedaban elementos por mostrar. Para la correcta funcionalidad de esto tuve que crear una nueva consulta de base de datos llamada "obtener_dispositivos_paginados" para poder avanzar en la db.

### Información dispositivos

Esta pestaña depende enteramente de "Ver dispositivos", en la pestaña anterior el hipervinculo genera un id que va a mostrar la información necesaria en esta.

