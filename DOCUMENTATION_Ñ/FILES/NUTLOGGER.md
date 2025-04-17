# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTLOGGER.md).

## Clase NutLogger

Systema de logging personalizado (para usar un sistema más elegante que print XD).

### método init (log_name : str)

###### log_name : str

El nombre que aparece en los logs creados por este logger.

### Atributos

###### log_name : str

El nombre que aparece en los logs creados por este logger.

### Métodos

#### log(message : Any, log_type : [NutLogType](/DOCUMENTATION_Ñ/FILES/NUTLOGTYPE.md) = NutLogType.INFO) -> None

Loggea `message` en la consola con el tipo `log_type`. (Sistema de printing más elegante XD).

###### message : Any

El mensaje a loggear.

###### log_type : [NutLogType](/DOCUMENTATION_Ñ/FILES/NUTLOGTYPE.md) = NutLogType.INFO

El tipo de mensaje que será loggeado.
