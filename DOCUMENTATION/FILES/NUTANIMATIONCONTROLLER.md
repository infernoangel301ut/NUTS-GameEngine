# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutAnimationController Class

The class that controls animations for a sprite.

### init method (img_size : NutVector2)

###### img_size : NutVector2

The size of the original image for the sprite.

### Attributes

###### animations : dict[str, NutAnimation]

Contains all animations.

###### cur_anim : str

Current animation that's being played.

###### anim_xml : XmlTree.Element | None

The animation's XML file (for sparrow animation system).

###### anim_type : NutAnimationType

The current animation system being used.

###### cur_frame : int

The frame being displayed in the current animation. Floored version of cur_frame_dec.

###### cur_frame_dec : float

The actual version of cur_frame, with the decimals.

###### spritesheet_size : NutVector2 | None

The size of every frame, used for the spritesheet animation system.

###### img_size : NutVector2

The size of the original image for the sprite.

###### anim_playing : bool

Whether an animation is currently playing or not.

### Methods

#### setupSpritesheetAnimation(frame_width : int, frame_height : int) -> None

Sets up the spritesheet animation system.

###### frame_width : int

The width of all the frames.

###### frame_height : int

The height of all the frames.

#### setupSparrowAnimation(xml_file_dir : str) -> None

Sets up the sparrow animation system.

###### xml_file_dir : str

The directory of the XML file.

#### makeSpritesheetAnimation(name : str, anim : list[int], reversed : bool = False, looped : bool = False, fps : int = 60) -> None

Creates a new animation for the spritesheet system.

###### name : str

The name for the animation.

###### anim : list[int]

The list of the frames to play.

###### reversed : bool = False

Whether to play the animation in reverse or not.

###### looped : bool = False

Whether to loop the animation or not.

###### fps : int = 60

The speed of the animation.

#### makeSparrowAnimation(name : str, anim_name : str, reversed : bool = False, looped : bool = False, fps : int = 60) -> None

Creates a new animation for the sparrow system.

###### name : str

The name for the animation.

###### anim_name : str

The animation name in the XML file.

###### reversed : bool = False

Whether to play the animation in reverse or not.

###### looped : bool = False

Whether to loop the animation or not.

###### fps : int = 60

The speed of the animation.

#### playAnimation(anin_name : str) -> None

Plays an animation.

###### anim_name : str

The name of the animation you want to play.

#### pause(unpause : bool | None = None) -> None

Pauses or resumes the animation.

###### unpause : bool | None = None

Whether the animation should be paused or resumed.

If None, it will just toggle.

#### stop() -> None

Stops the animation.

#### isAnimated() -> bool

Returns whether there's an animation or not.
