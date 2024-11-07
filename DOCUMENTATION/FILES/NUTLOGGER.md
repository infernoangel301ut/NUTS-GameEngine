# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutLogger Class

Custom logging system (to use a fancier system than print lol).

### init method (log_name : str)

###### log_name : str

The name that appears in the logs created by this logger.

### Attributes

###### log_name : str

The name that appears in the logs created by this logger.

### Methods

#### log(message : Any, log_type : [NutLogType](/DOCUMENTATION/FILES/NUTLOGTYPE.md) = NutLogType.INFO) -> None

Logs `message` in the console with the `log_type` type. (Fancier printing system lol).

###### message : Any

The message to log.

###### log_type : [NutLogType](/DOCUMENTATION/FILES/NUTLOGTYPE.md) = NutLogType.INFO

The type of the message that will be logged.
