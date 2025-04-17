# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTKEYBOARD.md).

## Clase NutKeyboard

Gestiona los inputs tanto del teclado como del ratón.

La forma recomendada de utilizarlo es a través del atributo `keyboard` de [NutGame](/DOCUMENTATION_Ñ/FILES/NUTGAME.md).

### Atributos

###### curHeldKeys : list[[NutKey](/DOCUMENTATION_Ñ/FILES/NUTKEY.md)]

Almacena todas las teclas que se están manteniendo.

### Métodos

#### getKeyState(key : [NutKey](/DOCUMENTATION_Ñ/FILES/NUTKEY.md)) -> [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md)

Regresa el estado en el que se encuentra la tecla.

###### key : [NutKey](/DOCUMENTATION_Ñ/FILES/NUTKEY.md)

La tecla de la cual dar información.

#### getMouseState(action : [NutMouseAction](/DOCUMENTATION_Ñ/FILES/NUTMOUSEACTION.md)) -> [NutKeyState](/DOCUMENTATION_Ñ/FILES/NUTKEYSTATE.md)

Regresa el estado en el que se encuentra el botón del ratón.

###### action : [NutMouseAction](/DOCUMENTATION_Ñ/FILES/NUTMOUSEACTION.md)

El botón del ratón del cual dar información.

#### getMousePosition() -> [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

Regresa la posición actual del ratón.

#### update(curState : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)) -> None

Actualiza toda la información relacionada a las teclas y ejecuta eventos de los inputs para la escena cargada actualmente y sus subescenas, en caso de haber inputs.

###### curState : [NutScene](/DOCUMENTATION_Ñ/FILES/NUTSCENE.md)

La escena cargada actualmente.
