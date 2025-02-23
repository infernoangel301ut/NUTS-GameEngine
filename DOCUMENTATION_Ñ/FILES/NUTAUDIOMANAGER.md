# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutAudioManager

Controla y ejecuta cosas relacionadas al audio.

La manera recomendada de usarlo es usando el atributo `audioManager` de la clase [NutGame](/DOCUMENTATION_Ñ/FILES/NUTGAME.md).

### metodo init()

### Atributos

###### sounds : dict[str, [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md)]

Diccionario que contiene todos los efectos de sonido guardados y les asigna un nombre.

###### music : dict[str, [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md)]

Diccionario que contiene toda la música guardada y les asigna un nombre.

### Metodos

#### storeAudio(audio : [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md), name : str) -> None

Guarda un audio (ya sea un efecto de sonido o una cancion) con un nombre, el cual puedes usar para reproducir el audio.

###### audio : [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md)

El audio a guardar. Se guardara en el atributo `sounds` si su tipo es NutSound, y en el atributo `music` si su tipo es NutMusic.

###### name : str

El nombre con el cual se guardará el audio. Se tendrá que usar más tarde con tal de reproducir el audio.

#### playAudio(is_sound : bool, name : str) -> None

Reproduce un audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o una canción (False).

###### name : str

El nombre con el cual se guardó el audio.

#### pauseAudio(is_sound : bool, name : str, pause : bool | None = None) -> None

Pausa o continua un audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o una canción (False).

###### name : str

El nombre con el cual se guardó el audio.

###### pause : bool | None = None

Si pausarlo (True) o continuarlo (False).

Si el valor es None, cambiara el valor actual a su opuesto.

#### stopAudio(is_sound : bool, name : str) -> None

Detiene un audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o una canción (False).

###### name : str

El nombre con el cual se guardó el audio.

#### updateAllAudios() -> None

Actualiza toda la información de los audios.

Se ejecuta automáticamente por NutGame, asi que no hay necesidad de ejecutarlo tu mismo.

#### unloadAllCurrentAudios() -> None

Se deshace de todos los audios cargados al momento.

Se ejecuta automáticamente por NutGame, pero todavia puedes ejecutarlo tu mismo si es necesario.
