# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutAudioManager Class

Manages and runs audio-related stuff.

Recommended way to use is by using the [NutGame](/DOCUMENTATION/FILES/NUTGAME.md) `audioManager` attribute.

### init method()

### Attributes

###### sounds : dict[str, [NutSound](/DOCUMENTATION/FILES/NUTSOUND.md)]

Dictionary that contains all stored sound effects and assigns them a name.

###### music : dict[str, [NutMusic](/DOCUMENTATION/FILES/NUTMUSIC.md)]

Dictionary that contains all stored music and assigns them a name.

### Methods

#### storeAudio(audio : [NutSound](/DOCUMENTATION/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION/FILES/NUTMUSIC.md), name : str) -> None

Saves an audio (either a sound effect or a song) with a name, which you can use to play the audio.

###### audio : [NutSound](/DOCUMENTATION/FILES/NUTSOUND.md) | [NutMusic](/DOCUMENTATION/FILES/NUTMUSIC.md)

The audio to save. Will save on the `sounds` attribute if its type is NutSound, and on the `music` attribute if its type is NutMusic.

###### name : str

The name the audio will be saved with. Will have to be used later in order to play the audio.

#### playAudio(is_sound : bool, name : str) -> None

Plays the audio.

###### is_sound : bool

Whether the audio got saved as a sound effect (True) or music (False).

###### name : str

The name the audio got saved with.

#### pauseAudio(is_sound : bool, name : str, pause : bool | None = None) -> None

Pauses or resumes an audio.

###### is_sound : bool

Whether the audio got saved as a sound effect (True) or music (False).

###### name : str

The name the audio will be saved with. Will have to be used later in order to play the audio.

###### pause : bool | None = None

Whether to pause it (True) or resume it (False).

If None, it will toggle the current value.

#### stopAudio(is_sound : bool, name : str) -> None

Stops an audio.

###### is_sound : bool

Whether the audio got saved as a sound effect (True) or music (False).

###### name : str

The name the audio will be saved with. Will have to be used later in order to play the audio.

#### updateAllAudios() -> None

Update all information on the audios.

Is automatically ran by NutGame, so no need to run it yourself.

#### unloadAllCurrentAudios() -> None

Gets rid of all currently stored audios.

Is automatically ran by NutGame, but you can still run it if needed.
