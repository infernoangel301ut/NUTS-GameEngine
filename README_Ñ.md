# NUTS Game Engine

If you rather reading this document in English, [click here](/README.md).

## ¿Qué es NUTS?

Bueno, definivamente no estamos hablando de la palabra inglesa "nuts", es decir, **_nueces_**.

NUTS es un motor de desarrollo de videojuegos que usa Python y Raylib (o al menos una versión de Python de este).

Su manera de emplearse esta altamente inspirada por otro motor llamado HaxeFlixel, y también toma otros elementos de otros motores, tales como Unity y Godot, mientras también añade sus propias caracteristicas.

Oh, por cierto, ha sido creado para un projecto para el instituto, así que a menos que de alguna manera se vuelva muy usado, probablemente no lo seguiré actualizando después de su salida.

## ¿Como instalo NUTS?

Para empezar, necesitarás el lenguaje de programación Python, así que si todavía no lo tienes, [haz click aquí](https://www.python.org/) para ir a la web oficial.

A continuación, necesitarás las dependencias, que para tu suerte, solo necesitarás la versión de Python de Raylib. Así que puedes [hacer click aquí](https://electronstudio.github.io/raylib-python-cffi/README.html#installation) para ir a la documentación... o te puedes quedar aquí y ejecutar los siguientes comandos para ir más rápido, tu eliges.

Estos són los dos comandos a ejecutar:

```bash
python -m pip install setuptools
python -m pip install raylib
```

Y ahora que todas las dependencias están instaladas, es hora de installar NUTS!

Simplemente descarga el archivo de dentro del repositorio llamado [**nuts.py**](/nuts.py) y añadelo a la carpeta de tu juego. Sí, eso es todo.

## ¿Como empiezo a usar NUTS?

Bueno, para empezar, debes crear un archivo de Python separado ("main.py", "game.py"... simplemente asegurate que termine en ".py"). Asegurate de que "nuts.py" y tu archivo principal estén en el mismo directorio.

Ahora, vas a querer importar NUTS, para ello, simplemente añade la siguiente linea al inicio de tu código:

```python
import nuts
```

A continuación, vas a querer guardar tu juego como una variable, para ello, haz lo siguiente (recuerda cambiar los parametros):

```python
game = nuts.NutGame(960, 720, "Juego de NUTS")
```

Ahora tienes el juego, pero necesitas una escena para mostrarle contenido al jugador.

Tendrás que crear una nueva clase que extiende la clase NutScene y añadir todo lo que necesites:

```python
class TestScene(nuts.NutScene):
    def __init__(self):
        super().__init__()
        # Guarda los atributos de la escena aquí, recuerda usar self

    def onLoaded(self):
        print("¡La escena de prueba ha sido cargada!")
        # Se ejecutará cuando se cargue la escena
    
    def onUpdated(self):
        pass
        # Se ejecutará en cada frame

    def onKeyInput(self, key:nuts.NutKey, key_state:nuts.NutKeyState):
        pass
        # Se ejecutará cada vez que se pulse una tecla
```

Cada metodo dentro de la clase tiene sus funcionalidades:
* **init()**: Todo dentro de él se ejecutará incluso antes de que se cargue la escena. Se usa para guardar atributos y valores.
* **onLoaded()**: Se ejecutará cuando la función `game.loadScene()` se ejecuté con esta escena.
* **onUpdated()**: se ejecutará cada frame, y por lo tanto todo el tiempo, permitiendote hacer cambios constantes.
* **onKeyInput(key, key_state)**: Se ejecutará cada vez que el usuario pulse una tecla, el parametro `key` contiene la tecla pulsada, mientras que el parametro `key_state` indica si la tecla ha sido pulsada, mantenida o soltada.

Ahora tenemos una escena a mostar, así que para acabar, debemos hacer que el juego la muestre y finalmente ejecutarlo.

Para ello, añadirás las siguientes lineas.

```python
game.loadScene(TestScene())
game.start()
```

Y así nuestro primer proyecto de NUTS ha empezado, aquí esta el código completo en caso de que seas perezoso y solo quieras copiar y pegar:

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