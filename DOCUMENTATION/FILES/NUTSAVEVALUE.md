# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSAVEVALUE.md).

## NutSaveValue Class

Value designed to be save file-friendly.

Created automatically by [NutSaveProperty](/DOCUMENTATION/FILES/NUTSAVEPROPERTY.md).

### init method (value : any, value_type : type)

###### value : any

The value to save.

###### value_type : type

The type of the value to save.

Only accepts the following types: int, float, bool, str, [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md).

### Attributes

###### value : any

The value to save.

###### value_type : type

The type of the value to save.

Only accepts the following types: int, float, bool, str, [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md).

### Methods

#### parseVal() -> str

Converts the value to a string, which will be used in the save file.
