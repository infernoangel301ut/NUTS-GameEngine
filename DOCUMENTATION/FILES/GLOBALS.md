# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

## Global functions and variables

### Functions

#### extend_zeros(num:str, amount:int) -> str

Function designed to get the frame of an XML animation for the sparrow system.

Gets the number, and adds zeros to the left until its length is the same as amount.

##### Parameters

###### num : str

The number value as a string.

###### amount : int

The amount of digits for the result to be.

#### find_xml_element_by_name_atr(xml_root:XmlTree.Element, name:str) -> XmlTree.Element | None

Function designed to get the frame of an XML animation for the sparrow system.

Gets the XML file element by its name attribute.

##### Parameters

###### xml_root : XmlTree.Element

The XML's root element, containing all of the animations.

###### name : str

The animation frame name, with the numbers.

### Variables

#### nuts_default_logger : [NutLogger](/DOCUMENTATION/FILES/NUTLOGGER.md) = NutLogger("NUTS")

The logger that NUTS uses by default.

#### any_numeric_value : type = int | float | [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

Type used for type checking when trying to use any numeric value.
