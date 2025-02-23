# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](/DOCUMENTATION_Ñ/INDEX.md).

## NutSound Class

The class used for sound effects (USE NutMusic FOR MUSIC).

### init method (path : str, volume : float = 0.5, pitch : float = 1)

###### path : str

The path of the sound you want to play.

###### volume : float = 0.5

The sound volume.

###### pitch : float = 1

The sound pitch (original pitch is 1).

### Attributes

###### file_path : str

The path of the sound you want to play.

###### raylib_audio : pyray.Sound

The raylib version of the sound.

###### volume : float

The sound volume.

###### pitch : float

The sound pitch (original pitch is 1).

###### paused : bool

Whether the sound effect is paused or not.

###### playing : bool

Whether the sound effect is playing or not.

###### pan : float

The direction the sound goes to, mostly for headsets.

(0 is left, 1 is right, and 0.5 is centered).
