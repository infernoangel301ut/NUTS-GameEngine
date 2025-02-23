# Documentación de NUTS Game Engine

If you rather reading the documentation in English, [click here](/DOCUMENTATION/INDEX.md).

## Clase NutAnimationController

La clase que controla las animaciones para un sprite.

### metodo init (img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md))

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño de la imagen original para el sprite.

### Atributos

###### animations : dict[str, [NutAnimation](/DOCUMENTATION_Ñ/FILES/NUTANIMATION.md)]

Contiene todas las animaciones.

###### cur_anim : str

La animación que se está reproduciendo al momento.

###### anim_xml : XmlTree.Element | None

El archivo XML de la animación (para el sistema de animación de sparrow).

###### anim_type : [NutAnimationType](/DOCUMENTATION_Ñ/FILES/NUTANIMATIONTYPE.md)

El sistema de animación siendo usado al momento.

###### cur_frame : int

El frame siendo mostrado en la animación actual. Versión sin decimales de cur_frame_dec.

###### cur_frame_dec : float

La verdadera versión de cur_frame, con los decimales.

###### spritesheet_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md) | None

El tamaño de cada frame, usado para el sistema de animación de spritesheet.

###### img_size : [NutVector2](/DOCUMENTATION_Ñ/FILES/NUTVECTOR2.md)

El tamaño de la imagen original para el sprite.

###### anim_playing : bool

Si la animación se esta reproduciendo al momento o no.

### Metodos

#### setupSpritesheetAnimation(frame_width : int, frame_height : int) -> None

Prepara el sistema de animación de spritesheet.

###### frame_width : int

El largo de todos los frames.

###### frame_height : int

El alto de todos los frames.

#### setupSparrowAnimation(xml_file_dir : str) -> None

Prepara el sistema de animación de sparrow.

###### xml_file_dir : str

La carpeta del archivo XML.

#### makeSpritesheetAnimation(name : str, anim : list[int], reversed : bool = False, looped : bool = False, fps : int = 60) -> None

Crea una nueva animación para el sistema de spritesheet.

###### name : str

El nombre de la animación.

###### anim : list[int]

La lista de los frames a reproducir.

###### reversed : bool = False

Si la animación se reproducirá al revés o no.

###### looped : bool = False

Si la animación se repetirá o no.

###### fps : int = 60

La velocidad de la animación.

#### makeSparrowAnimation(name : str, anim_name : str, reversed : bool = False, looped : bool = False, fps : int = 60) -> None

Crea una nueva animación para el sistema de sparrow.

###### name : str

El nombre de la animación.

###### anim_name : str

El nombre de la animación en el archivo XML.

###### reversed : bool = False

Si la animación se reproducirá al revés o no.

###### looped : bool = False

Si la animación se repetirá o no.

###### fps : int = 60

La velocidad de la animación.

#### playAnimation(anin_name : str) -> None

Reproduce una animación.

###### anim_name : str

El nombre de la animación que quieres reproducir.

#### pause(unpause : bool | None = None) -> None

Pausa o continua una animación.

###### unpause : bool | None = None

Si la animación deberia ser pausada o continuada.

Si el valor es None, simplemente se cambiará al contrario.

#### stop() -> None

Detiene la animación.

#### isAnimated() -> bool

Regresa si hay una animación o no.
