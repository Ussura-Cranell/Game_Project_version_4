from typing import List

import pygame


class Information:
    def __init__(self, text):
        import os
        font_path = os.path.join('src', 'Assets/Fonts/') + 'Minecraft Rus NEW.otf'
        font_size = 25
        self._current_font = pygame.font.Font(font_path, font_size)

        self._text:str = text

        # self._flag_check_press_E = False  # проверка клавиш, чтобы диалог не запускался повторно

        self._information_complete = False
        self._yes_button = False
        self._no_button = False

    @property
    def text(self):
        return self._text

    @property
    def current_font(self):
        return self._current_font

    # @property
    # def flag_check_press_E(self):
    #     return self._flag_check_press_E
    #
    # def set_flag_check_press_E(self, flag_check_press_E: bool):
    #     self._flag_check_press_E = flag_check_press_E

    @property
    def information_complete(self):
        return self._information_complete

    @property
    def yes_button(self):
        return self._yes_button

    @property
    def no_button(self):
        return self._no_button

    def set_information_complete(self, information_complete):
        self._information_complete = information_complete

    def set_yes_button(self, yes_button):
        self._yes_button = yes_button

    def set_no_button(self, no_button):
        self._no_button = no_button

    def restart(self):
        self._information_complete = False
        self._yes_button = False
        self._no_button = False