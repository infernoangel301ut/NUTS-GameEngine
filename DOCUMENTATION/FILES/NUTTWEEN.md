# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTTWEEN.md).

## NutTween Class

[This class extends the [NutTimer](/DOCUMENTATION/FILES/NUTTIMER.md) class, attributes and methods inherited from it will not be shown for simplicity]

Changes a property from ___its parent___ (very important) in a smooth way.

### init method (attribute_to_change : str, final_val : any_numeric_value, time : float, ease : (x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md).linear)

###### attribute_to_change : str

The name of the attribute you wanna change from the parent.

For example, if you wanna move the parent's x position, this value should be "position.x".

You are only able to change ints, floats, [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)s and [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)s.

###### final_Val : any_numeric_value

The ending value for the tween.

You are only able to change ints, floats, [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)s and [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)s.

###### time : float

The time it takes for the tween to end.

###### ease : (x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md).linear

The movement the tween will make. You can use a method from [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md) or make your own (as long as f(0) = 0 and f(1) = 1).

### Attributes

###### attribute_to_change : list[str]

The location of the attribute you wanna change from the parent.

###### initial_val : any_numeric_value | None

The starting value for the tween.

###### final_Val : any_numeric_value

The ending value for the tween.

###### ease : (x : float) -> any_numeric_value

The movement the tween will make. You can use a method from [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md) or make your own (as long as f(0) = 0 and f(1) = 1).

###### progress : float

How much of the way the tween has done (as a percentage).

###### cur_val : any_numeric_value | None

The current tween value, according to the tween progress.

### Methods

#### get_attr_val(parent : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)) -> any_numeric_value

Returns the value from the tweened attribute.

###### parent : [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md)

The parent (a.k.a. the tweened object).

#### update_progress() -> None

Updates the progress attribute.