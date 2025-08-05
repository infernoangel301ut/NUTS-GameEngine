# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTMUSIC.md).

## Clase NutMusic

La clase utilizada para la música (UTILIZA [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md) PARA EFECTOS DE SONIDO).

### método init (path : str, looped : bool = False, volume : float = 0.5, pitch : float = 1)

###### path : str

La ubicación de la música que quieres reproducir.

###### looped : bool = False

Si la música debería reproducirse en bucle o no.

###### volume : float = 0.5

El volumen de la música.

###### pitch : float = 1

El tono de la música (el tono original tiene como valor 1).

### Atributos

###### file_path : str

La ubicación de la música que quieres reproducir.

###### raylib_audio : pyray.Music

La versión de raylib de la música.

###### looped : bool

Si la música debería reproducirse en bucle o no.

###### volume : float

El volumen de la música.

###### pitch : float

El tono de la música (el tono original tiene como valor 1).

###### paused : bool

Si la música está pausada o no.

###### playing : bool

Si la música se está reproduciendo o no.

###### pan : float

La dirección a la que va la música, mayormente para auriculares.

(0 es izquierda, 1 es derecha, y 0.5 es por el medio).