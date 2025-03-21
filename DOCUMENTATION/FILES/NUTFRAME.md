# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTFRAME.md).

## NutFrame Class

Designed to get the position of an animation frame for an animated sprite.

### init method (img_position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), img_size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None, size_offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None, flipX : bool = False, flipY : bool = False, rotated : bool = False)

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

###### flipX : bool = False

Whether to invert this specific frame on the horizontal axis or not.

###### flipY : bool = False

Whether to invert this specific frame on the vertical axis or not.

###### rotated : bool = False

Whether to rotate this specific frame 90 degrees counterclockwise (a.k.a. -90 degrees) or not.

### Attributes

###### img_position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame position in the original image.

###### img_size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The frame size range in the original image.

###### offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The position adjustment when being displayed on the screen.

###### size_offset : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The size adjustment when being displayed on the screen.

###### flipX : bool

Whether to invert this specific frame on the horizontal axis or not.

###### flipY : bool

Whether to invert this specific frame on the vertical axis or not.

###### rotated : bool

Whether to rotate this specific frame 90 degrees counterclockwise (a.k.a. -90 degrees) or not.