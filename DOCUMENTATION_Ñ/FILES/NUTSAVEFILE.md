# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSAVEFILE.md).

## Clase NutSaveFile

Archivo que hace de archivo de guardado.

### método init (file_dir : str, file_name : str)

###### file_dir : str

El directorio en el que se almacenará el archivo de guardado.

###### file_name : str

El nombre del archivo en sí (la extensión se añadirá al crear el archivo).

### Atributos

###### file_dir : str

El directorio en el que se almacenará el archivo de guardado.

###### file_name : str

El nombre del archivo en sí (la extensión se añadirá al crear el archivo).

###### properties : dict[str, [NutSaveProperty](/DOCUMENTATION_Ñ/FILES/NUTSAVEPROPERTY.md)]

Las propiedades almacenadas en el archivo de guardado.

### Métodos

#### setProperty(property : [NutSaveProperty](/DOCUMENTATION_Ñ/FILES/NUTSAVEPROPERTY.md)) -> None

Almacena o modifica una propiedad en el archivo de guardado.

###### property : [NutSaveProperty](/DOCUMENTATION_Ñ/FILES/NUTSAVEPROPERTY.md)

La propiedad que almacenar o modificar.

#### parsePropertiesAsStr() -> str | None

Regresa los contenidos del archivo de guardado como un string basándose en las propiedades.

#### saveFile() -> None

Guarda el archivo en la carpeta especificada con el nombre especificado con la extensión de archivo ".nutsave".

#### loadFile() -> None

Carga el archivo de la carpeta especificada con el nombre especificado con la extensión de archivo ".nutsave".
