# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutGame

La clase más importante, literalmente lo ejecuta todo.

### metodo init(winWidth : float, winHeight : float, title : str, fps : int = 60)

###### winWidth : float

El ancho de la ventana del juego.

###### winHeight : float

El alto de la ventana del juego.

###### title : str

El titulo de la ventana del juego.

###### fps : int = 60

Los fps a los que se ejecutará el juego.

### Atributos

###### winWidth : float

El ancho de la ventana del juego.

###### winHeight : float

El alto de la ventana del juego.

###### title : str

El titulo de la ventana del juego.

###### fps : int

Los fps a los que se ejecutará el juego.

###### curScene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena siendo mostrada al momento en la pantalla.

###### keyboard : [NutKeyboard](/DOCUMENTATION_Ñ/FILES/NUTKEYBOARD.md)

El controlador de inputs principal, comprueba si hay inputs del teclado y del ratón.

###### audioManager : [NutAudioManager](/DOCUMENTATION_Ñ/FILES/NUTAUDIOMANAGER.md)

El controlador de audios principal, reproduce y guarda sonidos y música.

###### saveFiles : dict[str, [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)]

El almacén de archivos de guardado, toda la información de guardado está en este diccionario.

###### awaitingLoad : bool

Comprueba si debería ejecutar el evento onLoaded() de la escena.

Se recomienda no cambiarlo por tu cuenta.

###### awaitingAudioClear : bool

Si se debería eliminar todos los audios en el siguiente frame o no.

Se asigna automaticamente cambiando la escena, y tendrá que ver con su atributo clearAudioOnUnload.

###### gameShouldEnd : bool

Si el juego se debería cerrar en el siguiente frame o no.

Como alternativa, puedes usar el metodo close(), el cual asignara automaticamente el valor de este atributo a True.

### Metodos

#### saveFileExists(file_dir : str, file_name : str) -> bool

Si el archivo de guardado especificado existe o no. Principalmente usado para crear o guardar un archivo de guardado.

###### file_dir : str

The folder on which the save file should be located in.
La carpetwa en la cual el archivo de guardado debería estar ubicado.

###### file_name : str

The name of the file to check on. Do not add the file extension.
El nombre del archivo que comprobar. Do añadas la extensión de archivo.

#### addSaveFile(save : [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)) -> None

Añade el archivo de guardado al atributo saveFiles, asignando su clave al atributo file_name del archivo de guardado.

###### save : [NutSaveFile](/DOCUMENTATION_Ñ/FILES/NUTSAVEFILE.md)

El archivo de guardado que añadir.

#### loadScene(scene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)) -> None

Carga la escena especificada y descarga la anterior.

###### scene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena que cargar.

#### reloadScene() -> None

Carga el metodo loadScene usando la escena actual, recargandola de esta manera.

#### close() -> None

Cierra la ventana del juego.

#### start() -> None

Empieza a ejecutar el juego y todo lo demás.
