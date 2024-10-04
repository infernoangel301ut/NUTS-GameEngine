# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## Classes

### NutGame(winWidth:float, winHeight:float, title:str, fps:int = 60)
##### winWidth : float
The width of the window in pixels. In case of decimals being added, it will be rounded towards the lowest number.

##### winHeight : float
The height of the window in pixels. In case of decimals being added, it will be rounded towards the lowest number.

##### title : str
The title of the window.

##### fps : int (optional)
The amount of frames shown every second. Its value is 60 by default.

#### **Attributes**
##### winWidth : float
The width of the window in pixels. In case of decimals being added, it will be rounded towards the lowest number. Changing this won't cause any difference.

##### winHeight : float
The height of the window in pixels. In case of decimals being added, it will be rounded towards the lowest number. Changing this won't cause any difference.

##### title : str
The title of the window. Changing this won't cause any difference.

##### fps : int
The amount of frames shown every second. Its value is 60 by default. Changing this won't cause any difference.

##### curScene : NutScene
The scene being currently displayed. Change using `loadScene()` to avoid bugs.

##### keyboard : NutKeyboard
The keyboard input manager. Changing this might cause bugs, make sure to use the `onKeyInput()` event or the `getKeyState()` function in a `NutScene` class instead.

##### awaitingLoad : bool
Value used to load a scene correctly. Changing this might cause bugs.

#### **Methods**
##### loadScene(scene:NutScene) -> None
Loads a scene and unloads the one before it.

##### reloadScene() -> None
Unloads the scene and loads it back again.

##### start() -> None
Runs the game.

### NutKeyboard()
#### **Attributes**
##### curHeldKeys : list[int]
List containing all the keys that are being held down at the moment.

#### **Methods**
##### getKeyState(key:NutKey) -> NutKeyState
Returns wheter `key` is pressed, held, released or up.

##### update(curScene:NutScene) -> None
Reloads `curHeldKeys` and fires `onKeyInput()` on `curScene` for every key input (except when it is up).
This method is already ran automatically by the current `NutGame` class.

### NutScene()
Extends NutObject.
#### **Attributes**
##### bgColor : NutColor
The background color for this scene.

#### **Methods**
##### onLoaded() -> None
Runs once this scene has been loaded.
This method is already ran automatically by the current `NutGame` class.

##### onUnloaded() -> None
Runs once another scene has been loaded and replaces this one.
This method is already ran automatically by the current `NutGame` class.

##### onUpdated() -> None
Runs every frame when this class is loaded.
This method is already ran automatically by the current `NutGame` class.

##### afterUpdated() -> None
Runs after the `onUpdated()` method.
This method is already ran automatically by the current `NutGame` class.

##### onKeyInput(key:NutKey, key_state:NutKeyState) -> None
Runs every time a key has been pressed, and indicates the pressed key and its state.
This method is already ran automatically by the current `NutGame` class.

### NutRect(position:NutVector2, size:NutVector2, color:NutColor)
Extends NutObject.
