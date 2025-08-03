# NUTS Game Engine Code Examples

This document covers general aspects of NUTS, so as to get an idea on how to use it.

## Index

* [1 - Code template](#1---code-template)
* [2A - Detecting inputs](#2a---detecting-inputs)
* [2B - Detecting inputs (ALTERNATIVE)](#2b---detecting-inputs-alternative)
* [3 - Switching between scenes](#3---switching-between-scenes)
* [4 - Creating an object](#4---creating-an-object)
* [5A - Animated sprites (SPRITESHEET SYSTEM)](#5a---animated-sprites-spritesheet-system)
* [5B - Animated sprites (SPARROW SYSTEM)](#5b---animated-sprites-sparrow-system)
* [6 - Timers](#6---timers)
* [7 - Tweens](#7---tweens)
* [8 - Playing audio](#8---playing-audio)
* [9 - Save files](#9---save-files)

## 1 - Code template

```python
from nuts import *

game = NutGame(1280, 720, "game title") # Window width, window height and window title respectively.

class MainScene(NutScene): # The scene class
    def __init__(self): # When the scene object is initialized ...
        super().__init__() # Creates all required attributes and methods for a scene
        # Create all attributes in here

    def onLoaded(self): # When the scene is loaded using game.loadScene() ...
        pass # Code to run (remove "pass")

    def onUnloaded(self): # When another scene is loaded using game.loadScene() ...
        pass # Code to run (remove "pass")

    def onUpdated(self, elapsed:float): # When loading next frame (before rendering) ...
        pass # Code to run (remove "pass")
        # elapsed : float -> Time in seconds since last frame.

    def onUpdatedPost(self, elapsed:float): # When loading next frame (after rendering) ...
        pass # Code to run (remove "pass")
        # elapsed : float -> Time in seconds since last frame.

    def onKeyInput(self, key:NutKey, state:NutKeyState): # Whenever an input is detected from the keyboard ...
        pass # Code to run (remove "pass")
        # key : NutKey -> The key detected from the input.
        # state : NutKeyState -> The state in which the input was found.
    
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2): # Whenever an input is detected from the mouse ...
        pass # Code to run (remove "pass")
        # action : NutMouseAction -> The mouse button detected from the input.
        # state : NutKeyState -> The state in which the input was found.
        # position : NutVector2 -> The mouse position at the moment of the input.

game.loadScene(MainScene())
game.start()    
```

## 2A - Detecting inputs

```python
from nuts import *

game = NutGame(1280, 720, "game title")

class MainScene(NutScene):
    # The event to be used to detect keyboard inputs
    # key => The key which has been pressed.
    # state => The state in which the inputed key was found in.
    def onKeyInput(self, key:NutKey, state:NutKeyState):
        pass # Run some code here lmao

    # The event to be used to detect mouse inputs
    # action => The mouse button which has been pressed.
    # state => The state in which the inputed mouse button was found in.
    # position => The mouse position when the input was made.
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2):
        pass # Run some code here lmao

game.loadScene(MainScene())
game.start()
```

## 2B - Detecting inputs (ALTERNATIVE)

```python
# Checks if a specified key (E in this case) is in a specific state (being pressed right now, in this case)
if game.keyboard.getKeyState(NutKey.E) == NutKeyState.JUST_PRESSED: pass

# Checks if a specified mouse button (left in this case) is in a specific state (being pressed right now, in this case)
if game.keyboard.getMouseState(NutMouseAction.LEFT) == NutKeyState.JUST_PRESSED: pass

# Prints the current mouse position
print(game.keyboard.getMousePosition())
```

## 3 - Switching between scenes

```python
from nuts import *

game = NutGame(1280, 720, "game title")

class Scene1(NutScene):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(255, 0, 0) # Sets the scene's background color to red.

    def onKeyInput(self, key:NutKey, state:NutKeyState):
        if state == NutKeyState.JUST_PRESSED and key == NutKey.Q:
            game.loadScene(Scene2()) # Switch to the second scene

class Scene2(NutScene):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(0, 0, 255) # Sets the scene's background color to blue.

    def onKeyInput(self, key:NutKey, state:NutKeyState):
        if state == NutKeyState.JUST_PRESSED and key == NutKey.Q:
            game.loadScene(Scene1()) # Switch to the first scene.

game.loadScene(Scene1())
game.start()
```

## 4 - Creating an object

```python
# ... Inside of a scene
self.children["objName"] = NutObject()

# objName's child
self.children["objName"].children["subObj"] = NutObject()

# Can be any type that extends NutObject (like NutSprite, NutRect, NutText, etc.)
```

## 5A - Animated sprites (SPRITESHEET SYSTEM)

```python
# Create a NutSprite as usual (where the image directory, add the animated sprite image)
self.children["spr"] = NutSprite("image.png", NutVector2())
# Setup the spritesheet animation system using each animation's width and height as parameters.
self.children["spr"].animation.setupSpritesheetAnimation(20, 30)
# Create all animations like this:
# - First parameter : Animation name
# - Second parameter : All frames in order (from left to right, top to bottom).
# - Third parameter : Whether the animation is in reverse or not.
# - Fourth parameter : Whether the animation is looped or not.
# - Fifth parameter : The frames per second the animation will run at (not the same as the game's FPS).
self.children["spr"].animation.makeSpritesheetAnimation("anim name", [0, 1, 2, 3, 4], False, True, 60)
# Play the animation using its name.
self.children["spr"].animation.playAnimation("anim name")
```

## 5B - Animated sprites (SPARROW SYSTEM)

The sparrow animation system requires a PNG file and an XML file.

They can both be generated using Adobe Animate (or you can also use other programs).

```python
# Create a NutSprite as usual (where the image directory, add the animated sprite image)
self.children["spr"] = NutSprite("image.png", NutVector2())
# Setup the sparrow animation system using the XML file as a parameter.
self.children["spr"].animation.setupSparrowAnimation("image.xml")
# Create all animations like this:
# - First parameter : Animation name
# - Second parameter : The animation name inside of the XML file.
# - Third parameter : Whether the animation is in reverse or not.
# - Fourth parameter : Whether the animation is looped or not.
# - Fifth parameter : The frames per second the animation will run at (not the same as the game's FPS).
self.children["spr"].animation.makeSparrowAnimation("anim name", "anim", False, True, 60)
# Play the animation using its name.
self.children["spr"].animation.playAnimation("anim name")
```

## 6 - Timers

```python
# First parameter : Time for the timer to finish in seconds
# Second parameter : The amount of times the timer will run.
#       If the value is negative, the timer will run infinitely.
self.children["tmr"] = NutTimer(10, -1)

# Timer event
def event(tmr:NutTimer): print("Hello world!")

# For every loop completed, the previous function will run
self.children["tmr"].on_loop_completed = event

# Plays the timer
self.children["tmr"].play()
```

## 7 - Tweens

(CHECK [NutTweenEase](/DOCUMENTATION/FILES/NUTTWEENEASE.md) IN THE DOCUMENTATION!!!)

```python
# The object to be tweened (otherwise how are you even gonna tween)
self.children["rect"] = NutRect(NutVector2(100, 100), NutVector2(100, 100), NutColor(255, 0, 0))

# The tween must be a child of the object you want to tween.
# - First parameter : The attribute you want to tween.
# - Second parameter : The value to tween to.
# - Third parameter : The time the tween will take to finish.
# - Fourth parameter : The ease the tween will follow.
self.children["rect"].children["tween"] = NutTween("color", NutColor(0, 0, 255), 3, NutTweenEase.quadOut)

# Plays the tween
self.children["rect"].children["tween"].play()
```

## 8 - Playing audio

```python
# Store audio into the audio manager
game.audioManager.storeAudio(
    # Stores an audio:
    # - Parameter 1 : The audio directory.
    # - Paramater 2 : Whether the audio should loop or not.
    # - Parameter 3 : The volume.
    # - Parameter 4 : The pitch modifier.
    NutMusic("song.ogg", True, 0.5, 1),
    # The name the audio will be stored as
    "music"
)

# Plays the audio
# - Parameter 1 : Whether the audio is a NutSound (True) or a NutMusic (False)
# - Parameter 2 : The name the audio got stored as
game.audioManager.playAudio(False, "music")
```

## 9 - Save files

```python
# Stores the save file named "main" in the "saves" folder
game.addSaveFile(NutSaveFile("saves", "main"))

# If the previous save file exists...
if game.saveFileExists("saves", "main"):
    # Then load all its contents.
    game.saveFiles["main"].loadFile()
else:
    # Otherwise just create all the save properties yourself.
    game.saveFiles["main"].setProperty(
        # Where "test" is the value name
        # int is the value type (can use other types too)
        # and 9 is the value itself
        NutSaveProperty("test", int, 9)
    )

# Modifying a save value:
game.saveFiles["main"].properties["test"].val.value = 15

# Saving the save file changes
game.saveFiles["main"].saveFile()
```