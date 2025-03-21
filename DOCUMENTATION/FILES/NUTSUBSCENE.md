# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSUBSCENE.md).

## NutSubScene Class

[This class extends the [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md) class, attributes and methods inherited from it will not be shown for simplicity]

A scene inside of another scene, still does anything a normal scene does.

To make your own subscene, extend this class.

### init method (parentScene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md), transparentBG : bool = True)

###### parentScene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The scene this subscene is dependent of (in most cases, this parameter's value will be `self`).

###### transparentBG : bool = True

Whether to automatically make the subscene's background transparent or not. Useful so you can still see the parent scene.

### Attributes

###### parentScene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The scene this subscene is dependent of.

###### activated : bool

Whether this subscene is being displayed or not.

###### awaitingLoad : bool

Whether the `onLoaded` event is expected to be ran.

###### awaitingUnload : bool

Whether the `onUnloaded` event is expected to be ran.

### Methods

#### toggleActivate(value : bool | None = None) -> None

Used to display or hide this subscene (and to change the `activated` attribute).

###### value : bool | None = None

Whether to activate the subscene (True) or deactivate it (False).

If None, it will switch to the opposite of the current value.