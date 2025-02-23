# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

## NutKeyboard Class

Manages inputs from both mouse and keyboard.

Recommended way to use is by using the NutGame `keyboard` attribute.

### init method ()

### Attributes

###### curHeldKeys : list[[NutKey](/DOCUMENTATION/FILES/NUTKEY.md)]

Saves all keys that have been pressed but not yet released.

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

Updates all the key related information and runs the input events for the current loaded scene in case there are.

###### curState : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The current loaded scene.
