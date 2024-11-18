# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutCollisionManager Class

Designed to do collision related stuff.

### Methods

#### [static] getCollisionRect(obj : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)) -> pyray.Rectangle

Gets the raylib Rectangle from this object for collision reasons.

###### obj : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

The object to get the rectangle from.

#### [static] checkCollision(objA : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md), objB : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)) -> bool

Whether objA and objA are colliding or not.

###### objA : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

First object.

###### objB : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

Second object.

#### [static] checkSideCollisions(colliding : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md), collision : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)) -> [NutCollisionDirection](/DOCUMENTATION/FILES/NUTCOLLISIONDIRECTION.md)

Returns an object that specifies from which sides the colliding object is colliding.

###### colliding : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

The colliding object.

###### collision : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

The object being collided on.