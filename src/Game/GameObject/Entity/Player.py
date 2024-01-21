import os
from typing import Tuple, Set

import pygame

from src.Game.GameObject.Entity import Entity
from src.Game.Managers import EventManager, SoundManager, AnimationManager
from src.Game.Event import Event, InputEvent
from src.Game.Animation import Animaton
from src.Game.Sound import Sound

# name='Testing Player 1', size=(47, 45), layer=2

class Player(Entity.Entity):
    # игрок - единая сущность для всех сцен. Его состояние должно оставаться неизменимым между переходами эпизодов
    _player_object = None
    _initialized = False

    _default_name = "Ussura_Cranell"
    _default_rect_position = (0, 0)
    _default_rect_size = (47, 45)
    _default_layer = 2

    def __new__(cls):
        if not cls._player_object:
            cls._player_object = super(Player, cls).__new__(cls)
        return cls._player_object

    def __init__(self,
                 name: str = _default_name,
                 pos: Tuple[int, int] = _default_rect_position,
                 size: Tuple[int, int] = _default_rect_size,
                 layer: int = _default_layer):
        if Player._initialized: return None
        super().__init__(name, pos, size, layer)
        self._shared_resources: dict = None

        self._eventmanager = EventManager.EventManager()
        self._soundmanager = SoundManager.SoundManager()
        self._soundstorage = Sound.SoundStorage()
        Player._initialized = True

        self._barriers: set = None

        self._horizontale_testing_rect = pygame.Rect(0, 0, 1, 1)

        self._inventory = dict()

        # self._inventory['TV_remote_control'] = True # отладка

        character_steps = Sound.Sound(Sound.SoundId.SOUND_PLAYER_STEP,
                               os.path.join('src', 'Assets/Sounds/Other/player steps4.mp3'),
                               -1,
                               None,
                               None,
                               -1)

    def Player_Reset(self, name: str = _default_name,
                 pos: Tuple[int, int] = _default_rect_position,
                 size: Tuple[int, int] = _default_rect_size,
                 layer: int = _default_layer):
        super().__init__(name, pos, size, layer)
        self._shared_resources: dict = None

        self._eventmanager = EventManager.EventManager()
        self._soundmanager = SoundManager.SoundManager()
        self._soundstorage = Sound.SoundStorage()
        self._barriers: set = None

        # инвентарь сохраняется между переходами

    def set_shared_resources(self, shared_resources: dict):
        self._shared_resources = shared_resources
        self._barriers = shared_resources.get('barriers')

    def player_movement_update(self):

        # движение и анимация игрока
        animation_player_state = 0

        animation_player_move_left = 1
        animation_player_move_up = 2
        animation_player_move_right = 4
        animation_player_move_down = 8

        if self._eventmanager.search(Event.EventId.PLAYER_MOVE_LEFT) is not None:
            animation_player_state |= animation_player_move_left
        if self._eventmanager.search(Event.EventId.PLAYER_MOVE_UP) is not None:
            animation_player_state |= animation_player_move_up
        if self._eventmanager.search(Event.EventId.PLAYER_MOVE_RIGHT) is not None:
            animation_player_state |= animation_player_move_right
        if self._eventmanager.search(Event.EventId.PLAYER_MOVE_DOWN) is not None:
            animation_player_state |= animation_player_move_down

        if not bool(animation_player_state):
            # print('игрок не двигается')

            #print(f'super().current_animation: {super().current_animation}')
            print(f'self.current_animation: {self.current_animation}')

            # exit()
            self.current_animation.set_stop_animation(True)
            self.current_animation.set_current_frame(
                self.current_animation.last_index_animation)
            if self._soundmanager.search(Sound.SoundId.SOUND_PLAYER_STEP):
                self._soundmanager.remove(Sound.SoundId.SOUND_PLAYER_STEP)
            #     self._soundmanager.remove(Sound.SoundId.SOUND_PLAYER_STEP)

        elif self.current_animation.stop_animation:
            self.current_animation.set_stop_animation(False)
            if not self._soundmanager.search(Sound.SoundId.SOUND_PLAYER_STEP):
                sound = self._soundstorage.get_sound(Sound.SoundId.SOUND_PLAYER_STEP)
                self._soundmanager.add_sound(sound)
            #     self._soundmanager.add_sound(self._sound_step)

        speed_penalty = 0.75

        # нажато 3 клавиши
        if (animation_player_state & animation_player_move_left and
                animation_player_state & animation_player_move_up and
                animation_player_state & animation_player_move_right):
            print('# игрок движется: вверх 3')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP)
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              0,
                                              -self.movement_speed)
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN)
            print('# игрок движется: вниз 3')
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              0,
                                              self.movement_speed)
        elif (animation_player_state & animation_player_move_left and
              animation_player_state & animation_player_move_up):
            print('# игрок движется по-диагонали: лево-верх 2')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP_LEFT)
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              -self.movement_speed * speed_penalty,
                                              -self.movement_speed * speed_penalty)

            pass
        elif (animation_player_state & animation_player_move_up and
              animation_player_state & animation_player_move_right):
            print('# игрок движется по-диагонали: верх-право 2')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP_RIGHT)
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              self.movement_speed * speed_penalty,
                                              -self.movement_speed * speed_penalty)
            pass
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down):
            print('# игрок движется по-диагонали: право-низ 2')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN_RIGHT)
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              self.movement_speed * speed_penalty,
                                              self.movement_speed * speed_penalty)

            pass
        elif (animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            print('# игрок движется по-диагонали: низ-лево 2')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN_LEFT)
            self.check_player_move_to_barrier(self,
                                              self._barriers,
                                              -self.movement_speed * speed_penalty,
                                              +self.movement_speed * speed_penalty)
        elif (animation_player_state & animation_player_move_up):
            print('# игрок движется: вверх')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP)
            self.check_player_move_to_barrier(self, self._barriers, 0, -self.movement_speed)
        elif (animation_player_state & animation_player_move_right):
            print('# игрок движется: вправо')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_RIGHT)
            self.check_player_move_to_barrier(self, self._barriers, self.movement_speed, 0)
        elif (animation_player_state & animation_player_move_down):
            print('# игрок движется: вниз')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN)
            self.check_player_move_to_barrier(self, self._barriers, 0, self.movement_speed)
            pass
        elif (animation_player_state & animation_player_move_left):
            print('# игрок движется: влево')
            self.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_LEFT)
            self.check_player_move_to_barrier(self, self._barriers, -self.movement_speed, 0)

    # print(f'animation_player_state: {animation_player_state}')
    # print(f'animation_player_state: {self.current_animation.current_frame}')

    def check_player_move_to_barrier(self, player, barriers, x: int, y: int):

        from src.Game.GameObject.StaticObject import Trigger
        barriers: Set[Trigger.Trigger]

        rect_player = pygame.Rect(player.gameobject.rect)
        rect_player.x += 17
        rect_player.y += 49
        rect_player.size = (25, 10)

        rect_old_x, rect_old_y = rect_player.topleft

        if x != 0:
            rect_player.x += x
            barrier_flag: bool = False # игрок касается барьера
            for barrier in barriers:
                if barrier.gameobject.rect.colliderect(rect_player):
                    barrier_flag = True
            if not barrier_flag:
                # игрок не касается барьера
                player.gameobject.rect.x += x
            else:
                rect_player.topleft = (rect_old_x, rect_player.y)

        if y != 0:
            rect_player.y += y
            barrier_flag: bool = False  # игрок касается барьера
            for barrier in barriers:
                if barrier.gameobject.rect.colliderect(rect_player):
                    barrier_flag = True
            if not barrier_flag:
                # игрок не касается барьера
                player.gameobject.rect.y += y
            else:
                rect_player.topleft = (rect_player.x, rect_old_y)

        horizontale_testing_rect = pygame.Rect(player.gameobject.rect)
        horizontale_testing_rect.x += 17
        horizontale_testing_rect.y += 49
        horizontale_testing_rect.size = (25, 10)

        self._shared_resources['horizontale_testing_rect'] = horizontale_testing_rect
        self._horizontale_testing_rect = horizontale_testing_rect

    @property
    def horizontale_testing_rect(self):
        return self._horizontale_testing_rect

    @property
    def inventory(self):
        return self._inventory