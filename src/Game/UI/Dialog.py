from typing import List

import pygame


# работает всё на индексах!
class Dialog:

    def __init__(self):
        self._icons: List[pygame.Surface] = []
        self._texts: List[str] = []

        self._index_symbol = 0

        import os
        font_path = os.path.join('src', 'Assets/Fonts/') + 'Minecraft Rus NEW.otf'
        font_size = 20
        self._current_font = pygame.font.Font(font_path, font_size)
        self._current_text_index = 1 # не считая 0

        # self._flag_check_press_E = False # проверка клавиш, чтобы диалог не запускался повторно
        self._dialog_complete = False

    def add_icon(self, icon):
        self._icons.append(icon)
        self._current_icon = self._icons[0]

    def add_text(self, text):

        r'''
        Чтобы добавить задержку в диалог, нужно использовать следующий формат:
        text = 'line1line1line1\nline1line1line1#500\nline1line1line1#1500'
        #[int] - определяет на какое количество миллисекунд прервется диалог
        (если не написать, то задержки не будет)
        '''

        self._texts.append(text)
        self._current_text = self._texts[0]

    @property
    def current_icon(self):
        return self._current_icon
    @property
    def current_text(self):
        return self._current_text

    def next(self):
        if self._index_symbol >= len(self._current_text):
            self._index_symbol = 0
            if self._current_text_index >= len(self._texts): return -1
            self._current_text = self._texts[self._current_text_index]

            self._current_text_index += 1
            return None
        char = self._current_text[self._index_symbol]
        self._index_symbol += 1
        return char

    def next_dialog(self):
        self._index_symbol = 0
        if self._current_text_index >= len(self._texts): return -1
        self._current_text = self._texts[self._current_text_index]
        self._current_icon = self._icons[self._current_text_index]
        self._current_text_index += 1
        return None

    @property
    def current_font(self):
        return self._current_font

    # @property
    # def flag_check_press_E(self):
    #     return self._flag_check_press_E
    #
    # def set_flag_check_press_E(self, flag_check_press_E:bool):
    #     self._flag_check_press_E = flag_check_press_E

    def reset(self):
        self._index_symbol = 0
        self._current_text_index = 1
        self._flag_check_press_E = False
        self._current_icon = self._icons[0]
        self._current_text = self._texts[0]
        self._dialog_complete = False

    @property
    def dialog_complete(self):
        return self._dialog_complete

    def set_dialog_complete(self, value:bool):
        self._dialog_complete = value


