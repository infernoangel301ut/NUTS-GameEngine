# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

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
