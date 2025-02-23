# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

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
