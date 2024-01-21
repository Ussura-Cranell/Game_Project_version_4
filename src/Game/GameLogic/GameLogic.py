import pygame

from src.Game.Managers import AnimationManager, EventManager, ObjManager
from src.Game.GameObject.StaticObject import Trigger
from src.Game.Event import Event


class GameLogic:
    _game_logic = None

    def __new__(cls):
        if not cls._game_logic:
            cls._game_logic = super(GameLogic, cls).__new__(cls)
        return cls._game_logic

    def __init__(self):
        self._animation_manager = AnimationManager.AnimationManager()
        self._event_manager = EventManager.EventManager()
        self._obj_manager = ObjManager.GameObjectManager()

        # test
        self._trigger1 = Trigger.Trigger()
        self._trigger2 = Trigger.Trigger()

        self._animation_player_old_state = 0

    def update(self):
        # print('GameLogic update')

        if self._event_manager.search(Event.EventId.WINDOW_CLOSE) is not None:
            pygame.quit()
            exit()

        animation_player_state = 0

        animation_player_move_left = 1
        animation_player_move_up = 2
        animation_player_move_right = 4
        animation_player_move_down = 8

        if self._event_manager.search(Event.EventId.PLAYER_MOVE_LEFT) is not None:
            animation_player_state |= animation_player_move_left
        if self._event_manager.search(Event.EventId.PLAYER_MOVE_UP) is not None:
            animation_player_state |= animation_player_move_up
        if self._event_manager.search(Event.EventId.PLAYER_MOVE_RIGHT) is not None:
            animation_player_state |= animation_player_move_right
        if self._event_manager.search(Event.EventId.PLAYER_MOVE_DOWN) is not None:
            animation_player_state |= animation_player_move_down

        # нажато 3 клавиши
        if (animation_player_state & animation_player_move_left and
                animation_player_state & animation_player_move_up and
                animation_player_state & animation_player_move_right):
            print('# игрок движется: вверх 3')
            # игрок движется: вверх
            pass
        # elif (animation_player_state & animation_player_move_up and
        #         animation_player_state & animation_player_move_right and
        #         animation_player_state & animation_player_move_down):
        #     print('# игрок движется: вправо 3')
        #     # игрок движется: вправо
        #     pass
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            print('# игрок движется: вниз 3')
            # игрок движется: вниз
            pass
        # elif (animation_player_state & animation_player_move_down and
        #         animation_player_state & animation_player_move_left and
        #         animation_player_state & animation_player_move_up):
        #     print('# игрок движется: влево 3')
        #     # игрок движется: влево
        #     pass
        # нажато 2 клавиши
        elif (animation_player_state & animation_player_move_left and
              animation_player_state & animation_player_move_up):
            print('# игрок движется по-диагонали: лево-верх 2')
            # игрок движется по-диагонали: лево-верх
            pass
        elif (animation_player_state & animation_player_move_up and
              animation_player_state & animation_player_move_right):
            print('# игрок движется по-диагонали: верх-право 2')
            # игрок движется по-диагонали: верх-право
            pass
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down):
            print('# игрок движется по-диагонали: право-низ 2')
            # игрок движется по-диагонали: право-низ
            pass
        elif (animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            print('# игрок движется по-диагонали: низ-лево 2')
            # игрок движется по-диагонали: низ-лево
            pass
        # нажата 1 клавиша
        elif (animation_player_state & animation_player_move_up):
            print('# игрок движется: вверх')
            # игрок движется: вверх
            pass
        elif (animation_player_state & animation_player_move_right):
            print('# игрок движется: вправо')
            # игрок движется: вправо
            pass
        elif (animation_player_state & animation_player_move_down):
            print('# игрок движется: вниз')
            # игрок движется: вниз
            pass
        elif (animation_player_state & animation_player_move_left):
            print('# игрок движется: влево')
            # игрок движется: влево
            pass

        # если игрое двигается
        if animation_player_state != 0:
            self._animation_player_old_state = animation_player_state
            # print('# игрок двигается, записывается предыдущая анимация')
        # если игрок не двигается и
        elif self._animation_player_old_state != 0:
            # print('# игрок не двигается, включение анимации "статика" по соответствующему направлению')
            self._animation_player_old_state = 0

