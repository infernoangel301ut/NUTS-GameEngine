# NUTS Game Engine Documentation

Si prefieres leer la documentación en español, [haga click aquí](https://www.google.com/search?q=nigger&rlz=1CAGSIC_enES866&oq=nigger&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhgKGLEDGIAEMgwIAhAuGAoYsQMYgAQyDwgDEC4YChivARjHARiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyDAgGEC4YChixAxiABDIMCAcQLhgKGLEDGIAEMhIICBAAGAoYgwEYsQMYgAQYigXSAQgxNDA3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8&safe=active&ssui=on) (todavía no hay documentación en español XD).

## NutTimer Class

[This class extends the [NutObject](/DOCUMENTATION/FILES/NUTOBJECT.md) class, attributes and methods inherited from it will not be shown for simplicity]

Time that goes on until it finishes. Also runs certain events depending on what happens.

### init method (time : float, loops : int = 1)

###### time : float

The time in seconds until a loop is finished.

###### loops : int = 1

The amount of times the timer will repeat itself.

If the amount of loops is 0 or lower, the timer will loop infinitely.

### Attributes

###### time : float

The time in seconds until a loop is finished.

###### loops : int

The amount of times the timer will repeat itself.

If the amount of loops is 0 or lower, the timer will loop infinitely.

###### current_time : float

The amount of time that went on.

###### current_loops : int

The amount of loops completed.

###### playing : bool

Whether the timer is playing or not.

###### on_timer_completed : (timer : NutTimer) -> None

Function that runs when the timer has finished all loops and therefore stops playing.

###### on_loop_completed : (timer : NutTimer) -> None

Function that runs when the timer has completed a loop.

###### on_timer_update : (timer : NutTimer) -> None

Function that runs while the timer is playing.

### Methods

#### play() -> None

Starts the timer.

#### stop() -> None

Stops the timer before actually ending.

#### pause(paused : bool | None = None) -> None

Pauses or resumes the timer.

If paused is None, it will toggle the pause. Otherwise, it will pause it according to it.

#### update() -> None

Updates the timer progress.

#### [static] empty_timer_function(timer : NutTimer) -> None

Default value for all events (you can see them in the attributes).
