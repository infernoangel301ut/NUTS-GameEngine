# Documentación de NUTS Game Engine

If you wish to read the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

Or if you wish to read this specific document in English, [click here](/DOCUMENTATION/FILES/NUTAUDIOMANAGER.md).

## Clase NutAudioManager

Gestiona y ejecuta cosas relacionadas a los audios.

La forma recomendada de utilizarlo es a través del atributo `audioManager` de [NutGame](/DOCUMENTATION_Ñ/FILES/NUTGAME.md).

### Atributos

###### sounds : dict[str, [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md)]

Diccionario que contiene todos los efectos de sonido guardados y les asigna un nombre.

###### music : dict[str, [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md)]

Diccionario que contiene toda la música guardada y le asigna un nombre.

### Métodos

#### storeAudio(audio : [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md), name : str) -> None

Guarda un audio (ya sea un efecto de sonido o una canción) con un nombre, el cual puedes utilizar para reproducir el audio.

###### audio : [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md)

El audio que guardar. Se guardará en el atributo `sounds` si su tipo es [NutSound](/DOCUMENTATION_Ñ/FILES/NUTSOUND.md), y en el atributo `music` si su tipo es [NutMusic](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md).

###### name : str

El nombre con el que se guardará el audio. Se tendrá que usar más tarde para reproducir el audio.

#### playAudio(is_sound : bool, name : str) -> None

Reproduce el audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o como música (False).

###### name : str

El nombre con el que se guardó el audio.

#### pauseAudio(is_sound : bool, name : str, pause : bool | None = None) -> None

Pausa o continua un audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o como música (False).

###### name : str

El nombre con el que se guardó el audio.

###### pause : bool | None = None

Si pausarlo (True) o continuarlo (False).

Si es None, se cambiará al estado opuesto.

#### stopAudio(is_sound : bool, name : str) -> None

Detiene un audio.

###### is_sound : bool

Si el audio se guardó como un efecto de sonido (True) o como música (False).

###### name : str

El nombre con el que se guardó el audio.

#### updateAllAudios() -> None

Actualiza toda la información de los audios.

Se ejecuta automaticamente por [NutGame](/DOCUMENTATION_Ñ/FILES/NUTGAME.md), así que no hay necesidad de ejecutarlo tu mismo/a.

#### unloadAllCurrentAudios() -> None

Elimina todos los audios actualmente guardados.

Se ejecuta automaticamente por [NutGame](/DOCUMENTATION_Ñ/FILES/NUTGAME.md), pero puedes ejectuarlo si es necesario.
