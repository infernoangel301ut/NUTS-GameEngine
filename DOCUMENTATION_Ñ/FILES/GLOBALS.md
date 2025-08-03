# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/GLOBALS.md).

## Funciones y variables globales

### Funciones

#### find_xml_elementS_by_name_atr(xml_root:XmlTree.Element, name:str) -> list[XmlTree.Element] | None

Función diseñada para obtener el frame de una animación XML para el sistema de Sparrow.

Obtiene todos los elementos de un archivo XML con el atributo proveído `name`.

###### xml_root : XmlTree.Element

El elemento principal del XML, el cual contiene todas las animaciones.

###### name : str

El nombre del frame de la animación, sin los números, eso es para los frames individuales.

### Variables

#### version : str

La versión actual de NUTS.

#### view_width : int

El ancho del viewport. No confundir con el ancho de la ventana.

#### view_height : int

El alto del viewport. No confundir con el alto de la ventana.

#### nuts_default_logger : [NutLogger](/DOCUMENTATION_Ñ/FILES/NUTLOGGER.md) = NutLogger("NUTS")

El logger que NUTS usa por predeterminado.

#### any_numeric_value : type = int | float | [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)

Tipo usado para type-checking cuando se intenta usar cualquier valor numérico.
