# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutCamera

[Esta clase extiende a la clase [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), los atributos y metodos obtenidos de él no se mostrarán por simplicidad.]

Una camara que contiene otros objetos, tiene más libertad de movimiento.

### metodo init ()

### Atributos

###### angle : float

La rotación de la vista de la camara.

###### zoom : float

El zoom de la camara, el valor predeterminado es 1.

###### raylib_camera : pyray.Camera2D

La versión de raylib de la camara, usado para renderizar.