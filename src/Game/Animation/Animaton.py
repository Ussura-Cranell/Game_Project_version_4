from enum import Enum, auto
from typing import List

import pygame


class AnimationId(Enum):
    NONE = auto()

    PLAYER_MOVE_LEFT = auto()
    PLAYER_MOVE_UP = auto()
    PLAYER_MOVE_RIGHT = auto()
    PLAYER_MOVE_DOWN = auto()
    PLAYER_MOVE_UP_LEFT = auto()
    PLAYER_MOVE_UP_RIGHT = auto()
    PLAYER_MOVE_DOWN_LEFT = auto()
    PLAYER_MOVE_DOWN_RIGHT = auto()

    ARISTOCRAT_01_LEFT = auto()
    MAIN_MENU_BACKGROUND = auto()
    GAME_UNPUT_TEST = auto()

    # основное
    ANIMATION_1 = auto()
    ANIMATION_2 = auto()
    ANIMATION_3 = auto()
    ANIMATION_4 = auto()
    ANIMATION_5 = auto()
    ANIMATION_6 = auto()


class Animation:

    _DEFAULT_ANIMATION_CYCLICAL = True


    def __init__(self, animation_id: AnimationId,
                 frame_list: List[pygame.Surface] = [],
                 current_frame: int = 0,
                 animation_cyclical: bool = _DEFAULT_ANIMATION_CYCLICAL,
                 delay: int = 0,
                 skip_last_frame: bool = False):
        self._frame_list: List[pygame.Surface] = frame_list
        self._current_frame: int = current_frame
        self._animation_cyclical: bool = animation_cyclical
        self._stop_animation = False
        self._delay = delay
        self._delay_now = 0
        self._skip_last_frame = skip_last_frame

        self._animation_id = animation_id # not used

    def set_frame(self, index: int, frame: pygame.Surface):

        if index >= len(self._frame_list):
            for i in range(len(self._frame_list), index + 1):
                if i == index + 1:
                    self._frame_list.append(None)
                else:
                    self._frame_list.append(frame)
        else:
            if len(self._frame_list) == 0:
                self._frame_list.append(frame)
            else:
                self._frame_list[index] = frame

    def __str__(self):
        return f'Animation:[animation_cyclical:{self._animation_cyclical}, ' \
               f'current_frame:{self._current_frame}, ' \
               f'frame_list:{self._frame_list}]'

    def next(self):

        if not self._stop_animation:

            self._delay_now += 1

            if self._delay_now >= self._delay:
                self._current_frame += 1
                self._delay_now = 0


            size = len(self._frame_list)
            if self._skip_last_frame:
                size -= 1

            if self._current_frame >= size:
                if self._animation_cyclical:
                    self._current_frame = 0
                else:
                    self._current_frame -= 1
                    self._stop_animation = True

    @property
    def frame(self) -> pygame.Surface:
        return self._frame_list[self._current_frame]

    def set_stop_animation(self, stop: bool):
        self._stop_animation = stop

    @property
    def stop_animation(self) -> bool:
        return self._stop_animation

    @property
    def delay(self):
        return self._delay

    def set_delay(self, delay: int):
        self._delay = delay

    @property
    def current_frame(self):
        return self._current_frame

    def set_current_frame(self, index:int):
        if index >= len(self._frame_list):
            index = len(self._frame_list) - 1
        elif index < 0:
            index = 0
        self._current_frame = index

    @property
    def last_index_animation(self):
        return len(self._frame_list)

