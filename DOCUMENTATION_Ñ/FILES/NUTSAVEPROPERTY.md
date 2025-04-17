# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSAVEPROPERTY.md).

## Clase NutSaveProperty

Propiedad que se almacena en un archivo de guardado.

### método init (name : str, val_type : type, val : any)

###### name : str

El nombre de la propiedad. Se utilizará para acceder a ella.

###### val_type : type

El tipo de valor que quieres guardar. Solo acepta los siguientes: int, float, bool, str, [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md).

###### val : any

El valor que quieres guardar.

### Atributos

###### name : str

El nombre de la propiedad. Se utilizará para acceder a ella.

###### val : [NutSaveValue](/DOCUMENTATION_Ñ/FILES/NUTSAVEVALUE.md)

El valor que será guardado.
