from src.Game.Sound import Sound

import pygame

class SoundManager:
    _sound_manager = None
    _MAX_CHANNELS = 8

    def __new__(cls):
        if not cls._sound_manager:
            cls._sound_manager = super(SoundManager, cls).__new__(cls)
        return cls._sound_manager

    def __init__(self):
        pygame.mixer.init()

        pygame.mixer.set_num_channels(SoundManager._MAX_CHANNELS)
        self._channels = [pygame.mixer.Channel(i) for i in range(SoundManager._MAX_CHANNELS)]
        self._sounds = [None for i in range(SoundManager._MAX_CHANNELS)]

    def add_sound(self, sound: Sound.Sound):
        for i in range(len(self._channels)):
            if self._sounds[i] is None:
                self._sounds[i] = sound
                self._channels[i].play(sound.sound, sound.loops)
                break

    def update(self):
        for i in range(len(self._channels)):
            if self._channels[i].get_busy():
                sound: Sound.Sound = self._sounds[i]
                if sound is None:
                    break
                if sound.max_distance != -1:
                    self._channels[i].set_volume(
                        *Sound.Sound.stereo_sound(sound.target_coordinates,
                                                 sound.sound_coordinates,
                                                 sound.max_distance))
                else:
                    self._channels[i].set_volume(1.0, 1.0)

            elif self._sounds[i] is not None:
                self._sounds[i] = None

    def __str__(self):
        line = str()
        line += f'SoundManager values:'
        for sound in self._sounds:
            line += f'\n{sound}'
        line += f'\n'
        return line

    def search(self, id_sound):
        for element in self._sounds:
            element: Sound.Sound
            if element and id_sound == element.sound_id:
                return element
        return None

    def remove(self, id_sound):
        for i in range(len(self._sounds)):
            element: int
            if self._sounds[i] is not None and id_sound == self._sounds[i].sound_id:
                self._sounds[i] = None
                self._channels[i].stop()
                break

    def all_stop(self):
        for chanell in self._channels:
            chanell.stop()
        for sound in self._sounds:
            sound = None

    def reset(self):
        self._channels = [pygame.mixer.Channel(i) for i in range(SoundManager._MAX_CHANNELS)]
        self._sounds = [None for i in range(SoundManager._MAX_CHANNELS)]
