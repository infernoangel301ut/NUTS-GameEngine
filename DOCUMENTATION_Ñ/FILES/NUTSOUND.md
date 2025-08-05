# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSOUND.md).

## Clase NutSound

La clase empleada para efectos de sonido (UTILIZA [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md) PARA LA MÚSICA).

### método init (path : str, volume : float = 0.5, pitch : float = 1)

###### path : str

La ubicación del sonido que quieres reproducir.

###### volume : float = 0.5

El volumen del sonido.

###### pitch : float = 1

El tono del sonido (el tono original tiene como valor 1).

### Atributos

###### file_path : str

La ubicación del sonido que quieres reproducir.

###### raylib_audio : pyray.Sound

La versión de raylib del sonido.

###### volume : float

El volumen del sonido.

###### pitch : float

El tono del sonido (el tono original tiene como valor 1).

###### paused : bool

Si el sonido está pausado o no.

###### playing : bool

Si el sonido se esta reproduciendo o no.

###### pan : float

La dirección a la que va el sonido, mayormente para auriculares.

(0 es izquierda, 1 es derecha, y 0.5 es por el medio).
