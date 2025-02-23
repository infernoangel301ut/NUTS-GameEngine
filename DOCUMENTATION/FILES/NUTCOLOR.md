# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

## NutColor Class

Value type designed for colors.

### init method (r : int, g : int, b : int, a : int = 255)

###### r : int

The red value for this color. [0, 255]

###### g : int

The green value for this color. [0, 255]

###### b : int

The blue value for this color. [0, 255]

###### a : int = 255

The alpha (transparency) value for this color. [0, 255]

### Attributes

###### r : int

The red value for this color. [0, 255]

###### g : int

The green value for this color. [0, 255]

###### b : int

The blue value for this color. [0, 255]

###### a : int

The alpha (transparency) value for this color. [0, 255]

### Methods

#### toRaylibColor() -> pyray.Color

Returns the raylib Color class version of this NutColor value.

#### [static] fromFloatRGB(r : float, g : float, b : float, a : float = 1) -> NutColor

Allows you to get the NutColor value from values between 0 and 1 instead of 0 and 255.

###### r : float

The red value for this color. [0, 1]

###### g : float

The green value for this color. [0, 1]

###### b : float

The blue value for this color. [0, 1]

###### a : float = 1

The alpha (transparency) value for this color. [0, 1]

#### [static] fromHex(hexadecimal : str) -> NutColor

Allows you to get the NutColor value from a hexadecimal code.

(String must have a length of 6 or 8 characters. In case of there being 8 characters, the last 2 will be considered as the alpha value.)

(Examples:

"000000" -> r = 0; g = 0; b = 0; a = 255;

"00000000" -> r = 0; g = 0; b = 0; a = 0;

)

###### hexadecimal : str

The hexadecimal code for this color.
