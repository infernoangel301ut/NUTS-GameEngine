# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutScene Class

[This class extends the NutObject class, attributes and methods inherited from it will not be shown for simplicity]

A scene to be displayed by the game, contains most of the main stuff for the game to run.

To make your own scene, you usually extend this class.

### Attributes

###### bgColor : NutColor

This scene's background color.

### Methods

#### onLoaded() -> None

Event that runs once the scene has been loaded (and then not anymore lol).

#### onUpdated() -> None

Event that is running constantly.

#### onUpdatedPost() -> None

Event that runs after everything on the scene has been updated, and therefore also runs constantly.

#### OnUnloaded() -> None

Event that runs once another scene has been loaded (so this one is replaced).

#### OnKeyInput(key : NutKey, state : NutKeyState) -> None

Event that runs once an input has been done by the keyboard.

###### key : NutKey

The key related to the input.

###### state : NutKeyState

The press state the key was found in.

#### onMouseInput(action : NutMouseAction, state : NutKeyState, position : NutVector2) -> None

Event that runs once an input has been done by the mouse.

###### action : NutMouseAction

Which mouse button was pressed.

###### state : NutKeyState

The press state the mouse button was found it.

###### position : NutVector2

The mouse position at the time of the input.
