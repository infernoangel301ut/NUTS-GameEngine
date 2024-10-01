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

#### **Atributes**
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
The keyboard input manager. Changing this might cause bugs, make sure to use the `onKeyInput()` event in a `NutScene` class instead.

##### awaitingLoad : bool
Value used to load a scene correctly. Changing this might cause bugs.

#### **Methods**
##### loadScene(scene:NutScene) -> None
Loads a scene and unloads the one before it.

##### start() -> None
Runs the game.
