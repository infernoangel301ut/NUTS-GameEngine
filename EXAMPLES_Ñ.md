> [!IMPORTANT]
> A pesar de estar traducido, se requiere saber hablar inglés debido a ciertos términos y por el hecho de que NUTS en sí, a la hora de emplearlo, está en inglés. Tenlo en cuenta.

# Ejemplos de código de NUTS Game Engine

Este documento cubre aspectos generales de NUTS, con tal de hacerse una idea de como usarlo.

## Indice

* [1 - Plantilla de código](#1---plantilla-de-código)
* [2A - Detectando inputs](#2a---detectando-inputs)
* [2B - Detectando inputs (ALTERNATIVA)](#2b---detectando-inputs-alternativa)
* [3 - Cambiando entre escenas](#3---cambiando-entre-escenas)
* [4 - Creando un objeto](#4---creando-un-objeto)
* [5A - Sprites animados (SISTEMA SPRITESHEET)](#5a---sprites-animados-sistema-spritesheet)
* [5B - Sprites animados (SISTEMA SPARROW)](#5b---sprites-animados-sistema-sparrow)
* [6 - Temporizadores](#6---temporizadores)
* [7 - Transiciones](#7---transiciones)
* [8 - Reproduciendo audio](#8---reproduciendo-audio)
* [9 - Archivos de guardado](#9---archivos-de-guardado)

## 1 - Plantilla de código

```python
from nuts import *

game = NutGame(1280, 720, "game title") # Ancho de la ventana, altura de la ventana y título de la ventana respectivamente.

class MainScene(NutScene): # La clase de la escena
    def __init__(self): # Cuando el objeto de la escena es creado ...
        super().__init__() # Crea todos los atributos y métodos requeridos para una escena.
        # Crea aquí todos los atributos

    def onLoaded(self): # Cuando la escena es cargada usando game.loadScene() ...
        pass # Código a ejecutar (elimina "pass")

    def onUnloaded(self): # Cuando otra escena es cargada usando game.loadScene() ...
        pass # Código a ejecutar (elimina "pass")

    def onUpdated(self, elapsed:float): # Cuando se carga el siguiente frame (antes de renderizar) ...
        pass # Código a ejecutar (elimina "pass")
        # elapsed : float -> Tiempo en segundos desde el último frame.

    def onUpdatedPost(self, elapsed:float): # Cuando se carga el siguiente frame (después de renderizar) ...
        pass # Código a ejecutar (elimina "pass")
        # elapsed : float -> Tiempo en segundos desde el último frame.

    def onKeyInput(self, key:NutKey, state:NutKeyState): # Cuando se detecte un input por parte del teclado ...
        pass # Código a ejecutar (elimina "pass")
        # key : NutKey -> La tecla detectada del input.
        # state : NutKeyState -> El estado en el que se encontró el input.
    
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2): # Cuando se detecte un input por parte del ratón ...
        pass # Código a ejecutar (elimina "pass")
        # action : NutMouseAction -> El botón del ratón detectado por el input.
        # state : NutKeyState -> El estado en el que se encontró el input.
        # position : NutVector2 -> La posición del ratón al momento del input.

game.loadScene(MainScene())
game.start()    
```

## 2A - Detectando inputs

```python
from nuts import *

game = NutGame(1280, 720, "game title")

class MainScene(NutScene):
    # El evento usado para detectar inputs del teclado.
    # key => La tecla que ha sido pulsada.
    # state => El estado en el que la tecla del input fue encontrada.
    def onKeyInput(self, key:NutKey, state:NutKeyState):
        pass # Ejecuta algo de código aquí XD

    # El evento usado para detectar inputs del ratón.
    # action => El botón del ratón que ha sido pulsado.
    # state => El estado en el que el botón del ratón del input fue encontrado.
    # position => La posición del ratón cuando se hizo el input.
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2):
        pass # Ejecuta algo de código aquí XD

game.loadScene(MainScene())
game.start()
```

## 2B - Detectando inputs (ALTERNATIVA)

```python
# Comprueba si una tecla específica (E en este caso) está en un estado específico (siendo pulsada ahora mismo, en este caso)
if game.keyboard.getKeyState(NutKey.E) == NutKeyState.JUST_PRESSED: pass

# Comprueba si un botón del ratón especifico (izquierda en este caso) está en un estado específico (siendo pulsada ahora mismo, en este caso)
if game.keyboard.getMouseState(NutMouseAction.LEFT) == NutKeyState.JUST_PRESSED: pass

# Printea la posición actual del ratón.
print(game.keyboard.getMousePosition())
```

## 3 - Cambiando entre escenas

```python
from nuts import *

game = NutGame(1280, 720, "game title")

class Scene1(NutScene):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(255, 0, 0) # Asigna el color de fondo de la escena a rojo.

    def onKeyInput(self, key:NutKey, state:NutKeyState):
        if state == NutKeyState.JUST_PRESSED and key == NutKey.Q:
            game.loadScene(Scene2()) # Cambia a la segunda escena.

class Scene2(NutScene):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(0, 0, 255) # Asigna el color de fondo de la escena a azul.

    def onKeyInput(self, key:NutKey, state:NutKeyState):
        if state == NutKeyState.JUST_PRESSED and key == NutKey.Q:
            game.loadScene(Scene1()) # Cambia a la primera escena.

game.loadScene(Scene1())
game.start()
```

## 4 - Creando un objeto

```python
# ... Dentro de una escena
self.children["objName"] = NutObject()

# El hijo de objName
self.children["objName"].children["subObj"] = NutObject()

# Puede ser cualquier tipo que extienda a NutObject (como NutSprite, NutRect, NutText, etc.)
```

## 5A - Sprites animados (SISTEMA SPRITESHEET)

```python
# Crea un NutSprite como de normal (donde el directorio de la imagen, añade el sprite de la imagen animada)
self.children["spr"] = NutSprite("image.png", NutVector2())
# Prepara el sistema de animación Spritesheet usando el ancho y el alto de cada frame como parámetros.
self.children["spr"].animation.setupSpritesheetAnimation(20, 30)
# Crea todas las animaciones así:
# - Primer parámetro : Nombre de la animación
# - Segundo parámetro : Todos los frames en orden (de izquierda a derecha, arriba a abajo).
# - Tercer parámetro : Si la animación está en reversa o no.
# - Cuarto parámetro : Si la animación está en bucle o no.
# - Quinto parámetro : Los frames por segundo a los que se ejecutará la animación (no es lo mismo que los FPS del juego).
self.children["spr"].animation.makeSpritesheetAnimation("anim name", [0, 1, 2, 3, 4], False, True, 60)
# Reproduce la animación usando su nombre.
self.children["spr"].animation.playAnimation("anim name")
```

## 5B - Sprites animados (SISTEMA SPARROW)

El sistema de animación Sparrow necesita un archivo PNG y un archivo XML.

Ambos pueden ser generados usando Adobe Animate (o también puedes usar otros programas).

```python
# Crea un NutSprite como de normal (donde el directorio de la imagen, añade el sprite de la imagen animada)
self.children["spr"] = NutSprite("image.png", NutVector2())
# Prepara el sistema de animación Sparrow usando el archivo XML como parámetro.
self.children["spr"].animation.setupSparrowAnimation("image.xml")
# Crea todas las animaciones así:
# - Primer parámetro : Nombre de la animación
# - Segundo parámetro : El nombre de la animación dentro del archivo XML.
# - Tercer parámetro : Si la animación está en reversa o no.
# - Cuarto parámetro : Si la animación está en bucle o no.
# - Quinto parámetro : Los frames por segundo a los que se ejecutará la animación (no es lo mismo que los FPS del juego).
self.children["spr"].animation.makeSparrowAnimation("anim name", "anim", False, True, 60)
# Reproduce la animación usando su nombre.
self.children["spr"].animation.playAnimation("anim name")
```

## 6 - Temporizadores

```python
# Primer parámetro : Tiempo que le toma al temporizador terminar en segundos.
# Segundo parámetro : La cantidad de veces que se ejecutará el temporizador.
#       Si el valor es negativo, el temporizador se ejecutará infinitamente.
self.children["tmr"] = NutTimer(10, -1)

# Evento del temporizador
def event(tmr:NutTimer): print("Hello world!")

# Por cada bucle acabado, la función previa se ejecutará.
self.children["tmr"].on_loop_completed = event

# Reproduce el temporizador.
self.children["tmr"].play()
```

## 7 - Transiciones

(¡¡¡REVISA [NutTweenEase](/DOCUMENTATION_Ñ/FILES/NUTTWEENEASE.md) EN LA DOCUMENTACIÓN!!!)

```python
# El objeto a transicionar (si no, como vas a transicionar)
self.children["rect"] = NutRect(NutVector2(100, 100), NutVector2(100, 100), NutColor(255, 0, 0))

# La transición debe ser un hijo del objeto que quieres transicionar.
# - Primer parámetro : El atributo a transicionar.
# - Segundo parámetro : El valor al que transicionar.
# - Tercer parámetro : El tiempo que le toma a la transición acabar.
# - Cuarto parámetro : La función que seguirá la transición.
self.children["rect"].children["tween"] = NutTween("color", NutColor(0, 0, 255), 3, NutTweenEase.quadOut)

# Reproduce la transición.
self.children["rect"].children["tween"].play()
```

## 8 - Reproduciendo audio

```python
# Guarda audio en el manejador de audio
game.audioManager.storeAudio(
    # Guarda un audio:
    # - Parámetro 1 : El directorio del audio.
    # - Parámetro 2 : Si el audio debería ir en bucle o no.
    # - Parámetro 3 : El volumen.
    # - Parámetro 4 : El modificador de tono.
    NutMusic("song.ogg", True, 0.5, 1),
    # El nombre con el que se guardará el audio
    "music"
)

# Reproduce el audio
# - Parámetro 1 : Si el audio es un NutSound (True) o un NutMusic (False)
# - Parámetro 2 : El nombre con el que se guardó el audio.
game.audioManager.playAudio(False, "music")
```

## 9 - Archivos de guardado

```python
# Almacena el archivo de guardado llamado "main" en la carpeta "saves"
game.addSaveFile(NutSaveFile("saves", "main"))

# Si el archivo de guardado previo existe...
if game.saveFileExists("saves", "main"):
    # Entonces carga todos sus contenidos.
    game.saveFiles["main"].loadFile()
else:
    # Si no, crea todas las propiedades de guardado tú mismo/a.
    game.saveFiles["main"].setProperty(
        # Donde "test" es el nombre del valor
        # int es el tipo de valor (también puedes usar otros tipos)
        # y 9 es el valor en sí
        NutSaveProperty("test", int, 9)
    )

# Modificando un valor de guardado:
game.saveFiles["main"].properties["test"].val.value = 15

# Guardando los cambios del archivo de guardado.
game.saveFiles["main"].saveFile()
```