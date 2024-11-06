# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutFrame Class

Designed to get the position of an animation frame for an animated sprite.

### init method (img_position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), img_size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None, size_offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None)

###### img_position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame position in the original image.

###### img_size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame size range in the original image.

###### offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None

The position adjustment when being displayed on the screen.

If None, its value will be set to NutVector2(0, 0).

###### size_offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None

The size adjustment when being displayed on the screen.

If None, its value will be set to img_size.

### Attributes

###### img_position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame position in the original image.

###### img_size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame size range in the original image.

###### offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The position adjustment when being displayed on the screen.

###### size_offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The size adjustment when being displayed on the screen.
