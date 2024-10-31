# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutSprite Class

[This class extends the NutObject class, attributes and methods inherited from it will not be shown for simplicity]

A sprite that is displayed on the screen.

### init method (image_dir : str, position : NutVector2 = NutVector2(), size : NutVector2 | None = None)

###### image_dir : str

The sprite image directory.

###### position : NutVector2() = NutVector2()

The sprite position.

###### size : NutVector2() | None = None

The sprite's size.

If None, the size will be set to the image size.

### Attributes

###### image_dir : str

The sprite image directory.

###### image : pyray.Texture

The actual image to be displayed.

###### display_image : pyray.Texture

The `image` attribute, but modified to match the rest of the attributes.

###### size : NutVector2

The displayed image size.

###### angle : float

The sprite rotation.

###### color : NutColor

The sprite color modification, `NutColor(255, 255, 255)` by default.

###### animation : NutAnimationController

Manages the sprite animations, in case it is animated.

###### scale : NutVector2

The relative size multiplier. Original size is NutVector2(1, 1).

###### flipX : bool

Whether to flip the sprite horitzontally or not.

###### flipY : bool

Whether to flip the sprite vertically or not.

### Methods

#### updateDisplay() -> None

Updates the sprite to add the changed properties.
