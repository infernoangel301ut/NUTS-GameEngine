# NUTS Game Engine

If you wish to read this document in English, [click here](/README.md).

## ¿Qué es NUTS?

¡Estos NUTS! ¡Jaja!

... joder, ese chiste quedaba mejor en inglés. Bueno, volviendo al tema:

NUTS es un motor de videojuegos cuyo único propósito es darle libertad absoluta al desarrollador que este empleándolo:

Todo es modificable, todo es utilizable, ***todo está permitido***.

Es más o menos como una anarquía para el desarrollo de videojuegos.

NUTS utiliza una estructura similar a [HaxeFlixel](https://haxeflixel.com/) y una estructura similar a nodos para los objetos (es decir, una estructura tipo jerarquía).

Emplea Python como su lenguaje de programación y a [Raylib](https://www.raylib.com/) como su base ([o al menos una versión de Python de este](https://electronstudio.github.io/raylib-python-cffi/)).

NUTS es, y siempre será de código abierto. Eres libre de modificar a NUTS para ajustarlo a tus gustos e incluso añadir características que no estén agregadas actualmente.

Simplemente, acuérdate de dar créditos al autor en caso de publicar una versión modificada de NUTS: infernoangel301 (yo, XD).

Ah, ¿el nombre? Si, no significa nada, simplemente pensé que el nombre NUTS sonaba gracioso.

## ¿Qué características se pueden encontrar en NUTS?

Está planeado que NUTS tenga la mayor cantidad de opciones posibles para cada cosa, así que si una característica no existe todavía, puedes sugerirla tú mismo/a para que se añada en el futuro.

En cuanto a las que ya están añadidas:
* Dos formas para detectar inputs (`game.keyboard` o los eventos `onKeyInput` y `onMouseInput` de la escena).
* Cambiar el tamaño de la ventana de manera dinámica (la ventana se adapta al nuevo tamaño).
* Creación de objetos personalizados.
* Conversión entre tipos.
* Compatible con Raylib.
* ¡Y mucho más!

Actualmente, NUTS está en una etapa del desarrollo muy temprana, así que si encuentras algún bug, ¡por favor repórtalo en Github!

## ¿Cómo instalo NUTS?

De hecho, eso es bastante simple.

Primero, instala los módulos de Python necesarios:

```
pip install setuptools
pip install raylib
pip install PyInstaller
```

* setuptools: Dependencia de raylib.
* raylib: El módulo con el que trabaja NUTS.
* PyInstaller: Usado para exportar ([tutorial](https://imgur.com/FK8gPlc.png)).

La manera recomendada de hacerlo es descargando el archivo nuts.py de la sección de "Releases" de Github, desde la versión que quieras instalar.

La manera no recomendada de hacerlo es descargando el archivo [nuts.py](/nuts.py) del repositorio en sí (puedo haberme dejado algo sin revisar, de ahí que no este recomendado).

Para usar NUTS, simplemente crea un archivo de Python e importa el archivo de NUTS que has descargado.

```python
# Así
import nuts

# O así
from nuts import *
```

## ¿Cómo se usa NUTS?

Bueno, no lo voy a explicar a detalle, ya que para ello deberías comprobar los tutoriales, pero explicaré algunas cosas simples:

Primero crea una carpeta para tu proyecto, y después añade el archivo nuts.py que *probablemente* has instalado.

Después crea un archivo de Python por separado, y de ahí importa nuts, de la misma manera que se hace en el apartado de arriba.

El código principal deberia verse algo así:

```python
from nuts import *

game = NutGame(640, 480, "titulo epico") # Ancho, alto, y título de la ventana respectivamente.

class MainScene(NutScene):
    def onLoaded(self): # Se ejecuta una vez la escena se ha cargado.
        print("Malas NUTicias mi gente, malas NUTicias.")

    def onUpdated(self): # Se ejecuta en forma de bucle hasta que la escena ya no este presente.
        print("WAZAAAAAAAA")

game.loadScene(MainScene())
game.start()
```

Cabe añadir que también puedes crear una carpeta para meter todos los archivos para tu juego, y así mantenerlo todo organizado.

## ¿Cómo cojones se te ha ocurrido crear NUTS?

Bueno, en resumidas cuentas, se me ocurrió trabajar en NUTS debido a un proyecto para el instituto en el que tenemos que trabajar por todo el curso (me has oido bien, "tenemos", no "teniamos").

Inicialmente tuve unas cuantas ideas, pero decidi hacer un motor de juego, principalmente por que:

1. No es realmente un juego, así que en principio cuenta XD.
2. Ya todos hemos visto como se hace un juego, ¿pero y los motores que usan? Casi nunca recibimos una explicación sobre como funciona.

Durante el desarrollo, me estaba gustando bastante como estaba quedando, así que decidi que lo hiba a publicar de manera que cualquier persona pudiese usarlo, además de hacerle más actualizaciones.

A ver, ¿esperabas que un motor de juego llamado ***NUTS*** tuviese un trasfondo *emotivo*? XD.
