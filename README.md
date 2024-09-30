# NUTS Game Engine

Si prefieres leer el documento en español, [haga click aquí](/README_Ñ.md).

## What is NUTS?

Well, we're definetly not talking about actual **_nuts_**.

NUTS is a game engine that uses Python and Raylib (or at least a Python port of it).

Its way to be used is highly inspired by another game engine called HaxeFlixel, and also takes other elements from other game engines, such as Unity and Godot, while also adding its own elements.

Oh, also, it was made as a project for school, so unless it somehow becomes really used, I probably won't be updating it after its release.

## How do I install NUTS?

First of all, you will need the Python programming language, so if you don't have it yet, [click here](https://www.python.org/) to go to the official website.

Next, you will need the dependencies, which fortunately for you, you will only need the Python port for Raylib. So you can [click here](https://electronstudio.github.io/raylib-python-cffi/README.html#installation) to go to the documentation... or you can stay here and run the following commands to be a lot faster, your choice.

These are the two commands to run:

```bash
python -m pip install setuptools
python -m pip install raylib
```

And now that all the dependencies are installed, it is time to install NUTS!

Just download the file in the repository called [**nuts.py**](/nuts.py) and add it to your game folder. Yes, that's it.

## How do I start using NUTS?

Well, first of all, you must create a separate Python file ("main.py", "game.py"... just make sure it ends with ".py"). Make sure "nuts.py" and your main file are in the same directory.

Next, you want to import NUTS, to do so, just add the following line at the start of your code:

```python
import nuts
```

Now you wanna store your game as a variable, to do so, do the following (also remember to change the parameters):

```python
game = nuts.NutGame(960, 720, "NUTS game")
```

You now have the game, but you need a scene to show content to the player.

You will need to make a new class that extends the class NutScene and add anything you need:

```python
class TestScene(nuts.NutScene):
    def __init__(self):
        super().__init__()
        # Store your scene attributes here, remember to use self

    def onLoaded(self):
        print("The testing scene has been loaded!")
        # Will run once the scene has been loaded
    
    def onUpdated(self):
        pass
        # Will run every frame

    def onKeyInput(self, key:nuts.NutKey, key_state:nuts.NutKeyState):
        pass
        # Will run everytime a key is pressed or released
```

Every method inside the class has its functionalities:
* **__init__()**: Anything inside it will run even before the scene has been loaded. It is used to store attributes and values.
* **onLoaded()**: It will run once `game.loadScene()` has been ran with this scene.
* **onUpdated()**: It will run every frame, and therefore all the time, allowing you to do constant changes.
* **onKeyInput(key, key_state)**: It will run when the user pressed or released a key, the `key` parameter contains the key that was pressed, while the `key_state` parameters indicates whether the key is pressed, held or released.

Now we have a scene to show, so lastly, we need to get the game to display it and finally run.

To do so, you will add these last lines:

```python
game.loadScene(TestScene())
game.start()
```

So our first NUTS project has started, here is the full code in case you are lazy and just want to copy and paste:

```python
import nuts

game = nuts.NutGame(960, 720, "NUTS game")

class TestScene(nuts.NutScene):
    def __init__(self):
        super().__init__()
        # Store your scene attributes here, remember to use self

    def onLoaded(self):
        print("The testing scene has been loaded!")
        # Will run once the scene has been loaded
    
    def onUpdated(self):
        pass
        # Will run every frame

    def onKeyInput(self, key:nuts.NutKey, key_state:nuts.NutKeyState):
        pass
        # Will run everytime a key is pressed or released

game.loadScene(TestScene())
game.start()
```