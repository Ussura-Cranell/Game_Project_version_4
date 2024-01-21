from enum import Enum, auto
import pygame


class ButtonId(Enum):
    PLAY_BUTTON = auto()
    OPTIONS_BUTTON = auto()
    SETTING_BUTTON = auto()
    EXIT_BUTTON = auto()

    EPISODE_1 = auto()
    EPISODE_2 = auto()
    EPISODE_3 = auto()

    PLAY_MENU = auto()
    PLAY_EXIT_MENU = auto()
    PLAY_CONTINUE_MENU = auto()
    PLAY_QUIT_MENU = auto()

    # YES = auto()
    # NO = auto()

    # PLAY_ENVENTORY = auto()

    BACK_BUTTON = auto()

class ButtonСondition(Enum):
    PRESSED = auto()
    SELECRED = auto()
    NOTHING = auto()

class Button():
    def __init__(self, button_id: ButtonId, surface: pygame.Surface, surface_selected: pygame.Surface, surface_pressed: pygame.Surface = None):
        self._button_id = button_id

        self._surface = surface
        self._surface_selected = surface_selected
        self._surface_pressed = surface_pressed

        self._rect = self._surface.get_rect()
        self._condition = ButtonСondition.NOTHING

    @property
    def button_id(self):
        return self._button_id

    def set_condition(self, condition: ButtonСondition):
        self._condition = condition

    @property
    def condition(self):
        return self._condition

    @property
    def surface(self):
        return self._surface

    @property
    def surface_selected(self):
        return self._surface_selected

    @property
    def surface_pressed(self):
        return self._surface_pressed

    @property
    def rect(self):
        return self._rect

    def set_surface(self, surface: pygame.Surface):
        self._surface = surface
        old_rect = self._rect
        self._rect = self._surface.get_rect()
        self._rect.center = old_rect.center

    def set_rect(self, rect: pygame.Rect):
        old_rect = self._rect
        self._rect = rect
        self._rect.center = old_rect.center