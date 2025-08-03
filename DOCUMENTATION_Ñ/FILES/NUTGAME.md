# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTGAME.md).

## Clase NutGame

La clase más importante, literalmente lo ejecuta todo.

### método init (winWidth : float, winHeight : float, title : str, fps : int = 60)

###### winWidth : float

La anchura de la ventana del juego.

###### winHeight : float

La altura de la ventana del juego.

###### title : str

El título de la ventana del juego.

###### fps : int = 60

Los fps a los que se ejecutará el juego.

### Atributos

###### winWidth : float

La anchura de la ventana del juego.

###### winHeight : float

La altura de la ventana del juego.

###### viewWidth : float

La anchura de la vista del juego.

###### viewHeight : float

La altura de la vista del juego.

###### winPos : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición actual de la ventana en el escritorio.

###### title : str

El título de la ventana del juego.

###### fps : int

Los fps a los que se ejecutará el juego.

###### curScene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena siendo mostrada actualmente en pantalla.

###### keyboard : [NutKeyboard](/DOCUMENTATION_Ñ/FILES/NUTKEYBOARD.md)

El gestionador principal de los inputs, comprueba inputs por parte del teclado y del ratón.

###### audioManager : [NutAudioManager](/DOCUMENTATION_Ñ/FILES/NUTAUDIOMANAGER.md)

El controlador principal de audios, reproduce y guarda efectos de sonido y música..

###### saveFiles : dict[str, [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)]

El almacén de archivos de guardado, toda la información de guardado está en este diccionario.

###### awaitingLoad : bool

Comprueba si debería ejecutar el evento onLoaded() de la escena.

Se recomienda que no lo hagas por tí mismo/a.

###### awaitingAudioClear : bool

Si se espera eliminar todos los audios en el siguiente frame o no.

Se asigna automaticamente al cambiar la escena, y tiene que ver con su atributo clearAudioOnUnload.

###### gameShouldEnd : bool

Si el juego se debería cerrar en el siguiente frame o no.

Alternativamente, puedes ejecutar el método close(), el cual asignará este atributo automaticamente a True.

###### viewportCamera : pyray.Camera2D

La camara de raylib que contiene la vista relativa al tamaño de la ventana.

[¡¡¡EXPLICACIÓN!!! La ventana es lo que estás viendo en el escritorio, mientras que la vista es lo que la ventana en sí contiene. Ambos pueden tener diferentes tamaños.]

[La vista mantiene el tamaño inicial mientras se adapta al de la ventana, de esa manera, cambiarle el tamaño a la ventana tiene menos glitches.]

###### resizable : bool

Si a la ventana se le puede cambiar el tamaño o no. Usa el método `updateWindowProperties` para aplicar.

###### fullscreen : bool

Si el juego debería estar en pantalla completa o en forma de ventana. Usa el método `updateWindowProperties` para aplicar.

###### was_fullscreen : bool

Si el juego estaba anteriormente en pantalla completa o en forma de ventana, utilizado para evitar glitches.

###### shouldRestoreAfterFullscreen : bool

Si el juego debería aplicar algunos cambios después de la pantalla completa, utilizado para evitar glitches.

###### borderless : bool

Si la ventana debería tener bordes o no. Usa el método `updateWindowProperties` para aplicar.

###### was_borderless : bool

Si la ventana estaba con bordes o sin, usado para evitar glitches.

###### allowsTransparency : bool

Si la ventana permite que el fondo tenga transparencia o no. Usa el método `updateWindowProperties` para aplicar.

###### viewBorderColor : [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)

El color usado para los bordes de la vista.

### Métodos

#### saveFileExists(file_dir : str, file_name : str) -> bool

Si el archivo de guardado especificado existe o no. Mayormente usado para crear o cargar un archivo de guardado.

###### file_dir : str

El directorio en el que el archivo de guardado debería estar ubicado.

###### file_name : str

El nombre del archivo que comprobar. No añadas la extensión del archivo.

#### addSaveFile(save : [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)) -> None

Añade el archivo de guardado al atributo saveFiles, asignando su clave al atributo file_name del archivo de guardado.

###### save : [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)

El archivo de guardado que añadir.

#### loadScene(scene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)) -> None

Carga la escena especificada y quita la anterior.

###### scene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena que cargar.

#### reloadScene() -> None

Ejecuta el método loadScene usando la escena actual, recargandola.

#### close() -> None

Cierra la ventana del juego.

#### updateWindowSize() -> None

Actualiza el tamaño de la ventana según los atributos `winWidth` y `winHeight`.

#### updateWindowPos() -> None

Actualiza la posición de la ventana según el atributo `winPos`.

#### updateWindowProperties() -> None

Actualiza la ventana según los atributos que la definen.

#### setFPS(val : int) -> None

Cambia los FPS a los que se ejecuta el juego.

###### val : int

Los FPS a los que se ejecutará el juego.

#### start() -> None

Empieza a ejecutar el juego y todo lo demás.
