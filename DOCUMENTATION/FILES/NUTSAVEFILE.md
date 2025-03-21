# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md).

## NutSaveFile Class

File that acts as a save file.

### init method(file_dir : str, file_name : str)

###### file_dir : str

The folder on which the save file will be stored.

###### file_name : str

The name of the actual file (extension will be added on creating the file).

### Attributes

###### file_dir : str

The folder on which the save file will be stored.

###### file_name : str

The name of the actual file (extension will be added on creating the file).

###### properties : dict[str, [NutSaveProperty](/DOCUMENTATION/FILES/NUTSAVEPROPERTY.md)]

The properties stored in the save file.

### Methods

#### setProperty(property : [NutSaveProperty](/DOCUMENTATION/FILES/NUTSAVEPROPERTY.md)) -> None

Stores a property on the save file.

###### property : [NutSaveProperty](/DOCUMENTATION/FILES/NUTSAVEPROPERTY.md)

The property to save.

#### parsePropertiesAsStr() -> str | None

Returns the contents of the save file as a string based on all the properties.

#### saveFile() -> None

Saves the file on the specified folder with the specified name with the file extension ".nutsave".

#### loadFile() -> None

Loads the save file located on the specified folder with the specified name with the file extension ".nutsave".
