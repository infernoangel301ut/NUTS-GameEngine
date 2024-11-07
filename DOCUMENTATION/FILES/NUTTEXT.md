# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutText Class

[This class extends the [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md) class, attributes and methods inherited from it will not be shown for simplicity]

The text object (displays text, what a surprise).

### init method (position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), text : str, size : int, color : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md) = NutColor(255, 255, 255))

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The text position.

###### text : str

The string of text to be shown in the object.

###### size : int

The text size (not to be confused with the object size).

###### color : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md) = NutColor(255, 255, 255)

The text color.

### Attributes

###### text : str

The string of text to be shown in the object.

###### size : int

The text size (not to be confused with the object size).

###### font : str | None

The directory for the font being used.

###### raylib_font : pyray.Font | None

The raylib font object, used for rendering.

###### color : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

The text color.

###### spacing : int

The space between each letter.

###### angle : float

The text rotation.

### Methods

#### loadFont(font_dir : str) -> None

Loads a font to be used for the text.

###### font_dir : str

The font directory.

#### setDefaultFont() -> None

Removes the current font and sets the default one instead.
