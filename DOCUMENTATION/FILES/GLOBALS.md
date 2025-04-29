# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/GLOBALS.md).

## Global functions and variables

### Functions

#### find_xml_elements_by_name_atr(xml_root:XmlTree.Element, name:str) -> list[XmlTree.Element] | None

Function designed to get the frames of an XML animation for the sparrow system.

Gets all of the XML elements using the name attribute provided.

(Additionally, it places them in order).

###### xml_root : XmlTree.Element

The XML's root element, containing all of the animations.

###### name : str

The animation name, without the numbers, that is for the individual frames.

### Variables

#### version : str

NUTS' current version.

#### is_early_version : bool

Whether the NUTS version being used is really early or not. Only used to display a message on the console.

#### view_width : int

The viewport width. Not to be confused with the window width.

#### view_height : int

The viewport height. Not to be confused with the window height.

#### nuts_default_logger : [NutLogger](/DOCUMENTATION/FILES/NUTLOGGER.md) = NutLogger("NUTS")

The logger that NUTS uses by default.

#### any_numeric_value : type = int | float | [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

Type used for type checking when trying to use any numeric value.
