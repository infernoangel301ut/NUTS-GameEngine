# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutKeyboard Class

Manages inputs from both mouse and keyboard.

Recommended way to use is by using the NutGame `keyboard` attribute.

### init method ()

### Attributes

###### curHeldKeys : list[NutKey]

Saves all keys that have been pressed but not yet released.

### Methods

#### getKeyState(key : NutKey) -> NutKeyState

Returns in which state the key is found in.

###### key : NutKey

The key to give information on.

#### getMouseState(action : NutMouseAction) -> NutKeyState

Returns in which state the mouse button is found in.

###### action : NutMouseAction

The mouse button to give information on.

#### getMousePosition() -> NutVector2

Gives the current mouse position.

#### update(curState : NutScene) -> None

Updates all the key related information and runs the input events for the current loaded scene in case there are.

###### curState : NutScene

The current loaded scene.
