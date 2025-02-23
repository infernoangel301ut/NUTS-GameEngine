# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Funciones y variables globales

### Funciones

#### extend_zeros(num:str, amount:int) -> str

Función diseñada para obtener el frame de una animación XML para el sistema de sparrow.

Obtiene el número, y añade ceros a la izquierda hasta que su longitud sea igual a la cantidad.

##### Parámetros

###### num : str

El valor del número en forma de string.

###### amount : int

La cantidad de dígitos que debe tener el resultado.

#### find_xml_element_by_name_atr(xml_root:XmlTree.Element, name:str) -> XmlTree.Element | None

Función diseñada para obtener el frame de una animación XML para el sistema de sparrow.

Obtiene el elemento de un archivo XML por su attributo "name".

##### Parámetros

###### xml_root : XmlTree.Element

El elemento principal del XML, el cual contiene todas las animaciones.

###### name : str

El nombre del frame de la animación, con los números al final incluidos.

### Variables

#### nuts_default_logger : [NutLogger](/DOCUMENTATION_Ñ/FILES/NUTLOGGER.md) = NutLogger("NUTS")

El logger que NUTS usa por predeterminado.

#### any_numeric_value : type = int | float | [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)

Tipo usado para type checking cuando se intenta usar cualquier valor numerico.
