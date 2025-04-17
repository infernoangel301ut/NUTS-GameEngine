# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSCENE.md).

## Clase NutScene

[Esta clase extiende a la clase [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), aquellos atributos y mètodos obtenidos de él no se mostrarán por simplicidad]

Una escena para ser mostrada por el juego, contiene gran parte de las cosas principales para que se ejecute el juego.

Para hacer tu propia escena, extiende esta clase.

### Atributos

###### bgColor : [NutColor](/DOCUMENTATION_Ñ/FILES/NUTCOLOR.md)

El color del fondo de esta escena.

###### keepAudioOnUnload : bool

Si todos los audios deberían ser eliminados en cambiar a otra escena. (True por predeterminado)

###### update_paused : bool

Si el evento onUpdated should be ejectuarse o no. (False por predeterminado)

###### drawing_paused : bool

Si los sprites animados en esta escena deberían pausarse o no. (False por predeterminado)

### Métodos

#### onLoaded() -> None

Evento que se ejecuta cuando la escena ha sido cargada (y luego ya no XD).

#### onUpdated() -> None

Evento que se ejecuta constantemente.

#### onUpdatedPost() -> None

Evento que se ejecuta después de que todo en la escena se haya actualizado, y por tanto también se ejecuta constantemente.

#### OnUnloaded() -> None

Evento que se ejecuta cuando se ha cargado otra escena (así que esta queda reemplazada).

#### OnKeyInput(key : [NutKey](/DOCUMENTATION_Ñ/FILES/NUTKEY.md), state : [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md)) -> None

Evento que se ejecuta cuando un input se ha hecho por el teclado.

###### key : [NutKey](/DOCUMENTATION_Ñ/FILES/NUTKEY.md)

La tecla del input.

###### state : [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md)

El estado en el que se encontraba la tecla.

#### onMouseInput(action : [NutMouseAction](/DOCUMENTATION_Ñ/FILES/NUTMOUSEACTION.md), state : [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md), position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)) -> None

Evento que se ejecuta cuando un input se ha hecho por el ratón.

###### action : [NutMouseAction](/DOCUMENTATION_Ñ/FILES/NUTMOUSEACTION.md)

Que botón del ratón ha sido pulsado.

###### state : [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md)

El estado en el que se encontraba el botón del ratón.

###### position : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

La posición del ratón en el momento del input.
