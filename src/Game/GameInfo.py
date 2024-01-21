from typing import Tuple
import psutil
import pygame


class GameInfo:
    _game_info = None
    _initialized = False

    def __new__(cls):
        if not cls._game_info:
            cls._game_info = super(GameInfo, cls).__new__(cls)
        return cls._game_info

    def __init__(self):

        if GameInfo._initialized: return None

        # print('init GameInfo')
        self._game_title: str = 'The Noisses is killing (demo)'
        self._game_icon: pygame.Surface = pygame.Surface((100, 100))
        self._game_icon.fill((255, 255, 255))
        self._screen_size = (1200, 760)

        GameInfo._initialized = True

        self._debugging_flag = False

    def set_debugging_flag(self, value:bool):
        self._debugging_flag = value

    @property
    def debugging_flag(self):
        return self._debugging_flag

    def _get_process_memory_usage(self):
        """
        Текущее использование памяти программой.
        """
        process = psutil.Process()
        memory_info = process.memory_info()
        return memory_info.rss

    @property
    def game_title(self) -> str:
        return self._game_title

    @property
    def screen_size(self) -> Tuple[int, int]:
        return self._screen_size

    @property
    def game_icon(self) -> pygame.Surface:
        return self._game_icon

    @property
    def takes_MB(self) -> str:
        return f'{self._get_process_memory_usage() / 1024 ** 2:.2f}'

    @property
    def takes_KB(self) -> str:
        return f'{self._get_process_memory_usage() / 1024:.2f}'

    @property
    def takes_Byte(self) -> str:
        return f'{self._get_process_memory_usage()}'

    # этот метод лучше перенести позже в другой класс
    def reset_all(self):
        from src.Game.Managers import AnimationManager, EventManager, ObjManager, SoundManager

        AnimationManager.AnimationManager().reset()
        EventManager.EventManager().reset()
        ObjManager.GameObjectManager().reset()
        SoundManager.SoundManager().reset()
