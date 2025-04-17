# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSAVEVALUE.md).

## Clase NutSaveValue

Valor diseñado para ser apto para archivos de guardado.

Creado automaticamente por [NutSaveProperty](/DOCUMENTATION_Ñ/FILES/NUTSAVEPROPERTY.md).

### método init (value : any, value_type : type)

###### value : any

El valor a guardar.

###### value_type : type

El tipo de valor a guardar.

Solo acepta los siguientes tipos: int, float, bool, str, [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md).

### Atributos

###### value : any

El valor a guardar.

###### value_type : type

El tipo de valor a guardar.

Solo acepta los siguientes tipos: int, float, bool, str, [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md), [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md).

### Métodos

#### parseVal() -> str

Convierte el valor a un string, el cual será usado en el archivo de guardado.
