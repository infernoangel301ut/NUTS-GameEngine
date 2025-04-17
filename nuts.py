import pyray
import math
import xml.etree.ElementTree as XmlTree
from enum import IntEnum
from typing import Callable
import os
import builtins

# NUTS version info
version:str = "0.1.0"
is_early_version:bool = True

view_width = 640
view_height = 480 # Both of these are by default, but get changed with NutGame

def extend_zeros(num:str, amount:int) -> str:
    """
    Function made for XML animation help.
    
    Returns `num` extended to have as many 0s in the left in order to have `amount` number of digits.
    """
    while len(num) < amount: num = "0" + num
    return num

def find_xml_elements_by_name_atr(xml_root:XmlTree.Element, name:str) -> list[XmlTree.Element] | None:
    """
    Function made for XML animation help.
    
    Returns the XML elements containing the name element called `name` or None if not found.
    """
    vals:dict[int, XmlTree.Element] = {}
    for anim in xml_root:
        val = anim.get("name")
        num = val[len(val)-4:]
        try: num = int(num)
        except: continue

        if val[:len(val)-4] == name: vals[num] = anim
    
    if len(vals) == 0: return None

    def element_sort(x):
        try: v = list(vals.values()).index(x)
        except ValueError: return -999
        return list(vals.keys())[v]
    
    res = list(vals.values())
    res.sort(key=element_sort)

    return res

class NutKey(IntEnum):
    """
    Enum that contains all keyboard keys.

    (Might have kind of stolen this from raylib's code lol)
    """
    NULL = 0
    APOSTROPHE = 39
    COMMA = 44
    MINUS = 45
    PERIOD = 46
    SLASH = 47
    ZERO = 48
    ONE = 49
    TWO = 50
    THREE = 51
    FOUR = 52
    FIVE = 53
    SIX = 54
    SEVEN = 55
    EIGHT = 56
    NINE = 57
    SEMICOLON = 59
    EQUAL = 61
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    LEFT_BRACKET = 91
    BACKSLASH = 92
    RIGHT_BRACKET = 93
    GRAVE = 96
    SPACE = 32
    ESCAPE = 256
    ENTER = 257
    TAB = 258
    BACKSPACE = 259
    INSERT = 260
    DELETE = 261
    RIGHT = 262
    LEFT = 263
    DOWN = 264
    UP = 265
    PAGE_UP = 266
    PAGE_DOWN = 267
    HOME = 268
    END = 269
    CAPS_LOCK = 280
    SCROLL_LOCK = 281
    NUM_LOCK = 282
    PRINT_SCREEN = 283
    PAUSE = 284
    F1 = 290
    F2 = 291
    F3 = 292
    F4 = 293
    F5 = 294
    F6 = 295
    F7 = 296
    F8 = 297
    F9 = 298
    F10 = 299
    F11 = 300
    F12 = 301
    LEFT_SHIFT = 340
    LEFT_CONTROL = 341
    LEFT_ALT = 342
    LEFT_SUPER = 343
    RIGHT_SHIFT = 344
    RIGHT_CONTROL = 345
    RIGHT_ALT = 346
    RIGHT_SUPER = 347
    KB_MENU = 348
    NUMPAD_ZERO = 320
    NUMPAD_ONE = 321
    NUMPAD_TWO = 322
    NUMPAD_THREE = 323
    NUMPAD_FOUR = 324
    NUMPAD_FIVE = 325
    NUMPAD_SIX = 326
    NUMPAD_SEVEN = 327
    NUMPAD_EIGHT = 328
    NUMPAD_NINE = 329
    NUMPAD_DECIMAL = 330
    NUMPAD_DIVIDE = 331
    NUMPAD_MULTIPLY = 332
    NUMPAD_SUBTRACT = 333
    NUMPAD_ADD = 334
    NUMPAD_ENTER = 335
    NUMPAD_EQUAL = 336
    BACK = 4
    MENU = 82
    VOLUME_UP = 24
    VOLUME_DOWN = 25

class NutMouseAction(IntEnum):
    """
    Enum that contains the buttons you can press with a mouse.
    """
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2

class NutKeyState(IntEnum):
    """
    Enum that contains the possible states a key or mouse button can be in.
    """
    PRESSED = 0
    JUST_PRESSED = 1
    JUST_RELEASED = 2
    RELEASED = 3

class NutAnimationType(IntEnum):
    """
    Enum that contains the animation techniques used for sprites.
    """
    NO_ANIMATION = -1
    SPRITESHEET = 0
    SPARROW = 1

class NutLogType(IntEnum):
    """
    Enum that contains the types when logging (using `NutLogger`).
    """
    INFO = 0
    WARNING = 1
    ERROR = 2

class NutLogger:
    """
    Object used for fancy printing lmao
    """
    def __init__(self, log_name:str):
        self.log_name = log_name

    def log(self, message, log_type:NutLogType = NutLogType.INFO):
        log_type_str = ("INFO" if log_type == NutLogType.INFO else "ERROR") if log_type != NutLogType.WARNING else "WARNING"
        print(f"({self.log_name}) : <{log_type_str}> -> {message}")

nuts_default_logger = NutLogger("NUTS")

