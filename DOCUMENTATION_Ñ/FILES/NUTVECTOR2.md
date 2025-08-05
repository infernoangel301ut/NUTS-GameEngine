# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTVECTOR2.md).

## Clase NutVector2

Valor numérico que contiene dos números. Usado para valores bidimensionales como posición y tamaño.

Este objeto permite sumas y restas.

### método init (x : float = 0, y : float = 0)

###### x : float = 0

El valor horizontal.

###### y : float = 0

El valor vertical.

### Atributos

###### x : float

El valor horizontal.

###### y : float

El valor vertical.

### Métodos

#### toRaylibVector2() -> pyray.Vector2

Regresa el NutVector2 actual en forma de clase Vector2 de raylib.

#### [estático] convert(x : pyray.Vector2 | list | tuple) -> NutVector2

Convierte `x` a un objeto NutVector2.

###### x : pyray.Vector2 | list | tuple

El objeto a convertir.