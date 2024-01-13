from typing import Set

from src.Game.Managers import EventManager
from src.Game.Event import Event
from src.Game.Animation import Animaton
from src.Game.GameObject.Entity import Player
import pygame

class GameLogic:

    def __init__(self, shared_resources: dict = None):
        self._shared_resources = shared_resources
        self._animationmanager = shared_resources.get('animationmanager')

        self._eventmanager = EventManager.EventManager()

        self._player: Player.Player = shared_resources.get('player')
        self._player_animation_old_state = None

        from src.Game.GameObject.StaticObject import Trigger
        self._barriers: Set[Trigger.Trigger] = shared_resources.get('barriers')

        from src.Game.Scene import Scene
        self._scene: Scene.Scene = shared_resources.get('scene')

        from src.Game.Sound import Sound
        from src.Game.Managers import SoundManager

        self._soundmanager = SoundManager.SoundManager()
        self._soundstorage: Sound.SoundStorage = shared_resources.get('soundstorage')
        self._tv_sound: Sound.Sound = shared_resources.get('tv_music')
        self._tv_trigger = self._shared_resources.get('tv_trigger')
        self._tv = self._shared_resources.get('tv')
        self._spikers = self._shared_resources.get('spikers')
        self._sound_step = self._shared_resources.get('sound_step')

    def update(self):

        from src.Game.Sound import Sound


        if self._player.gameobject.rect.colliderect(self._tv_trigger.gameobject.rect):
            if self._soundmanager.search(Sound.SoundId.Memphis_Cult9Mm) is None:
                self._soundmanager.add_sound(self._tv_sound)
                from src.Game.GameObject.Entity import Entity
                self._tv:Entity.Entity
                if self._tv.current_animation is not Animaton.AnimationId.ANIMATION_1:
                    self._tv.set_current_animation(Animaton.AnimationId.ANIMATION_1)
                    self._spikers.set_current_animation(Animaton.AnimationId.ANIMATION_1)
            # print(f'self._tv.current_animation: {self._tv.current_animation}')

        if self._soundmanager.search(Sound.SoundId.Memphis_Cult9Mm) is None:
            self._tv.set_current_animation(Animaton.AnimationId.NONE)
            self._spikers.set_current_animation(Animaton.AnimationId.NONE)
        self._tv_sound.set_target_coordinates(self._player.gameobject.rect.center)
        self._sound_step: Sound.Sound

        if self._eventmanager.search(Event.EventId.PlAYER_PRESS_ESC):
            from src.Game.UI import Menus

            if self._scene:
                self._scene.uimanager.change_menu(Menus.Play_Menu(self._scene.camera.surface))
                self._eventmanager.del_event(Event.Event(Event.EventId.PlAYER_PRESS_ESC)) # на всякий случай
                self._soundmanager.all_stop()
            else:
                from src.Game.Scene import Scene
                self._scene: Scene.Scene = self._shared_resources.get('scene')

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
            self._player.current_animation.set_stop_animation(True)
            self._player.current_animation.set_current_frame(
                self._player.current_animation.last_index_animation)
            if self._soundmanager.search(Sound.SoundId.SOUND_PLAYER_STEP):
                self._soundmanager.remove(Sound.SoundId.SOUND_PLAYER_STEP)

        elif self._player.current_animation.stop_animation:
            self._player.current_animation.set_stop_animation(False)
            if self._soundmanager.search(Sound.SoundId.SOUND_PLAYER_STEP) is None:
                self._soundmanager.add_sound(self._sound_step)

        speed_penalty = 0.75

        # нажато 3 клавиши
        if (animation_player_state & animation_player_move_left and
                animation_player_state & animation_player_move_up and
                animation_player_state & animation_player_move_right):
            print('# игрок движется: вверх 3')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP)
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              0,
                                              -self._player.movement_speed)
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN)
            print('# игрок движется: вниз 3')
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              0,
                                              self._player.movement_speed)
        elif (animation_player_state & animation_player_move_left and
              animation_player_state & animation_player_move_up):
            print('# игрок движется по-диагонали: лево-верх 2')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP_LEFT)
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              -self._player.movement_speed * speed_penalty,
                                              -self._player.movement_speed * speed_penalty)

            pass
        elif (animation_player_state & animation_player_move_up and
              animation_player_state & animation_player_move_right):
            print('# игрок движется по-диагонали: верх-право 2')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP_RIGHT)
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              self._player.movement_speed * speed_penalty,
                                              -self._player.movement_speed * speed_penalty)
            pass
        elif (animation_player_state & animation_player_move_right and
              animation_player_state & animation_player_move_down):
            print('# игрок движется по-диагонали: право-низ 2')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN_RIGHT)
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              self._player.movement_speed * speed_penalty,
                                              self._player.movement_speed * speed_penalty)

            pass
        elif (animation_player_state & animation_player_move_down and
              animation_player_state & animation_player_move_left):
            print('# игрок движется по-диагонали: низ-лево 2')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN_LEFT)
            self.check_player_move_to_barrier(self._player,
                                              self._barriers,
                                              -self._player.movement_speed * speed_penalty,
                                              +self._player.movement_speed * speed_penalty)
        elif (animation_player_state & animation_player_move_up):
            print('# игрок движется: вверх')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_UP)
            self.check_player_move_to_barrier(self._player, self._barriers, 0, -self._player.movement_speed)
        elif (animation_player_state & animation_player_move_right):
            print('# игрок движется: вправо')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_RIGHT)
            self.check_player_move_to_barrier(self._player, self._barriers, self._player.movement_speed, 0)
        elif (animation_player_state & animation_player_move_down):
            print('# игрок движется: вниз')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN)
            self.check_player_move_to_barrier(self._player, self._barriers, 0, self._player.movement_speed)
            pass
        elif (animation_player_state & animation_player_move_left):
            print('# игрок движется: влево')
            self._player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_LEFT)
            self.check_player_move_to_barrier(self._player, self._barriers, -self._player.movement_speed, 0)

        # print(f'animation_player_state: {animation_player_state}')
        # print(f'animation_player_state: {self._player.current_animation.current_frame}')

    def check_player_move_to_barrier(self, player: Player.Player, barriers, x: int, y: int):

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

    def camera_move_cursor(self):

        if self._scene is None:
            self._scene = self._shared_resources.get('scene')
        else:
            # Текущее положение курсора и центра экрана
            cursor_position = pygame.mouse.get_pos()
            screen_center = self._scene.camera.screen_center

            # Вычисление вектора смещения от центра экрана до курсора
            offset_vector = pygame.Vector2(cursor_position[0] - screen_center[0], cursor_position[1] - screen_center[1])

            # Коэффициент масштабирования в зависимости от расстояния
            distance_scale = 0.025  # Настройка
            scale_factor = 1.0 / (1.0 + distance_scale * offset_vector.length())

            camera_movement = offset_vector * scale_factor

            # print(f'camera_movement: {camera_movement}')
            self._scene.camera.set_position((self._scene.camera.position[0] + camera_movement[0],
                                            self._scene.camera.position[1] + camera_movement[1]))