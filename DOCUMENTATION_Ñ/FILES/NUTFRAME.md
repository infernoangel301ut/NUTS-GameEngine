# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutFrame

Diseñado para obtener la posición de un frame de una animación para un sprite animado.

### metodo init (img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None, size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None)

###### img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición del frame en la imagen original.

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño del frame en la imagen original.

###### offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None

El ajuste de la posición al ser mostrado en pantalla.

Si el valor es None, su valor será asignado a NutVector2(0, 0).

###### size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None = None

El ajuste del tamaño al ser mostrado en pantalla.

Si el valor es None, su valor será asignado a el atributo img_size.

### Atributos

###### img_position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición del frame en la imagen original.

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño del frame en la imagen original.

###### offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El ajuste de la posición al ser mostrado en pantalla.

###### size_offset : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El ajuste del tamaño al ser mostrado en pantalla.
