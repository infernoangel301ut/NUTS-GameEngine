# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTVECTOR2.md).

## Clase NutColor

Tipo de valor diseñado para colores.

### método init (r : int, g : int, b : int, a : int = 255)

###### r : int

El valor rojo para este color. [0, 255]

###### g : int

El valor verde para este color. [0, 255]

###### b : int

El valor azul para este color. [0, 255]

###### a : int = 255

El valor alfa (transparencia) para este color. [0, 255]

### Atributos

###### r : int

El valor rojo para este color. [0, 255]

###### g : int

El valor verde para este color. [0, 255]

###### b : int

El valor azul para este color. [0, 255]

###### a : int

El valor alfa (transparencia) para este color. [0, 255]

### Métodos

#### toRaylibColor() -> pyray.Color

Regresa la versión de raylib de este color.

#### [estático] fromFloatRGB(r : float, g : float, b : float, a : float = 1) -> NutColor

Te permite obtener el valor NutColor usando valores entre 0 y 1 en vez de entre 0 y 255.

###### r : float

El valor rojo para este color. [0, 1]

###### g : float

El valor verde para este color. [0, 1]

###### b : float

El valor azul para este color. [0, 1]

###### a : float = 1

El valor alfa (transparencia) para este color. [0, 1]

#### [estático] fromHex(hexadecimal : str) -> NutColor

Te permite obtener el valor NutColor usando un código hexadecimal.

(El string debe tener una longitud de 6 u 8 caracteres. En caso de haber 8 caracteres, los últimos 2 serán considerados como el valor alfa.)

(Ejemplos:

"000000" -> r = 0; g = 0; b = 0; a = 255;

"00000000" -> r = 0; g = 0; b = 0; a = 0;

)

###### hexadecimal : str

El código hexadecimal para este color.

#### [estático] convert(x : pyray.Color | list | tuple | int) -> NutColor

Convierte `x` en un objeto NutColor.

###### x : pyray.Vector2 | list | tuple

El objeto a convertir.