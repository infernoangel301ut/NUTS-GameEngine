# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTCAMERA.md).

## NutCamera Class

[This class extends the [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md) class, attributes and methods inherited from it will not be shown for simplicity]

A camera that contains other objects, has more movement freedom.

### init method ()

### Attributes

###### angle : float

The camera view rotation.

###### zoom : float

The camera zoom, default is 1.

###### raylib_camera : pyray.Camera2D

The raylib version of the camera, used for rendering.
