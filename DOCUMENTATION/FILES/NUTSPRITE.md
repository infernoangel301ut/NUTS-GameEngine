# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSPRITE.md).

## NutSprite Class

[This class extends the [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md) class, attributes and methods inherited from it will not be shown for simplicity]

A sprite that is displayed on the screen.

### init method (image_dir : str, position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2(), size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None)

###### image_dir : str

The sprite image directory.

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2()

The sprite position.

###### size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) | None = None

The sprite's size.

If None, the size will be set to the image size.

### Attributes

###### image_dir : str

The sprite image directory.

###### image : pyray.Texture

The actual image to be displayed.

###### display_image : pyray.Texture

The `image` attribute, but modified to match the rest of the attributes.

###### size : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The displayed image size.

###### angle : float

The sprite rotation.

###### color : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

The sprite color modification, `NutColor(255, 255, 255)` by default.

###### animation : [NutAnimationController](/DOCUMENTATION/FILES/NUTANIMATIONCONTROLLER.md)

Manages the sprite animations, in case it is animated.

###### scale : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The relative size multiplier. Original size is NutVector2(1, 1).

###### flipX : bool

Whether to flip the sprite horitzontally or not.

###### flipY : bool

Whether to flip the sprite vertically or not.

### Methods

#### updateDisplay() -> None

Updates the sprite to add the changed properties.
