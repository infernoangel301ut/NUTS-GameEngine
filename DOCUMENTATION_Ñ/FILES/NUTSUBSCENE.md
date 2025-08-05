# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTSUBSCENE.md).

## Clase NutSubScene

[Esta clase extiende a la clase [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md), aquellos atributos y métodos obtenidos de él no se mostrarán por simplicidad]

Una escena dentro de otra escena, aún hace todo lo que una escena normal hace.

Para hacer tu propia subescena, extiende esta clase.

### método init (parentScene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md), transparentBG : bool = True)

###### parentScene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena de la que depende esta subescena (en la mayoría de casos, el valor de este parámetro será `self`).

###### transparentBG : bool = True

Si automáticamente hacer el fondo de esta subescena transparente o no. Útil si aún quieres ver la escena principal.

### Atributos

###### parentScene : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena de la que depende esta subescena.

###### activated : bool

Si esta subescena se está mostrando o no.

###### awaitingLoad : bool

Si se espera que el evento `onLoaded` se ejecute.

###### awaitingUnload : bool

Si se espera que el evento `onUnloaded` se ejecute.

### Métodos

#### toggleActivate(value : bool | None = None) -> None

Utilizado para mostrar o esconder esta subescena (y cambiar el atributo `activated`).

###### value : bool | None = None

Si activar esta subescena (True) o desactivarla (False).

Si el valor es None, cambiará al opuesto del valor actual.