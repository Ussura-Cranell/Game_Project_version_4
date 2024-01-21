import math
from enum import Enum, auto
from typing import Tuple


class SoundId(Enum):

    SELECTED_BUTTON = auto()
    ENTERED_BUTTON = auto()

    ERROR = auto()
    TEST1 = auto()
    TEST2 = auto()

    Memphis_Cult9Mm = auto()
    SOUND_PLAYER_STEP = auto()

    SOUND_DIALOG = auto()

    COVERING = auto()

class SoundStorage:
    _sound_storage = None
    _initialized = False

    def __new__(cls):
        if not cls._sound_storage:
            cls._sound_storage = super(SoundStorage, cls).__new__(cls)
        return cls._sound_storage

    def __init__(self):
        if SoundStorage._initialized: return None
        self._sounds = {}
        SoundStorage._initialized = True

    def add_sound(self, sound_id: SoundId, sound):

        # print(f'edded {SoundId, sound}')
        self._sounds[sound_id] = sound

    def get_sound(self, sound_id):
        return self._sounds.get(sound_id)

    def __str__(self):
        line = str()
        line += f'SoundStorage values:\n'
        for key in self._sounds.keys():
            line += f'"{key.name}" {self._sounds.get(key)}\n'
        return line

    def reset(self):
        # pass
        self._sounds = {}

class Sound:

    _sound_storage = SoundStorage()

    def __init__(self, sound_id: SoundId, sound_file, loops: int, target_coordinates, sound_coordinates, max_distance: int):
        import pygame
        self._sound = pygame.mixer.Sound(sound_file)
        self._loops = loops
        self._target_coordinates = target_coordinates
        self._sound_coordinates = sound_coordinates
        self._max_distance = max_distance
        self._sound_id = sound_id

        Sound._sound_storage.add_sound(sound_id, self)

    @property
    def sound(self):
        return self._sound

    @property
    def loops(self):
        return self._loops

    @property
    def target_coordinates(self):
        return self._target_coordinates

    @property
    def sound_coordinates(self):
        return self._sound_coordinates

    @property
    def max_distance(self):
        return self._max_distance

    @property
    def sound_id(self):
        return self._sound_id

    def set_target_coordinates(self, target_coordinates: Tuple[int, int]):
        self._target_coordinates = target_coordinates

    def set_sound_coordinates(self, sound_coordinates: Tuple[int, int]):
        self._sound_coordinates = sound_coordinates

    def set_max_distance(self, max_distance: Tuple[int, int]):
        self._max_distance = max_distance

    @classmethod
    def stereo_sound(cls, target_pos, sound_pos, max_distance):
        target_x, target_y = target_pos
        sound_x, sound_y = sound_pos
        distance = math.sqrt((target_x - sound_x) ** 2 + (target_y - sound_y) ** 2)
        angle = math.atan2(target_y - sound_y, target_x - sound_x)
        left_volume = 0
        right_volume = 0
        if distance < max_distance:
            volume = 1 - distance / max_distance
            left_volume = volume * (1 + math.cos(angle)) / 2
            right_volume = volume * (1 - math.cos(angle)) / 2
        return left_volume, right_volume

    def __str__(self):
        return f'Sound:[sound:{self._sound},target_coordinates:{self._target_coordinates},sound_coordinates:{self._sound_coordinates}]'



