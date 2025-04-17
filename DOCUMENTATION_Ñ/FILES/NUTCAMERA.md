# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTCAMERA.md).

## Clase NutCamera

[Esta clase extiende a la clase [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), aquellos atributos y mètodos obtenidos de él no se mostrarán por simplicidad]

Una camara que contiene otros objetos, tiene más libertad de movimiento.

### método init ()

### Atributos

###### angle : float

La rotación de la vista de la camara.

###### zoom : float

El zoom de la camara, el valor predeterminado es 1.

###### raylib_camera : pyray.Camera2D

La versión de raylib de la camara, usado para renderizar.