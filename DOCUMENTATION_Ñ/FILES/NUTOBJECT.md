# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTOBJECT.md).

## Clase NutObject

La base para objetos ubicados en la pantalla, todo aquello que se renderiza proviene de esta clase.

### método init (position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2())

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md) = NutVector2()

La posición del objeto en la ventana (aun así no será visible, por que no és NADA).

### Atributos

###### children : dict[str, NutObject]

Los otros NutObjects que dependen de este.

###### position : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

La posición del objeto en la ventana.

### Métodos

#### render(globalPos : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md), parent : NutObject | None, paused : bool) -> None

Renderiza este objeto en la ventana.

(Este método se ejecuta automáticamente por la clase [NutGame](/DOCUMENTATION/FILES/NUTGAME.md), no hay necesidad de ejecutarlo tú mismo).

###### globalPos : [NutVector2](/DOCUMENTATION/FILES/NUTVECTOR2.md)

La posición del parent, para ajustar la posición del objeto actual.

###### parent : NutObject | None

El parent de este NutObject, o None si no tiene parent (chiste de sin papa gracioso).

Usado para obtener propiedades del parent.

###### paused : bool

Si está pausado o no.

#### centerX() -> None

Centra el NutObject en el eje X.

#### centerY() -> None

Centra el NutObject en el eje Y.

#### center() -> None

Centra el NutObject tanto en el eje X como en el eje Y.