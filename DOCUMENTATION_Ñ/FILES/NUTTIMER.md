# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTTIMER.md).

## Clase NutTimer

[Esta clase extiende a la clase [NutObject](/DOCUMENTATION_Ñ/FILES/NUTOBJECT.md), aquellos atributos y métodos obtenidos de el no se mostrarán por simplicidad]

Tiempo que sigue hasta que termina. También ejecuta ciertos eventos dependiendo de lo que pase.

### método init (time : float, loops : int = 1)

###### time : float

El tiempo en segundos hasta que una repetición haya terminado.

###### loops : int = 1

La cantidad de veces que el temporizador se repetirá.

Si la cantidad de repeticiones es igual o menor a 0, el temporizador se repetirá infinitamente.

### Atributos

###### time : float

El tiempo en segundos hasta que una repetición haya terminado.

###### loops : int

La cantidad de veces que el temporizador se repetirá.

Si la cantidad de repeticiones es igual o menor a 0, el temporizador se repetirá infinitamente.

###### current_time : float

La cantidad de tiempo que ha pasado.

###### current_loops : int

La cantidad de repeticiones completadas.

###### playing : bool

Si el temporizador se está reproduciendo o no.

###### on_timer_completed : (timer : NutTimer) -> None

Función que se ejecuta cuando el temporizador ha terminado todas las repeticiones y, por lo tanto, deja de reproducirse.

###### on_loop_completed : (timer : NutTimer) -> None

Función que se ejecuta cuando el temporizador ha terminado una repetición.

###### on_timer_update : (timer : NutTimer) -> None

Función que se ejecuta mientras el temporizador se reproduce.

### Métodos

#### play() -> None

Inicia el temporizador.

#### stop() -> None

Detiene el temporizador antes de terminar.

#### pause(paused : bool | None = None) -> None

Pausa o continua el temporizador.

Si paused es None, se cambiará el estado de la pausa. Si no, se pausará según el valor.

#### update() -> None

Actualiza el progreso del temporizador.

#### [static] empty_timer_function(timer : NutTimer) -> None

Valor por predeterminado para todos los eventos (puedes verlos en los atributos).
