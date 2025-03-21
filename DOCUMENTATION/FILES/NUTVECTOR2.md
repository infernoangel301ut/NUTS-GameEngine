# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md).

## NutVector2 Class

Numeric value that contains 2 numbers. Used for two-dimensional values like position and size.

This object supports addition and subtraction.

### init method (x : float = 0, y : float = 0)

###### x : float = 0

The horizontal value.

###### y : float = 0

The vertical value.

### Attributes

###### x : float

The horizontal value.

###### y : float

The vertical value.

### Methods

#### toRaylibVector2() -> pyray.Vector2

Returns the current NutVector2 as a raylib Vector2 class.

#### [static] convert(x : pyray.Vector2 | list | tuple) -> NutVector2

Converts `x` to a NutVector2 object.

###### x : pyray.Vector2 | list | tuple

The object to convert.