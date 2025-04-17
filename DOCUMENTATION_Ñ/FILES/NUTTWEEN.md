# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTTWEEN.md).

## Clase NutTween

[Esta clase extiende a la clase [NutTimer](/DOCUMENTATION_Ñ/FILES/NUTTIMER.md), aquellos atributos y mètodos obtenidos de el no se mostrarán por simplicidad]

Cambia una propiedad de ___su parent___ (muy importante) de una manera suave.

### método init (attribute_to_change : str, final_val : any_numeric_value, time : float, ease : (s : any_numeric_value, f : any_numeric_value, d : float, x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION_Ñ/FILES/NUTTWEENEASE.md).linear)

###### attribute_to_change : str

El nombre del atributo que quieres cambiar del parent.

Por ejemplo, si quieres mover la posición x del parent, este valor debería ser "position.x".

Solo puedes cambiar ints, floats, [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)s y [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)s.

###### final_Val : any_numeric_value

El valor final para el tween.

Solo puedes cambiar ints, floats, [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)s y [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)s.

###### time : float

El tiempo que le toma al tween para terminar.

###### ease : (x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION_Ñ/FILES/NUTTWEENEASE.md).linear

El movimiento que hará el tween. Puedes usar un método de [NutTweenEase](/DOCUMENTATION_Ñ/FILES/NUTTWEENEASE.md) o hacer el tuyo propio (siempre  y cuando f(0) = 0 y f(1) = 1).

### Atributos

###### attribute_to_change : list[str]

La localización del atributo que quieres cambiar del parent.

###### initial_val : any_numeric_value | None

El valor inicial del tween.

###### final_Val : any_numeric_value

El valor final del tween.

###### ease : (x : float) -> any_numeric_value

El movimiento que hará el tween. Puedes usar un método de [NutTweenEase](/DOCUMENTATION_Ñ/FILES/NUTTWEENEASE.md) o hacer el tuyo propio (siempre  y cuando f(0) = 0 y f(1) = 1).

###### progress : float

Cuanto progreso ha hecho el tween (en forma de porcentage).

###### cur_val : any_numeric_value | None

El valor actual del tween, según el progreso del tween. Es equivalente a `ease(progress)`.

### Métodos

#### get_attr_val(parent : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)) -> any_numeric_value

Regresa el valor del atributo del tween.

###### parent : [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md)

El parent (es decir, el objeto del tween).

#### update_progress() -> None

Actualiza el atributo progress.
