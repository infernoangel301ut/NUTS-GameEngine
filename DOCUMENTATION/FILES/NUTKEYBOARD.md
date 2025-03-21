# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTKEYBOARD.md).

## NutKeyboard Class

Manages inputs from both mouse and keyboard.

Recommended way to use is by using the [NutGame](/DOCUMENTATION/FILES/NUTGAME.md) `keyboard` attribute.

### Attributes

###### curHeldKeys : list[[NutKey](/DOCUMENTATION/FILES/NUTKEY.md)]

Stores all keys that are being held down.

### Methods

#### getKeyState(key : [NutKey](/DOCUMENTATION/FILES/NUTKEY.md)) -> [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md)

Returns in which state the key is found in.

###### key : [NutKey](/DOCUMENTATION/FILES/NUTKEY.md)

The key to give information on.

#### getMouseState(action : [NutMouseAction](/DOCUMENTATION/FILES/NUTMOUSEACTION.md)) -> [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md)

Returns in which state the mouse button is found in.

###### action : [NutMouseAction](/DOCUMENTATION/FILES/NUTMOUSEACTION.md)

The mouse button to give information on.

#### getMousePosition() -> [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

Gives the current mouse position.

#### update(curState : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)) -> None

Updates all the key related information and runs the input events for the current loaded scene and its subscenes, in case there are any inputs.

###### curState : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The current loaded scene.