class NutVector2:
    """
    General two-dimensional value.
    
    I could use complex numbers instead but that's for NERDS.
    """
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y

    def __add__(self, other:"NutVector2"): return NutVector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other:"NutVector2"): return NutVector2(self.x - other.x, self.y - other.y)

    def __repr__(self): return f"({self.x} , {self.y})"

    def toRaylibVector2(self) -> pyray.Vector2: return pyray.Vector2(self.x, self.y)
    @staticmethod
    def convert(x:type[pyray.Vector2] | list | tuple):
        return NutVector2(x.x, x.y) if type(x) not in (list, tuple) else NutVector2(x[0], x[1])

class NutColor:
    """
    Color value.
    """
    def __init__(self, r:int, g:int, b:int, a:int=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def toRaylibColor(self) -> pyray.Color: return pyray.Color(self.r, self.g, self.b, self.a)

    @staticmethod
    def fromFloatRGB(r:float, g:float, b:float, a:float = 1) -> "NutColor":
        return NutColor(math.floor(r*255), math.floor(g*255), math.floor(b*255), math.floor(a*255))
    
    @staticmethod
    def fromHex(hexadecimal:str) -> "NutColor":
        return NutColor(int(hexadecimal[:2], 16), int(hexadecimal[2:4], 16), int(hexadecimal[4:6], 16),
                        int(hexadecimal[6:], 16) if len(hexadecimal) > 6 else 255)
    
    @staticmethod
    def convert(x:type[pyray.Color] | list | tuple | int):
        if type(x) == pyray.Color: return NutColor(x.r, x.g, x.b, x.a)
        elif type(x) == int: return NutColor.fromHex(extend_zeros(hex(x), 6 if len(hex(x)) <= 6 else 8))
        else: return NutColor(x[0], x[1], x[2], x[3])
    
    def __str__(self) -> str:
        return f"r = {self.r}; g = {self.g}; b = {self.b}; a = {self.a};"
    
any_numeric_value = int | float | NutVector2 | NutColor # For tweens

class NutTweenEase:
    # ** = Power
    # x**0.5 = sqrt(x) (square root, learn exponential properties lol)

    # Desmos url with all these tweens being displayed:
    # https://www.desmos.com/calculator/p6zalcgjl0
    @staticmethod
    def linear(x:float): return x

    @staticmethod
    def quadIn(x:float): return x*x

    @staticmethod
    def quadOut(x:float): return -(x*x) + 2*x

    @staticmethod
    def quadBoth(x:float): return 2*x*x if x <= 0.5 else 2*(-(x*x) + 2*x) - 1

    @staticmethod
    def sineIn(x:float): return -math.sin((math.pi*x + math.pi)/2) + 1

    @staticmethod
    def sineOut(x:float): return math.sin((math.pi*x)/2)

    @staticmethod
    def sineBoth(x:float): return (math.sin(math.pi*x - math.pi/2)+1)/2

    @staticmethod
    def expoIn(x:float): return 2**(10*(x-1))

    @staticmethod
    def expoOut(x:float): return -(2**(-10*x))+1

    @staticmethod
    def expoBoth(x:float): return (2**(10*(x*2-1)))/2 if x <= 0.5 else (-(2**(-10*(2*x-1)))+2)/2

    @staticmethod
    def circOut(x:float): return x**0.5

    @staticmethod
    def circIn(x:float): return x**1.5

    @staticmethod
    def circBoth(x:float): return ((2*x)**0.5)/2 if x <= 0.5 else (2*(x**3) + 2)**0.5 - 1
    
class NutObject:
    """
    Main object class for NUTS.
    
    Used for pretty much everything: NutScene, NutSprite, NutRect, NutText, etc.
    """
    def __init__(self, position:NutVector2 = NutVector2()):
        self.children:dict[str, NutObject] = {}
        self.position:NutVector2 = position
    
    def render(self, globalPos:NutVector2, parent:"NutObject | None", paused:bool) -> None:
        for i in self.children.values():
            if type(i) == NutTween: 
                if i.cur_val != None:
                    item = self
                    if len(i.attribute_to_change) > 1:
                        for j in i.attribute_to_change[:len(i.attribute_to_change)-1]: item = item.__getattribute__(j)
                    if i.playing: item.__setattr__(i.attribute_to_change[len(i.attribute_to_change)-1], i.cur_val)
            i.render(self.position + globalPos, self, paused)

    def centerX(self) -> None: self.position.x = view_width / 2
    def centerY(self) -> None: self.position.y = view_height / 2
    def center(self) -> None:
        self.centerX()
        self.centerY()

class NutRect(NutObject):
    def __init__(self, position:NutVector2, size:NutVector2, color:NutColor):
        super().__init__(position)
        self.size:NutVector2 = size
        self.color:NutColor = color
        self.angle:float = 0

    def render(self, globalPos:NutVector2, parent:"NutObject | None", paused:bool) -> None:
        pyray.draw_rectangle_pro(
            pyray.Rectangle(
                int(self.position.x + globalPos.x + self.size.x/2),
                int(self.position.y + globalPos.y + self.size.y/2),
                int(self.size.x),
                int(self.size.y)
            ), pyray.Vector2(self.size.x/2, self.size.y/2), self.angle, self.color.toRaylibColor()
        )
        super().render(globalPos, self, paused)

    def centerX(self) -> None: self.position.x = (view_width - self.size.x) / 2
    def centerY(self) -> None: self.position.y = (view_height - self.size.y) / 2

class NutFrame:
    def __init__(self, img_position:NutVector2, img_size:NutVector2, offset:NutVector2 | None = None, size_offset:NutVector2 | None = None, flipX:bool = False, flipY:bool = False, rotated:bool = False):
        self.img_position = img_position
        self.img_size = img_size
        self.offset = offset if offset != None else NutVector2()
        self.size_offset = size_offset if size_offset != None else self.img_size
        self.flipX = flipX
        self.flipY = flipY
        self.rotated = rotated

class NutAnimation:
    def __init__(self):
        self.frames:list[NutFrame] = []
        self.reversed:bool = False
        self.fps:int = 60
        self.looped:bool = False

class NutAnimationController:
    def __init__(self, img_size:NutVector2):
        self.animations:dict[str, NutAnimation] = {}
        self.cur_anim:str = ""
        self.anim_xml:XmlTree.Element | None = None
        self.anim_type:int = NutAnimationType.NO_ANIMATION
        self.cur_frame:int = 0
        self.cur_frame_dec:float = 0
        self.spritesheet_size:NutVector2 | None = None
        self.img_size:NutVector2 = img_size
        self.anim_playing:bool = False

    def setupSpritesheetAnimation(self, frame_width:int, frame_height:int):
        self.anim_type = 0
        self.spritesheet_size = NutVector2(frame_width, frame_height)

    def setupSparrowAnimation(self, xml_file_dir:str):
        self.anim_type = 1
        self.anim_xml = XmlTree.parse(xml_file_dir).getroot()

    def makeSpritesheetAnimation(self, name:str, anim:list[int], reversed:bool = False, looped:bool = False, fps:int = 60):
        if self.anim_type != 0: return
        if self.spritesheet_size == None: return

        anim_object = NutAnimation()
        anim_object.fps = fps
        anim_object.reversed = reversed
        anim_object.looped = looped
        for i in anim:
            anim_object.frames.append(NutFrame(
                NutVector2(
                    self.spritesheet_size.x * (i % (self.img_size.x // self.spritesheet_size.x)),
                    self.spritesheet_size.y * (i // (self.img_size.x // self.spritesheet_size.x))
                ),
                self.spritesheet_size
            ))
        self.animations[name] = anim_object

    def makeSparrowAnimation(self, name:str, anim_name:str, reversed:bool = False, looped:bool = False, fps:int = 60):
        if self.anim_type != 1: return
        if self.anim_xml == None: return

        anim_object = NutAnimation()
        anim_object.fps = fps
        anim_object.reversed = reversed
        anim_object.looped = looped
        anim_elements:list[XmlTree.Element] | None = find_xml_elements_by_name_atr(self.anim_xml, anim_name)

        if anim_elements == None:
            nuts_default_logger.log(f"Tried to make animation '{name}', but no '{anim_name}' was found.", NutLogType.ERROR)
            return

        for i in anim_elements:
            anim_object.frames.append(NutFrame(
                NutVector2(int(i.get("x")), int(i.get("y"))),
                NutVector2(int(i.get("width")), int(i.get("height"))),
                NutVector2(int(i.get("frameX", "0")), int(i.get("frameY", "0"))),
                NutVector2(int(i.get("frameWidth", i.get("width"))), int(i.get("frameHeight", i.get("height")))),
                i.get("flipX", "false").lower() == "true", i.get("flipY", "false").lower() == "true",
                i.get("rotated", "false").lower() == "true", 
            ))
            self.animations[name] = anim_object

    def playAnimation(self, anim_name:str):
        if self.animations.get(anim_name) == None: return
        self.cur_frame = self.cur_frame_dec = 0
        self.cur_anim = anim_name
        self.anim_playing = True

    def pause(self, unpause:bool | None = None):
        self.anim_playing = (not self.anim_playing) if unpause == None else unpause

    def stop(self):
        self.anim_playing = False
        self.cur_frame = self.cur_frame_dec = 0

    def isAnimated(self) -> bool:
        return self.anim_type != NutAnimationType.NO_ANIMATION

class NutSprite(NutObject):
    def __init__(self, image_dir:str, position:NutVector2 = NutVector2(), size:NutVector2 = None):
        super().__init__(position)
        self.image_dir = image_dir
        self.image = pyray.load_texture(self.image_dir)
        self.display_image = self.image
        self.size = NutVector2(self.display_image.width, self.display_image.height) if size == None else size
        self.angle:float = 0
        self.color = NutColor(255, 255, 255)
        self.animation = NutAnimationController(NutVector2(self.image.width, self.image.height))
        self.scale = NutVector2(1, 1)
        self.flipX:bool = False
        self.flipY:bool = False

    def updateDisplay(self):
        self.image = pyray.load_texture(self.image_dir)
        self.display_image = self.image
        if self.flipX: self.display_image.width *= -1
        if self.flipY: self.display_image.height *= -1
    
    def render(self, globalPos:NutVector2, parent:"NutObject | None", paused:bool):
        if self.animation.isAnimated() and len(self.animation.cur_anim) != 0:
            cur_anim = self.animation.animations[self.animation.cur_anim]
            #print(cur_anim.frames)
            cur_frame = cur_anim.frames[self.animation.cur_frame] if not cur_anim.reversed else cur_anim.frames[::-1][self.animation.cur_frame]
            pyray.draw_texture_pro(
                self.display_image,
                pyray.Rectangle(
                    cur_frame.img_position.x if not (self.flipX ^ cur_frame.flipX) else self.image.width - cur_frame.img_position.x - cur_frame.img_size.x,
                    cur_frame.img_position.y if not (self.flipY ^ cur_frame.flipY) else self.image.height - cur_frame.img_position.y - cur_frame.img_size.y,
                    cur_frame.img_size.x, cur_frame.img_size.y
                ),
                pyray.Rectangle(
                    self.position.x - cur_frame.offset.x*self.scale.x,
                    self.position.y - (cur_frame.offset.y + (0 if not cur_frame.rotated else cur_frame.img_size.x))*self.scale.y,
                    cur_frame.img_size.x*self.scale.x,
                    cur_frame.img_size.y*self.scale.y
                ),
                pyray.Vector2(0, 0), self.angle if not cur_frame.rotated else self.angle - 90, self.color.toRaylibColor()
            )
            window_fps = pyray.get_fps() if not paused else 0
            if self.animation.anim_playing and window_fps != 0:
                self.animation.cur_frame_dec += (cur_anim.fps / window_fps)
                self.animation.cur_frame = math.floor(self.animation.cur_frame_dec)
                if self.animation.cur_frame >= len(cur_anim.frames):
                    if cur_anim.looped: self.animation.cur_frame_dec = self.animation.cur_frame = 0
                    else:
                        self.animation.cur_frame_dec = self.animation.cur_frame = len(cur_anim.frames)-1
                        self.animation.anim_playing = False
        else:
            r_size = NutVector2(math.floor(self.size.x * self.scale.x), math.floor(self.size.y * self.scale.y))
            pyray.draw_texture_pro(
                self.display_image,
                pyray.Rectangle(0, 0, self.display_image.width * (-1 if self.flipX else 1), self.display_image.height * (-1 if self.flipY else 1)),
                pyray.Rectangle(self.position.x + globalPos.x + r_size.x/2, self.position.y + globalPos.y + r_size.y/2, r_size.x, r_size.y),
                pyray.Vector2(r_size.x/2, r_size.y/2), self.angle, self.color.toRaylibColor()
            )
        super().render(globalPos, self, paused)

    def centerX(self) -> None: self.position.x = abs(view_width - self.size.x*self.scale.x) / 2
    def centerY(self) -> None: self.position.y = abs(view_height - self.size.y*self.scale.y) / 2

class NutSound:
    def __init__(self, path:str, volume:float = 0.5, pitch:float = 1):
        self.file_path = path
        self.raylib_audio:pyray.Sound = pyray.load_sound(self.file_path)
        self.volume = volume
        self.pitch = pitch
        self.paused = False
        self.playing = False
        self.pan = 0.5

        pyray.set_sound_volume(self.raylib_audio, self.volume)
        pyray.set_sound_pitch(self.raylib_audio, self.pitch)

class NutMusic:
    def __init__(self, path:str, looped:bool = False, volume:float = 0.5, pitch:float = 1):
        self.file_path = path
        self.raylib_audio:pyray.Music = pyray.load_music_stream(self.file_path)
        self.looped = looped
        self.volume = volume
        self.pitch = pitch
        self.paused = False
        self.playing = False
        self.pan = 0.5

        pyray.set_music_volume(self.raylib_audio, self.volume)
        pyray.set_music_pitch(self.raylib_audio, self.pitch)

class NutText(NutObject):
    def __init__(self, position:NutVector2, text:str, size:int, color:NutColor = NutColor(255, 255, 255)):
        super().__init__(position)
        self.text = text
        self.size = size
        self.font:str | None = None
        self.raylib_font:pyray.Font | None = None
        self.color = color
        self.spacing = 2
        self.angle:float = 0

    def loadFont(self, font_dir:str):
        self.font = font_dir
        self.raylib_font = pyray.load_font(self.font)

    def setDefaultFont(self):
        self.font = None
        self.raylib_font = None

    def render(self, globalPos:NutVector2, parent:"NutObject | None", paused:bool):
        font_check = self.raylib_font if self.raylib_font != None else pyray.get_font_default()
        center = pyray.measure_text_ex(font_check, self.text, self.size, self.spacing)
        center.x /= 2
        center.y /= 2

        pyray.draw_text_pro(
            font_check, self.text, pyray.Vector2(self.position.x + center.x, self.position.y + center.y),
            center, self.angle, self.size, self.spacing, self.color.toRaylibColor()
        )
        super().render(globalPos, self, paused)

    def centerX(self): self.position.x = (view_width - pyray.measure_text_ex(self.raylib_font if self.raylib_font != None else pyray.get_font_default(), self.text, self.size, self.spacing).x) / 2
    def centerY(self): self.position.y = (view_height - pyray.measure_text_ex(self.raylib_font if self.raylib_font != None else pyray.get_font_default(), self.text, self.size, self.spacing).y) / 2

class NutTimer(NutObject):
    def __init__(self, time:float, loops:int = 1):
        super().__init__()
        self.time = time
        self.loops = loops
        self.current_time:float = 0
        self.current_loops:int = 0
        self.playing:bool = False
        self.on_timer_completed:Callable = NutTimer.empty_timer_function
        self.on_loop_completed:Callable = NutTimer.empty_timer_function
        self.on_timer_update:Callable = NutTimer.empty_timer_function

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
        self.current_time = 0
        self.current_loops = 0

    def pause(self, paused:bool | None = None):
        self.playing = not self.playing if paused == None else paused

    def update(self):
        if not self.playing: return

        self.current_time += pyray.get_frame_time()
        self.on_timer_update(self)
        if self.current_time > self.time:
            self.on_loop_completed(self)
            self.current_loops += 1
            if self.current_loops == self.loops:
                self.on_timer_completed(self)
                self.stop()
            else:
                self.current_time = 0

    def render(self, globalPos: NutVector2, parent:"NutObject | None", paused:bool) -> None:
        if not paused: self.update()
        super().render(globalPos, self, paused)

    @staticmethod
    def empty_timer_function(timer:"NutTimer"): pass

class NutTween(NutTimer):
    def __init__(self, attribute_to_change:str, final_val:any_numeric_value, time:float, ease:Callable = NutTweenEase.linear):
        super().__init__(time)
        self.attribute_to_change:list[str] = attribute_to_change.split(".")
        self.final_val = final_val
        self.cur_val:any_numeric_value | None = None
        self.initial_val:any_numeric_value | None = None
        self.ease:Callable = ease
        self.progress:float = 0

    def get_attr_val(self, parent:NutObject) -> any_numeric_value:
        cur_val:any_numeric_value | None = None
        for i, v in enumerate(self.attribute_to_change):
            obj = cur_val if i != 0 else parent
            cur_val = obj.__getattribute__(v)

        return cur_val
    
    def update_progress(self): self.progress = max(min(1, self.ease(self.current_time/self.time)), 0)

    def play(self):
        self.initial_val = None # Fixes a bug where it would use the previous property value instead of the new one
        super().play()
    
    def stop(self):
        self.update_progress()
        if self.progress <= 0: self.cur_val = self.initial_val
        elif self.progress >= 1: self.cur_val = self.final_val
        self.initial_val = None
        super().stop()
    
    def render(self, globalPos: NutVector2, parent:"NutObject | None", paused:bool):
        if self.initial_val == None: self.initial_val = self.get_attr_val(parent)

        self.update_progress()

        if not self.playing: self.cur_val = self.get_attr_val(parent)
        else:
            if type(self.initial_val) == float: self.cur_val = self.initial_val + (self.final_val - self.initial_val) * self.progress
            elif type(self.initial_val) == int: self.cur_val = math.floor(self.initial_val + (self.final_val - self.initial_val) * self.progress)
            elif type(self.initial_val) == NutVector2: self.cur_val = self.initial_val + NutVector2((self.final_val.x - self.initial_val.x) * self.progress, (self.final_val.y - self.initial_val.y) * self.progress)
            elif type(self.initial_val) == NutColor:
                self.cur_val = NutColor(
                    math.floor(self.initial_val.r + (self.final_val.r - self.initial_val.r) * self.progress),
                    math.floor(self.initial_val.g + (self.final_val.g - self.initial_val.g) * self.progress),
                    math.floor(self.initial_val.b + (self.final_val.b - self.initial_val.b) * self.progress),
                    math.floor(self.initial_val.a + (self.final_val.a - self.initial_val.a) * self.progress)
                )
        super().render(globalPos, self, paused)

class NutCamera(NutObject):
    def __init__(self):
        super().__init__()
        self.angle:float = 0
        self.zoom:float = 1
        self.raylib_camera:pyray.Camera2D = pyray.Camera2D(
            pyray.Vector2(0, 0),
            self.position.toRaylibVector2(),
            self.angle,
            self.zoom
        )

    def render(self, globalPos: NutVector2, parent:"NutObject | None", paused:bool):
        self.raylib_camera.target = self.position.toRaylibVector2()
        self.raylib_camera.rotation = self.angle
        self.raylib_camera.zoom = self.zoom

        pyray.begin_mode_2d(self.raylib_camera)
        super().render(globalPos + self.position, self, paused)
        pyray.end_mode_2d()

class NutScene(NutObject):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(0, 0, 0)
        self.keepAudioOnUnload:bool = False
        self.update_paused:bool = False
        self.drawing_paused:bool = False

    def render(self, globalPos: NutVector2, parent:"NutObject | None", paused:bool) -> None:
        pyray.clear_background(self.bgColor.toRaylibColor())
        super().render(self.position + globalPos, self, paused or self.drawing_paused)
    
    def onLoaded(self) -> None: pass
    def onUpdated(self, elapsed:float) -> None: pass
    def onUpdatedPost(self, elapsed:float) -> None: pass
    def onUnloaded(self) -> None: pass
    def onKeyInput(self, key:NutKey, state:NutKeyState) -> None: pass
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2) -> None: pass

class NutSubScene(NutScene):
    def __init__(self, parentScene:NutScene, transarentBG:bool = True):
        super().__init__()
        self.parentScene = parentScene
        self.activated:bool = False
        self.awaitingLoad:bool = False
        self.awaitingUnload:bool = False
        self.bgColor.a = 63 if transarentBG else 255

    def render(self, globalPos: NutVector2, parent:"NutObject | None", paused:bool) -> None:
        if self.awaitingUnload:
            self.awaitingUnload = False
            self.onUnloaded()
            self.children.clear()
            # Clearing children because they will be created with the onLoaded method.
            # Which will also run when the NutSubScene gets activated.
        if self.activated:
            pyray.draw_rectangle(0, 0, pyray.get_render_width(), pyray.get_render_height(), self.bgColor.toRaylibColor())
            if self.awaitingLoad:
                self.awaitingLoad = False
                self.children.clear()
                self.onLoaded()
            if not self.update_paused: self.onUpdated(pyray.get_frame_time())
            super().render(self.position + globalPos, self, self.drawing_paused)
            if not self.update_paused: self.onUpdatedPost(pyray.get_frame_time())
        # unlike other objects, NutSubScene does not give a fuck whether its parent is paused
        # it only cares whether THEY are paused or not
        # this also applies for its scene methods

    def toggleActivate(self, value:bool | None = None):
        self.activated = value if value != None else not self.activated
        self.awaitingLoad = self.activated
        self.awaitingUnload = not self.activated

class NutKeyboard:
    def __init__(self):
        self.curHeldKeys:list[int] = []

    def getKeyState(self, key:NutKey) -> NutKeyState:
        if pyray.is_key_pressed(key): return NutKeyState.JUST_PRESSED
        if key in self.curHeldKeys: return NutKeyState.PRESSED
        if pyray.is_key_released(key): return NutKeyState.JUST_RELEASED
        return NutKeyState.RELEASED

    def getMouseState(self, action:NutMouseAction) -> NutKeyState:
        if pyray.is_mouse_button_pressed(action): return NutKeyState.JUST_PRESSED
        if pyray.is_mouse_button_down(action): return NutKeyState.PRESSED
        if pyray.is_mouse_button_released(action): return NutKeyState.JUST_RELEASED
        return NutKeyState.RELEASED

    def getMousePosition(self) -> NutVector2: return NutVector2(pyray.get_mouse_x(), pyray.get_mouse_y())
    
    def update(self, curState:NutScene) -> None:
        # Keyboard
        updatedHeldKeys:list[int] = []
        for i in self.curHeldKeys:
            if pyray.is_key_down(i):
                curState.onKeyInput(i, NutKeyState.PRESSED)
                updatedHeldKeys.append(i)
            else: curState.onKeyInput(i, NutKeyState.JUST_RELEASED)
        self.curHeldKeys = updatedHeldKeys

        justPressedKey = pyray.get_key_pressed()
        if justPressedKey != 0:
            curState.onKeyInput(justPressedKey, NutKeyState.JUST_PRESSED)
            self.curHeldKeys.append(justPressedKey)

        # Mouse
        mousePos = NutVector2(pyray.get_mouse_x(), pyray.get_mouse_y())
        for i in range(0, 3):
            if pyray.is_mouse_button_pressed(i): curState.onMouseInput(i, NutKeyState.JUST_PRESSED, mousePos)
            elif pyray.is_mouse_button_down(i): curState.onMouseInput(i, NutKeyState.PRESSED, mousePos)
            elif pyray.is_mouse_button_released(i): curState.onMouseInput(i, NutKeyState.JUST_RELEASED, mousePos)

        for v in curState.children.values():
            if type(v) != NutSubScene: continue
            if v.activated: self.update(v)

class NutAudioManager:
    def __init__(self):
        self.sounds:dict[str, NutSound] = {}
        self.music:dict[str, NutMusic] = {}

    def storeAudio(self, audio:NutSound | NutMusic, name:str):
        if type(audio) == NutSound:
            if self.sounds.get(name) != None:
                pyray.unload_sound(self.sounds[name].raylib_audio)
                self.sounds[name] = None
            self.sounds[name] = audio
        else:
            if self.music.get(name) != None:
                pyray.unload_music_stream(self.music[name].raylib_audio)
                self.music[name] = None
            self.music[name] = audio

    def playAudio(self, is_sound:bool, name:str):
        if is_sound:
            pyray.play_sound(self.sounds[name].raylib_audio)
            self.sounds[name].playing = True
        else:
            pyray.play_music_stream(self.music[name].raylib_audio)
            self.music[name].playing = True

    def pauseAudio(self, is_sound:bool, name:str, pause:bool | None = None):
        if is_sound:
            self.sounds[name].paused = (not self.sounds[name].paused) if pause == None else pause
            if self.sounds[name].paused: pyray.pause_sound(self.sounds[name].raylib_audio)
            else: pyray.resume_sound(self.sounds[name].raylib_audio)
        else:
            self.music[name].paused = (not self.music[name].paused) if pause == None else pause
            if self.music[name].paused: pyray.pause_music_stream(self.music[name].raylib_audio)
            else: pyray.resume_music_stream(self.music[name].raylib_audio)

    def stopAudio(self, is_sound:bool, name:str):
        if is_sound:
            pyray.stop_sound(self.sounds[name].raylib_audio)
            self.sounds[name].playing = False
        else:
            pyray.stop_music_stream(self.music[name].raylib_audio)
            self.music[name].playing = False

    def updateAllAudios(self):
        # Just updates music lol, sounds don't need to be updated
        for i, v in self.music.items():
            pyray.update_music_stream(v.raylib_audio)
            if pyray.get_music_time_played(v.raylib_audio) / pyray.get_music_time_length(v.raylib_audio) > 1:
                pyray.stop_music_stream(v.raylib_audio)
                if v.looped: pyray.play_audio_stream(v.raylib_audio)
                else: self.music[i].playing = False

    def unloadAllCurrentAudios(self):
        for i in self.music.values(): pyray.unload_music_stream(i.raylib_audio)
        for i in self.sounds.values(): pyray.unload_sound(i.raylib_audio)
        self.music = {}
        self.sounds = {}

class NutSaveValue:
    def __init__(self, value, value_type:type):
        self.value_type = value_type
        self.value = value

    def parseVal(self):
        if self.value_type not in (int, float, bool, str, NutVector2, NutColor):
            nuts_default_logger.log(f"Can't log value with type \"{self.value_type.__name__}\"")
            return ""
        if self.value_type == NutVector2: return f"{self.value.x},{self.value.y}"
        elif self.value_type == NutColor: return f"{self.value.r},{self.value.g},{self.value.b},{self.value.a}"
        return str(self.value)

class NutSaveProperty:
    def __init__(self, name:str, val_type:type, val):
        self.name = name
        self.val = NutSaveValue(val, val_type)

class NutSaveFile:
    def __init__(self, file_dir:str, file_name:str):
        self.file_dir = file_dir
        self.file_name = file_name
        self.properties:dict[str, NutSaveProperty] = {}

    def setProperty(self, property:NutSaveProperty):
        self.properties[property.name] = property

    def parsePropertiesAsStr(self) -> str | None:
        result = ""
        for i in self.properties.values(): result += f'"{i.name}" "{i.val.value_type.__name__}" "{i.val.parseVal()}"\n'
        return result

    def saveFile(self):
        file = open(self.file_dir + "/" + self.file_name + ".nutsave", "w")
        file.write(self.parsePropertiesAsStr())
        file.close()

    def loadFile(self):
        contents = open(self.file_dir + "/" + self.file_name + ".nutsave", "r").readlines()
        for i in contents:
            str_started = False
            vals:list[str] = []
            cur_val = ""
            for j in i:
                if j == '"':
                    str_started = not str_started
                    if not str_started:
                        vals.append(cur_val)
                        #print(cur_val)
                    cur_val = ""
                else:
                    if not str_started: continue
                    cur_val += j
            type_val = None
            try:
                type_val = getattr(builtins, vals[1])
            except:
                t = globals().get(vals[1])
                type_val = t if isinstance(t, type) else None
            
            if type_val == None: continue

            val_value = vals[2]
            if type_val in (NutVector2, NutColor):
                val_list = vals[2].split(",")
                if type_val == NutVector2: val_value = NutVector2(float(val_list[0]), float(val_list[1]))
                else: val_value = NutColor(int(val_list[0]), int(val_list[1]), int(val_list[2]), int(val_list[3]))
            else:
                if type_val == bool: val_value = vals[2] == "True"
                else: val_value = type_val(vals[2])

            self.setProperty(NutSaveProperty(vals[0], type_val, val_value))

class NutGame:
    def __init__(self, winWidth:float, winHeight:float, title:str, fps:int = 60):
        self.winWidth, self.viewWidth = winWidth, winWidth
        self.winHeight, self.viewHeight = winHeight, winHeight
        global view_width
        global view_height
        view_width = math.floor(self.viewWidth)
        view_height = math.floor(self.viewHeight)
        self.winPos:NutVector2 = NutVector2()
        self.title = title
        self.fps = fps
        self.curScene = NutScene()
        self.keyboard = NutKeyboard()
        self.audioManager = NutAudioManager()
        self.saveFiles:dict[str, NutSaveFile] = {}
        self.awaitingLoad = False
        self.gameShouldEnd:bool = False
        self.awaitingAudioClear:bool = False
        self.viewportCamera:pyray.Camera2D = pyray.Camera2D(pyray.Vector2(0, 0), pyray.Vector2(0, 0), 0, 1)
        self.resizable:bool = True
        self.fullscreen:bool = False
        self.was_fullscreen:bool = False
        self.shouldRestoreAfterFullscreen:bool = False
        self.borderless:bool = False
        self.was_borderless:bool = False
        self.allowsTransparency:bool = False
        self.viewBorderColor:NutColor = NutColor(0, 0, 0, 255)

    def saveFileExists(self, file_dir:str, file_name:str):
        return os.path.exists(file_dir + "/" + file_name + ".nutsave")

    def addSaveFile(self, save:NutSaveFile):
        self.saveFiles[save.file_name] = save

    def loadScene(self, scene:NutScene) -> None:
        self.curScene.onUnloaded()
        self.awaitingAudioClear = not self.curScene.keepAudioOnUnload
        self.curScene = scene
        self.awaitingLoad = True
    
    def reloadScene(self) -> None: self.loadScene(type(self.curScene)())

    def close(self): self.gameShouldEnd = True

    def updateWindowSize(self): pyray.set_window_size(self.winWidth, self.winHeight)
    def updateWindowPos(self): pyray.set_window_position(math.floor(self.winPos.x), math.floor(self.winPos.y))

    def updateWindowProperties(self):
        pyray.set_window_title(self.title)
        pyray.set_config_flags(
            (pyray.ConfigFlags.FLAG_WINDOW_RESIZABLE * self.resizable) |
            (pyray.ConfigFlags.FLAG_WINDOW_TRANSPARENT * self.allowsTransparency)
        )
        if self.borderless != self.was_borderless:
            pyray.toggle_borderless_windowed()
            self.was_borderless = self.borderless
            self.updateWindowSize()
            self.updateWindowPos()
        if self.fullscreen != self.was_fullscreen:
            if self.fullscreen:
                self.shouldRestoreAfterFullscreen = not pyray.is_window_maximized()
                pyray.maximize_window()
            pyray.toggle_fullscreen()
            if not self.fullscreen and self.shouldRestoreAfterFullscreen:
                pyray.restore_window()
                self.shouldRestoreAfterFullscreen = False
            self.was_fullscreen = self.fullscreen

    def start(self) -> None:
        self.updateWindowProperties()
        pyray.init_window(math.floor(self.winWidth), math.floor(self.winHeight), self.title)
        pyray.init_audio_device()
        pyray.set_target_fps(self.fps)

        nuts_default_logger.log(f"NUTS Game Engine v{version} has been initialized.")
        if is_early_version: nuts_default_logger.log("\n\tYou are using an early version of NUTS,\n\twhich means it may contain LOTS of bugs and glitches.\n\n\tPlease report them on the github page if you find any!\n\thttps://github.com/infernoangel301ut/NUTS-GameEngine", NutLogType.WARNING)

        self.winPos = NutVector2.convert(pyray.get_window_position())

        global view_width
        global view_height

        while not pyray.window_should_close():
            if self.awaitingLoad:
                self.awaitingLoad = False
                if self.awaitingAudioClear:
                    self.awaitingAudioClear = False
                    self.audioManager.unloadAllCurrentAudios()
                self.curScene.onLoaded()
            if not self.curScene.update_paused: self.curScene.onUpdated(pyray.get_frame_time())

            self.keyboard.update(self.curScene)
            if not self.curScene.update_paused: self.audioManager.updateAllAudios()

            view_width = math.floor(self.viewWidth)
            view_height = math.floor(self.viewHeight)

            pyray.begin_drawing()
            if pyray.get_window_position() != self.winPos.toRaylibVector2(): self.winPos = NutVector2.convert(pyray.get_window_position())
            # No raylib support for good window resizing? I don't fucking care, I'm making it myself.
            if pyray.is_window_resized():
                self.winWidth = pyray.get_render_width()
                self.winHeight = pyray.get_render_height()
                resizedViewWidth = self.viewWidth * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight)
                resizedViewHeight = self.viewHeight * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight)
                self.viewportCamera.offset = pyray.Vector2(
                    (self.winWidth - resizedViewWidth)/2,
                    (self.winHeight - resizedViewHeight)/2
                )
                self.viewportCamera.zoom = ((resizedViewWidth**2 + resizedViewHeight**2)**0.5)/((self.viewWidth**2 + self.viewHeight**2)**0.5)
            pyray.begin_mode_2d(self.viewportCamera)
            self.curScene.render(NutVector2(), None, False)
            pyray.end_mode_2d()
            # Left border
            pyray.draw_rectangle(
                0, 0, math.ceil((self.winWidth - self.viewWidth * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2),
                math.ceil(self.winHeight), self.viewBorderColor.toRaylibColor()
            )
            # Right border
            pyray.draw_rectangle(
                math.ceil(self.winWidth - (self.winWidth - self.viewWidth * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2), 0,
                math.ceil((self.winWidth - self.viewWidth * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2),
                math.ceil(self.winHeight), self.viewBorderColor.toRaylibColor()
            )
            # Top border
            pyray.draw_rectangle(
                0, 0, math.ceil(self.winWidth),
                math.ceil((self.winHeight - self.viewHeight * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2),
                self.viewBorderColor.toRaylibColor()
            )
            # Bottom border
            pyray.draw_rectangle(
                0, math.ceil(self.winHeight - (self.winHeight - self.viewHeight * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2),
                math.ceil(self.winWidth), math.ceil((self.winHeight - self.viewHeight * min(self.winWidth/self.viewWidth, self.winHeight/self.viewHeight))/2),
                self.viewBorderColor.toRaylibColor()
            )

            pyray.end_drawing()
            
            if not self.curScene.update_paused: self.curScene.onUpdatedPost(pyray.get_frame_time())

            if self.gameShouldEnd: break

        self.audioManager.unloadAllCurrentAudios()
        pyray.close_audio_device()
        pyray.close_window()
