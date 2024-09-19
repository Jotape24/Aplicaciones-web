# README Aplicación web

Alumno: José Pablo Canales

## Organizacion de archivos

Se organizo el proyecto diferenciando en 3 carpetas principales, las cuales cada una contiene archivos del tipo especificado, cada archivo tiene el nombre del archivo html que referencian. En el caso de los archivos JavaScript, se crearon subcarpetas para diferencias archivos JavaScript relacionados con cierto HTML, luego se crearon archivos JS para separar las distintas funciones que pueden tener para una misma pagina, con nombre de forma "nombreHTML-funcion.js". 

A continuación se muestra una guia de navegación por el proyecto:

    - css // se incluyen los archivos de tipo css
        - agregar-donacion.css
        - index.css
        - informacion-dispositivos.css
        - ver-dispositivos.css
    - html // se incluyen los archivos de tipo html
        - agregar-donacion.html
        - index.html
        - informacion-dispositivos.html
        - ver-dispositivos.html
    - javascript // se incluyen los archivos de tipo javascript
        - agregar-donacion
            - agregar-donacion-clonar.js
            - agregar-donacion-menu-desplegable.js
            - agregar-donacion-validacion.js
        - informacion-dispositivos
            - informacion-dispositivo-agrandar-imagen.js
            - informacion-dispositivo-validar-comm.js
            - informacion-dispositivos-mostrar-correcto.js


## Decisiones  de diseño

En esta sección se hablara sobre las desiciones tomadas en el diseño de cada pestaña.

### Index

Cumple el rol de menú principal en la pagina, este contiene los botones principales para navegar por esta, con un estilo basado en lo visto en clases auxiliares.

### Agregar donación

En esta pestaña se realiza una validación de los formularios, mostrando mensajes distintos en caso que este sea correcto o no. Ademas es posible agregar formularios de dispositivos adicionales, aunque de momento no supe como implementar la validación de estos ultimos.

### Ver dispositivos

En esta pestaña se decidio mostrar los dispositivos donados de una forma en particular y se le asigno a todos los elementos un hipervinculo para que se muestre la información deseada en la pestaña *Información dispositivos*

### Información dispositivos

En esta pestaña me entere tarde que tenia que mostrar lo mismo para todos los hipervinculos de la pestaña *Ver dispositivos*, por lo que utilice atributos hidden e hipervinculos de forma *informacion-dispositivo.html?dispositivo=id*, donde mediante un script javascript, que revela solo la información pedida.

Para el formulario de comentarios ya me habia enterado que se tenia que mostrar lo mismo siempre por lo que implemente uno solo para todos los dispositivos, este si atributo hidden.

