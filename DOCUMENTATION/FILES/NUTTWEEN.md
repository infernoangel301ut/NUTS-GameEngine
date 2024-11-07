# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutTween Class

[This class extends the [NutTimer](/DOCUMENTATION/FILES/NUTTIMER.md) class, attributes and methods inherited from it will not be shown for simplicity]

Changes a property from ___its parent___ (very important) in a smooth way.

### init method (attribute_to_change : str, initial_val : any_numeric_value, final_val : any_numeric_value, time : float, ease : (s : any_numeric_value, f : any_numeric_value, d : float, x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md).linear)

###### attribute_to_change : str

The name of the attribute you wanna change from the parent.

###### initial_val : any_numeric_value

The starting value for the tween.

###### final_Val : any_numeric_value

The ending value for the tween.

###### time : float

The time it takes for the tween to end.

###### ease : (s : any_numeric_value, f : any_numeric_value, d : float, x : float) -> any_numeric_value = [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md).linear

The ease of the tween, a.k.a. how it will move. You can use a method from [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md) or make your own.

### Attributes

###### attribute_to_change : str

The name of the attribute you wanna change from the parent.

###### initial_val : any_numeric_value

The starting value for the tween.

###### final_Val : any_numeric_value

The ending value for the tween.

###### ease : (s : any_numeric_value, f : any_numeric_value, d : float, x : float) -> any_numeric_value

The ease of the tween, a.k.a. how it will move. You can use a method from [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md) or make your own.
