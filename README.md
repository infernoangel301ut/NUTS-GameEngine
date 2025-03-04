# NUTS Game Engine

Si deseas leer este documento en español, [haz click aquí](/README_Ñ.md).

## What is NUTS?

Deez NUTS! HAHA! OK, now for real.

NUTS is a game engine whose sole purpose is to give full freedom to the developer using it:

Anything is modifiable, anything is usable, ***anything is allowed***.

It is kinda like an anarchy for game development.

NUTS uses a structure similar to [HaxeFlixel](https://haxeflixel.com/) and a node-like structure for objects (a.k.a. a hierarchy-like structure).

It uses Python as its programming language and [Raylib](https://www.raylib.com/) as its base ([or at least a Python port of it](https://electronstudio.github.io/raylib-python-cffi/)).

NUTS is, and will always be open-source. You are free to modify NUTS to adjust it to your liking and even add features which are currently not added.

Just remember to credit the author in case of releasing a modified version of NUTS: infernoangel301 (me lmao).

Oh yea, the name? Yea it doesn't mean anything, just thought the name NUTS sounded funny.

## Which features can be found in NUTS?

NUTS is planned to have as many options for anything as possible, so even if a feature does not currently exists, you can suggest it yourself to be added in the future.

As for currently-added features:
* Two ways for input detection (`game.keyboard` or the scene's `onKeyInput` and `onMouseInput` events).
* Dynamic window resizing (the window adapts when being resized).
* Custom object creation.
* Conversions between types.
* Compatible with Raylib.
* And much more!

NUTS is currently in a really early development stage, so if you find any bugs, please make sure to report them on Github!

## How do I install NUTS?

Actually, that's pretty simple.

First, install the required Python modules:

(pip is used here, but if your Python build has issues, you can run whatever you need)

```
pip install setuptools
pip install raylib
pip install PyInstaller
```

* setuptools: raylib dependency.
* raylib: The module NUTS works on.
* PyInstaller: Used to export ([tutorial](https://imgur.com/FK8gPlc.png))

The recommended way of installing NUTS is by going into the GitHub releases section and downloading the nuts.py file from the version you want to install.

The non-recommended way of installing NUTS is by downloading the [nuts.py](/nuts.py) file in the repository itself (I might have missed something there, thus why it is not recommended).

To use NUTS, just create a Python file and import the NUTS file you just downloaded:

```python
# Like this
import nuts

# Or like this
from nuts import *
```

## How do I use NUTS?

Well, I will not be going into detail about it, since you should definetly check out the tutorials for that, but I'll explain some simple stuff:

You first wanna create a folder for your whole project, then add the nuts.py file you *probably* installed in.

Then create a separate Python file, and from there import nuts, just like it is specified in the above section.

The main code should look something like this:

```python
from nuts import *

game = NutGame(640, 480, "cool title") # Window width, window height and window title respectively.

class MainScene(NutScene):
    def onLoaded(self): # Runs once the scene has been loaded.
        print("Hey look! I'm going NUTS!!!")

    def onUpdated(self): # Runs in a loop until the scene gets unloaded.
        print("WEEWOO")

game.loadScene(MainScene())
game.start()
```

As an addition, you can also create a separate folder for your game assets to keep everything organized.

## How the fuck did you come up with NUTS?

Well, long story short, I came up with NUTS because of a project for school we *have* to work on for the entire grade (you heard me right, "*have*", not "*had*").

I initially had a couple ideas, but I decided to stick with a game engine, mainly because:

1. It's not really game so it kinda counts lmao.
2. We all have seen how a game is made, but what about the engines they use? We barely get any explanation on their functionality.

Midway through development, I was actually proud of how it was looking so far, so I decided that I would also be publishing it for everyone to use, plus doing more updates to it.

I mean, were you really expecting a game engine called ***NUTS*** to have an *emotive* backstory? lmao.
