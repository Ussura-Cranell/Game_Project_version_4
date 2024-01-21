import pygame
from src.Game import GameInfo
import os # временно


class Window:
    _window = None
    _initialized = False

    def __new__(cls):
        if not cls._window:
            cls._window = super(Window, cls).__new__(cls)
        return cls._window

    def __init__(self):

        if Window._initialized: return None

        # print('init Window')
        gameinfo = GameInfo.GameInfo()
        self._screen = pygame.display.set_mode(size=gameinfo.screen_size, flags=pygame.HWSURFACE | pygame.DOUBLEBUF)
        # | pygame.RESIZABLE - изменение размеров окна
        pygame.display.set_caption(gameinfo.game_title)
        pygame.display.set_icon(gameinfo.game_icon)
        self._clock = pygame.time.Clock()

        Window._initialized = True

    @property
    def screen(self): return self._screen

    @property
    def clock(self): return self._clock

    def clear_console(self): # временно
        # Очистка консоли в зависимости от операционной системы
        os.system('cls' if os.name == 'nt' else 'clear')
