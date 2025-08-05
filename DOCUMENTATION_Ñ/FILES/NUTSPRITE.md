# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSPRITE.md).

## Clase NutSprite

[Esta clase extiende a la clase [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), aquellos atributos y métodos obtenidos de él no se mostrarán por simplicidad]

Un sprite siendo mostrado en pantalla.

### método init (image_dir : str, position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2(), size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)NutVector2 | None = None)

###### image_dir : str

El directorio de la imagen del sprite.

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2()

La posición del sprite.

###### size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None

El tamaño del sprite.

Si el valor es None, el tamaño se asignará al tamaño de la imagen.

### Atributos

###### image_dir : str

El directorio de la imagen del sprite.

###### image : pyray.Texture

La verdadera imagen a ser mostrada.

###### display_image : pyray.Texture

El atributo `image`, pero modificado para encajar con el resto de atributos.

###### size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

El tamaño de la imagen mostrada.

###### angle : float

La rotación del sprite.

###### color : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

La modificación del color del sprite, `NutColor(255, 255, 255)` por predeterminado.

###### animation : [NutAnimationController](/DOCUMENTATION/FILES/NUTANIMATIONCONTROLLER.md)

Se encarga de las animaciones del sprite, en caso de estar animado.

###### scale : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

El multiplicador de tamaño relativo. El tamaño original es `NutVector2(1, 1)`.

###### flipX : bool

Si invertir el sprite horizontalmente o no.

###### flipY : bool

Si invertir el sprite verticalmente o no.

### Métodos

#### updateDisplay() -> None

Actualiza el sprite para añadir las propiedades cambiadas.
