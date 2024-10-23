import pyray
import math
import xml.etree.ElementTree as XmlTree
from enum import IntEnum

def extend_zeros(num:str, amount:int) -> str:
    "Function made for XML animation help."
    while len(num) < amount: num = "0" + num
    return num

def find_xml_element_by_name_atr(xml_root:XmlTree.Element, name:str) -> XmlTree.Element | None:
    "Function made for XML animation help."
    for anim in xml_root:
        if anim.get("name") == name: return anim
    return None

class NutKey(IntEnum):
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
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2

class NutKeyState(IntEnum):
    PRESSED = 0
    JUST_PRESSED = 1
    JUST_RELEASED = 2
    RELEASED = 3

class NutAnimationType(IntEnum):
    NO_ANIMATION = -1
    SPRITESHEET = 0
    SPARROW = 1

class NutAudioProperty(IntEnum):
    VOLUME = 0
    PITCH = 1
    PAN = 2

class NutVector2:
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y

    def __add__(self, other:"NutVector2"): return NutVector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other:"NutVector2"): return NutVector2(self.x - other.x, self.y - other.y)

    def __repr__(self): return f"({self.x} , {self.y})"

class NutColor:
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
    
    def __str__(self) -> str:
        return f"r = {self.r}; g = {self.g}; b = {self.b}; a = {self.a};"
    
class NutObject:
    def __init__(self, position:NutVector2 = NutVector2()):
        self.children:dict[str, NutObject] = {}
        self.position:NutVector2 = position
    
    def render(self, globalPos:NutVector2) -> None:
        for i in self.children.values():
            i.render(self.position + globalPos)

    def centerX(self) -> None: self.position.x = pyray.get_screen_width() / 2
    def centerY(self) -> None: self.position.y = pyray.get_screen_height() / 2

class NutRect(NutObject):
    def __init__(self, position:NutVector2, size:NutVector2, color:NutColor):
        super().__init__(position)
        self.size:NutVector2 = size
        self.color:NutColor = color
        self.angle:float = 0

    def render(self, globalPos:NutVector2) -> None:
        pyray.draw_rectangle_pro(
            pyray.Rectangle(
                int(self.position.x + globalPos.x + self.size.x/2),
                int(self.position.y + globalPos.y + self.size.y/2),
                int(self.size.x),
                int(self.size.y)
            ), pyray.Vector2(self.size.x/2, self.size.y/2), self.angle, self.color.toRaylibColor()
        )
        super().render(globalPos)

    def centerX(self) -> None: self.position.x = (pyray.get_screen_width() - self.size.x) / 2
    def centerY(self) -> None: self.position.y = (pyray.get_screen_height() - self.size.y) / 2

class NutFrame:
    def __init__(self, img_position:NutVector2, img_size:NutVector2, offset:NutVector2 | None = None, size_offset:NutVector2 | None = None):
        self.img_position = img_position
        self.img_size = img_size
        self.offset = offset if offset != None else NutVector2()
        self.size_offset = size_offset if size_offset != None else self.img_size

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
        count = 0
        anim_element = find_xml_element_by_name_atr(self.anim_xml, anim_name + extend_zeros(str(count), 4))

        while anim_element != None:
            anim_object.frames.append(NutFrame(
                NutVector2(int(anim_element.get("x")), int(anim_element.get("y"))),
                NutVector2(int(anim_element.get("width")), int(anim_element.get("height"))),
                NutVector2(int(anim_element.get("frameX", "0")), int(anim_element.get("frameY", "0"))),
                NutVector2(int(anim_element.get("frameWidth", anim_element.get("width"))), int(anim_element.get("frameHeight", anim_element.get("height"))))
            ))
            count += 1
            anim_element = find_xml_element_by_name_atr(self.anim_xml, anim_name + extend_zeros(str(count), 4))
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
        self.angle = 0
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
    
    def render(self, globalPos:NutVector2):
        if self.animation.isAnimated() and len(self.animation.cur_anim) != 0:
            cur_anim = self.animation.animations[self.animation.cur_anim]
            cur_frame = cur_anim.frames[self.animation.cur_frame] if not cur_anim.reversed else cur_anim.frames[::-1][self.animation.cur_frame]
            r_size = NutVector2(math.floor(cur_frame.img_size.x * self.scale.x), math.floor(cur_frame.img_size.y * self.scale.y))
            pyray.draw_texture_pro(
                self.display_image,
                pyray.Rectangle(
                    cur_frame.img_position.x if not self.flipX else self.display_image.width - cur_frame.img_position.x - cur_frame.img_size.x,
                    cur_frame.img_position.y if not self.flipY else self.display_image.height - cur_frame.img_position.y - cur_frame.img_size.y,
                    cur_frame.img_size.x, cur_frame.img_size.y
                ),
                pyray.Rectangle(self.position.x + globalPos.x + r_size.x/2 - cur_frame.offset.x, self.position.y + globalPos.y + r_size.y/2 - cur_frame.offset.y, r_size.x, r_size.y),
                pyray.Vector2(r_size.x/2, r_size.y/2), self.angle, self.color.toRaylibColor()
            )
            window_fps = pyray.get_fps()
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
        super().render(globalPos)

    def centerX(self) -> None: self.position.x = (pyray.get_screen_width() - self.size.x) / 2
    def centerY(self) -> None: self.position.y = (pyray.get_screen_height() - self.size.y) / 2

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

# Will add soon too
"""
class NutText:
    def __init__(self):
        pass
"""

class NutScene(NutObject):
    def __init__(self):
        super().__init__()
        self.bgColor = NutColor(0, 0, 0)

    def render(self) -> None:
        pyray.clear_background(self.bgColor.toRaylibColor())
        super().render(self.position)
    
    def onLoaded(self) -> None: pass
    def onUpdated(self) -> None: pass
    def onUpdatedPost(self) -> None: pass
    def onUnloaded(self) -> None: pass
    def onKeyInput(self, key:NutKey, state:NutKeyState) -> None: pass
    def onMouseInput(self, action:NutMouseAction, state:NutKeyState, position:NutVector2) -> None: pass

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

class NutGame:
    def __init__(self, winWidth:float, winHeight:float, title:str, fps:int = 60):
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.title = title
        self.fps = fps
        self.curScene = NutScene()
        self.keyboard = NutKeyboard()
        self.audioManager = NutAudioManager()
        self.awaitingLoad = False

    def loadScene(self, scene:NutScene) -> None:
        self.curScene.onUnloaded()
        self.curScene = scene
        self.awaitingLoad = True
    
    def reloadScene(self) -> None: self.loadScene(self.curScene)

    def start(self) -> None:
        pyray.init_window(math.floor(self.winWidth), math.floor(self.winHeight), self.title)
        pyray.init_audio_device()
        pyray.set_target_fps(self.fps)

        while not pyray.window_should_close():
            if self.awaitingLoad:
                self.awaitingLoad = False
                self.audioManager.unloadAllCurrentAudios()
                self.curScene.onLoaded()
            self.curScene.onUpdated()

            self.keyboard.update(self.curScene)
            self.audioManager.updateAllAudios()

            pyray.begin_drawing()
            self.curScene.render()
            pyray.end_drawing()
            
            self.curScene.onUpdatedPost()

        self.audioManager.unloadAllCurrentAudios()
        pyray.close_audio_device()
        pyray.close_window()
