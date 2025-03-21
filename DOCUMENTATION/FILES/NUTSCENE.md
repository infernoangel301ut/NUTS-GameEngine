# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md).

## NutScene Class

[This class extends the [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md) class, attributes and methods inherited from it will not be shown for simplicity]

A scene to be displayed by the game, contains most of the main stuff for the game to run.

To make your own scene, extend this class.

### Attributes

###### bgColor : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

This scene's background color.

###### keepAudioOnUnload : bool

Whether all audio should be cleared on loading another scene. (True by default)

###### update_paused : bool

Whether the onUpdate event should be ran or not. (False by default)

###### drawing_paused : bool

Whether animated sprites in this scene should be paused or not. (False by default)

### Methods

#### onLoaded() -> None

Event that runs once the scene has been loaded (and then not anymore lol).

#### onUpdated() -> None

Event that is running constantly.

#### onUpdatedPost() -> None

Event that runs after everything on the scene has been updated, and therefore also runs constantly.

#### OnUnloaded() -> None

Event that runs once another scene has been loaded (so this one is replaced).

#### OnKeyInput(key : [NutKey](/DOCUMENTATION/FILES/NUTKEY.md), state : [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md)) -> None

Event that runs once an input has been done by the keyboard.

###### key : [NutKey](/DOCUMENTATION/FILES/NUTKEY.md)

The key related to the input.

###### state : [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md)

The press state the key was found in.

#### onMouseInput(action : [NutMouseAction](/DOCUMENTATION/FILES/NUTMOUSEACTION.md), state : [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md), position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)) -> None

Event that runs once an input has been done by the mouse.

###### action : [NutMouseAction](/DOCUMENTATION/FILES/NUTMOUSEACTION.md)

Which mouse button was pressed.

###### state : [NutKeyState](/DOCUMENTATION/FILES/NUTKEYSTATE.md)

The press state the mouse button was found it.

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The mouse position at the time of the input.
