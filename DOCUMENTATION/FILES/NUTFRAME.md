# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutFrame Class

Designed to get the position of an animation frame for an animated sprite.

### init method (img_position : NutVector2, img_size : NutVector2, offset : NutVector2 | None = None, size_offset : NutVector2 | None = None)

###### img_position : NutVector2

The frame position in the original image.

###### img_size : NutVector2

The frame size range in the original image.

###### offset : NutVector2 | None = None

The position adjustment when being displayed on the screen.

If None, its value will be set to NutVector2(0, 0).

###### size_offset : NutVector2 | None = None

The size adjustment when being displayed on the screen.

If None, its value will be set to img_size.

### Attributes

###### img_position : NutVector2

The frame position in the original image.

###### img_size : NutVector2

The frame size range in the original image.

###### offset : NutVector2

The position adjustment when being displayed on the screen.

###### size_offset : NutVector2

The size adjustment when being displayed on the screen.
