# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutGame Class

The most important class, literally runs the whole thing.

### init method(winWidth : float, winHeight : float, title : str, fps : int = 60)

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

Checks whether it should run the states onLoaded() event.

It is recommended that you do not change it by yourself.

###### gameShouldEnd : bool

Whether the game should close on the next frame or not.

Alternatively, you can run the close() method which will automatically set this attribute to True.

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

#### start() -> None

Starts running the game and everything else.
