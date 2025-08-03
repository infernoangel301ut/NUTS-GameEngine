# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTGAME.md).

## NutGame Class

The most important class, literally runs the whole thing.

### init method (winWidth : float, winHeight : float, title : str, fps : int = 60)

###### winWidth : float

The game window's width.

###### winHeight : float

The game window's height.

###### title : str

The game window's title.

###### fps : int = 60

The fps the game will run at.

### Attributes

###### winWidth : float

The game window's width.

###### winHeight : float

The game window's height.

###### viewWidth : float

The viewport's width.

###### viewHeight : float

The viewport's height.

###### winPos : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

The current position of the window in the desktop.

###### title : str

The game window's title.

###### fps : int

The fps the game will run at.

###### curScene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The scene currently being displayed on screen.

###### keyboard : [NutKeyboard](/DOCUMENTATION/FILES/NUTKEYBOARD.md)

The main input manager, checks for keyboard and mouse inputs.

###### audioManager : [NutAudioManager](/DOCUMENTATION/FILES/NUTAUDIOMANAGER.md)

The main audio controller, plays and saves sound and music.

###### saveFiles : dict[str, [NutSaveFile](/DOCUMENTATION/FILES/NUTSAVEFILE.md)]

The save file storage, all save information is in this dictionary.

###### awaitingLoad : bool

Checks whether it should run the scene's onLoaded() event.

It is recommended that you do not change it by yourself.

###### awaitingAudioClear : bool

Whether it is expected to clear the audio next frame or not.

It is automatically set by changing the scene, and has to do with its clearAudioOnUnload attribute.

###### gameShouldEnd : bool

Whether the game should close on the next frame or not.

Alternatively, you can run the close() method which will automatically set this attribute to True.

###### viewportCamera : pyray.Camera2D

The raylib camera containing the view relative to the window size.

[EXPLANATION!!! The window is what you're seeing on your desktop, while the viewport, is what the window itself is containing. They can both have different sizes.]

[The viewport maintains the initial size while adapting itself to the window, thus making resizing the window less glitchy.]

###### resizable : bool

Whether the window can be resized or not. Use the `updateWindowProperties` method to apply.

###### fullscreen : bool

Whether the game should be on fullscreen or windowed. Use the `updateWindowProperties` method to apply.

###### was_fullscreen : bool

Whether the game was previously on fullscreen or windowed, used to avoid glitches.

###### shouldRestoreAfterFullscreen : bool

Whether the game should apply some changes after fullscreen, used to avoid glitches.

###### borderless : bool

Whether the window should have borders or not. Use the `updateWindowProperties` method to apply.

###### was_borderless : bool

Whether the game was previously on borderless or not, used to avoid glitches.

###### allowsTransparency : bool

Whether the game allows for actual window transparency or not. Use the `updateWindowProperties` method to apply.

###### viewBorderColor : [NutColor](/DOCUMENTATION/FILES/NUTCOLOR.md)

The color used for the viewport obrders.

### Methods

#### saveFileExists(file_dir : str, file_name : str) -> bool

Whether the specified save file exists or not. Mostly used for either creating or loading a save file.

###### file_dir : str

The folder on which the save file should be located in.

###### file_name : str

The name of the file to check on. Do not add the file extension.

#### addSaveFile(save : [NutSaveFile](/DOCUMENTATION/FILES/NUTSAVEFILE.md)) -> None

Adds the save file to the saveFiles attribute, assigning its key to the save file's file_name attribute.

###### save : [NutSaveFile](/DOCUMENTATION/FILES/NUTSAVEFILE.md)

The save file to add in.

#### loadScene(scene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)) -> None

Loads the specified scene and unloads the previous one.

###### scene : [NutScene](/DOCUMENTATION/FILES/NUTSCENE.md)

The scene to load in.

#### reloadScene() -> None

Runs the loadScene method using the current scene, reloading it.

#### close() -> None

Closes the game window.

#### updateWindowSize() -> None

Updates the window size according to the `winWidth` and `winHeight` attributes.

#### updateWindowPos() -> None

Updates the window position according to the `winPos` attribute.

#### updateWindowProperties() -> None

Updates the window according to the attributes defining it.

#### setFPS(val : int) -> None

Changes the FPS at which the game runs.

###### val : int

The FPS to run the game at.

#### start() -> None

Starts running the game and everything else.
