# NUTS Game Engine Documentation

Si deseas leer la documentación en español, [haz click aquí](/DOCUMENTATION_Ñ/INDEX.md).

O si deseas leer solo este documento en español, [haz click aquí](/DOCUMENTATION_Ñ/FILES/NUTMUSIC.md).

## NutMusic Class

The class used for music (USE [NutSound](/DOCUMENTATION/FILES/NUTSOUND.md) FOR SOUND EFFECTS).

### init method (path : str, looped : bool = False, volume : float = 0.5, pitch : float = 1)

###### path : str

The path of the music you want to play.

###### looped : bool = False

Whether the music should loop or not.

###### volume : float = 0.5

The music volume.

###### pitch : float = 1

The music pitch (original pitch is 1).

### Attributes

###### file_path : str

The path of the music you want to play.

###### raylib_audio : pyray.Music

The raylib version of the music.

###### looped : bool

Whether the music should loop or not.

###### volume : float

The music volume.

###### pitch : float

The music pitch (original pitch is 1).

###### paused : bool

Whether the music is paused or not.

###### playing : bool

Whether the music is playing or not.

###### pan : float

The direction the music goes to, mostly for headsets.

(0 is left, 1 is right, and 0.5 is centered).
