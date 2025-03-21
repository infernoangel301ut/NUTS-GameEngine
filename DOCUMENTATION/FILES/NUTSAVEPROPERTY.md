# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSAVEPROPERTY.md).

## NutSaveProperty Class

Property that is stored in a save file.

### init method(name : str, val_type : type, val : any)

###### name : str

The name of the property. Will be used to access it.

###### val_type : type

The type of the value you want to save. Only accepts the following: int, float, bool, str, [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md).

###### val : any

The value you want to save.

### Attributes

###### name : str

The name of the property. Will be used to access it.

###### val : [NutSaveValue](/DOCUMENTATION/FILES/NUTSAVEVALUE.md)

The value that will be saved.
