# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTFRAME.md).

## Clase NutFrame

Diseñado para obtener la posición de un frame de una animación para un sprite animado.

### método init (img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None, size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None, flipX : bool = False, flipY : bool = False, rotated : bool = False)

###### img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición del frame en la imagen original.

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño del frame en la imagen original.

###### offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None

El ajuste de la posición al ser mostrado en pantalla.

Si el valor es None, su valor será asignado a NutVector2(0, 0).

###### size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None

El ajuste del tamaño al ser mostrado en pantalla.

Si el valor es None, su valor será asignado a el atributo `img_size`.

###### flipX : bool = False

Si invertir este frame específico en el eje horizontal o no.

###### flipY : bool = False

Si invertir este frame específico en el eje vertical o no.

###### rotated : bool = False

Si rotar este frame específico 90 grados en el sentido contrario de las agujas del reloj (es decir, -90 grados) o no.

### Atributos

###### img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición del frame en la imagen original.

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño del frame en la imagen original.

###### offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El ajuste de la posición al ser mostrado en pantalla.

###### size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El ajuste del tamaño al ser mostrado en pantalla.

###### flipX : bool

Si invertir este frame específico en el eje horizontal o no.

###### flipY : bool

Si invertir este frame específico en el eje vertical o no.

###### rotated : bool

Si rotar este frame específico 90 grados en el sentido contrario de las agujas del reloj (es decir, -90 grados) o no.
