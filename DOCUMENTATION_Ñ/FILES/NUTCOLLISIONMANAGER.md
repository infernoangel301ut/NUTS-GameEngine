# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutCollisionManager

Diseñado para cosas relacionadas a colisiones.

### Metodos

#### [estático] getCollisionRect(obj : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)) -> pyray.Rectangle

Obtiene el rectangulo de raylib de este objeto por razones de colisión.

###### obj : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

El objeto del cual obtener el rectangulo.

#### [estático] checkCollision(objA : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), objB : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)) -> bool

Si objA y objB están colisionando o no.

###### objA : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

Primer objeto.

###### objB : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

Segundo objeto.

#### [estático] checkSideCollisions(colliding : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), collision : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)) -> [NutCollisionDirection](/DOCUMENTATION_Ñ/FILES/NUTCOLLISIONDIRECTION.md)

Regresa un objeto que especifica por que lados está colisionando el objeto.

###### colliding : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

El objeto colisionante.

###### collision : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

El objeto en el que se esta colisionando.