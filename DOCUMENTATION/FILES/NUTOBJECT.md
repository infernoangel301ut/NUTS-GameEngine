# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutObject Class

The base on-screen object, everything that gets rendered comes from this class.

### init method (position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2())

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2()

The object position in the window (still won't be visible though lol, because this is NOTHING).

### Attributes

###### children : dict[str, NutObject]

The other NutObjects that depend on this current one.

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The object position in the window.

### Methods

#### render(globalPos : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), parent : NutObject | None) -> None

Renders this object on the screen.

(This method is automatically ran by the NutGame class, there's no need to run it yourself).

###### globalPos : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The parent's position, to adjust this current object's position.

###### parent : NutObject | None

This NutObject's parent, or None if it has no parent (awesome fatherless joke).

Used to get properties from the parent.

#### centerX() -> None

Centers the NutObject on the X axis.

#### centerY() -> None

Centers the NutObject on the Y axis.
