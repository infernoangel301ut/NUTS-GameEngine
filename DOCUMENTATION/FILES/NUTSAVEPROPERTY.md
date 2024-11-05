# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutSaveProperty Class

Property that is stored in a save file.

### init method(name : str, val_type : type, val : any)

###### name : str

The name of the property. Will be used to access it.

###### val_type : type

The type of the value you want to save. Only accepts the following: int, float, bool, str, NutVector2, NutColor.

###### val : any

The value you want to save.

### Attributes

###### name : str

The name of the property. Will be used to access it.

###### val : NutSaveValue

The value that will be saved.
