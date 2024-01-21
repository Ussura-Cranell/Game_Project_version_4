import os
from typing import Set, List, Type

from src.Game.Managers import EventManager
from src.Game.Event import Event
from src.Game.Animation import Animaton
from src.Game.GameObject.Entity import Player
from . import SharedResources
from src.Game.UI import Menus
from src.Game.Tools import Multitool
from src.Game.Sound import Sound
import pygame


class GameLogic:
    class Refrigerator_event:
        # from ...GameLogic.GameLogic import GameLogic
        def __init__(self, game_logic_object: Type['GameLogic()']):
            self._game_logic_object = game_logic_object  # экземпляр GameLogic
            self._shared_resources = SharedResources.SharedResources().shared_resources  # общие ресурсы

            from src.Game.Scene import Scene
            self._scene: Scene.Scene = self._shared_resources.get('scene')

            # from src.Game.Sound import Sound
            from src.Game.Managers import SoundManager
            self._soundmanager = SoundManager.SoundManager()

            self._eventmanager = EventManager.EventManager()

            from src.Game.GameObject.StaticObject import Trigger
            point_reference = self._shared_resources.get('point_reference')
            self._refrigerator_area = Trigger.Trigger(name='refrigerator_area',
                                                      pos=(point_reference[0] + 310, point_reference[1] + 84),
                                                      size=(32, 20)).gameobject.rect
            self._shared_resources['refrigerator_area'] = self._refrigerator_area

            self._player: Player.Player = Player.Player()

            # self._horizontale_testing_rect:pygame.Rect = self._shared_resources.get('horizontale_testing_rect')

            from src.Game.UI import Dialog
            # self._dialog1: Dialog.Dialog = self._shared_resources.get('dialog1')

            self._update = self.dialog_refrigerator1

            from src.Game.UI import Dialog, Information
            text1 = f'\n Обожаю холодильники! #400\n Они как магические порталы в мир\n бескрайних возможностей.'
            text2 = f'\n Кстати я очень хочу пить.#400\n Может там что-то осталось со вчера?'
            text3 = f'\n Хмм...#400\n Думаю сделаю это в другой раз'
            text4 = f'#400\n Блин, тут совсем ничего не осталось.#600\n Есть только пакет кифира, но он очень\n подозрительно на меня смотрит #400\n'
            text5 = f'\n СТОП ЧТО???#750\n ЧТО ЗДЕСЬ ДЕЛАЕТ ПУЛЬТ ОТ ТЕЛЕВИЗОРА???#1000\n Хотя чему я удивляюсь...'
            text6 = f'\n Он немного холодный'

            dialog1 = Dialog.Dialog()
            dialog2 = Dialog.Dialog()
            dialog3 = Dialog.Dialog()
            dialog4 = Dialog.Dialog()

            icon1 = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/UNTITLED.png')).convert()
            dialog1.add_icon(icon1)
            dialog1.add_icon(icon1)
            dialog1.add_text(text1)
            dialog1.add_text(text2)

            dialog2.add_icon(icon1)
            dialog2.add_text(text3)

            dialog3.add_icon(icon1)
            dialog3.add_icon(icon1)
            dialog3.add_text(text4)
            dialog3.add_text(text5)

            dialog4.add_icon(icon1)
            dialog4.add_text(text6)

            information1 = Information.Information('\nОткрыть холодильник?')
            information2 = Information.Information('\nВзять пульт от телевизора?')

            self._refrigerator_1 = dialog1
            self._refrigerator_2 = dialog2
            self._refrigerator_3 = dialog3
            self._refrigerator_4 = dialog4

            self._information1 = information1
            self._information2 = information2

            from src.Game.GameObject.Entity import Entity
            from src.Game.Animation import Animaton
            from src.Game.Managers import AnimationManager
            refrigerator_animation_sheet = pygame.image.load(
                os.path.join('src', 'Assets/testAnimations/animated_fridge_white_64x96.png'))
            refrigerator_animation = Multitool.x_y_transform_spritesheet_to_animation(
                refrigerator_animation_sheet, (64, 96))

            self._refrigerator_object = Entity.Entity(name='refrigerator_object',
                                                      pos=(0, 0),
                                                      size=(64, 96),
                                                      layer=1,
                                                      movement_speed=0)
            animation1 = Animaton.Animation(Animaton.AnimationId.ANIMATION_1,
                                            refrigerator_animation,
                                            0,
                                            False,
                                            3,
                                            True)
            self._refrigerator_object.add_animation(Animaton.AnimationId.ANIMATION_1, animation1)
            self._refrigerator_object.set_current_animation(Animaton.AnimationId.ANIMATION_1)
            self._refrigerator_object.sprite.set_surface(refrigerator_animation[0])

            self._refrigerator_object.gameobject.rect.topleft = (point_reference[0] + 310, point_reference[1])

            self._animationmanager = AnimationManager.AnimationManager()

        def set_update_function(self, update):
            self._update = update

        @property
        def update(self):
            return self._update

        # холодильник
        def dialog_refrigerator1(self):

            if self._refrigerator_1.dialog_complete:
                self.set_update_function(self.information_refrigerator_1)

            elif self._player.horizontale_testing_rect.colliderect(self._refrigerator_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:

                self._game_logic_object.set_check_button_E_pressed(True)
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._refrigerator_1))
                self._soundmanager.all_pause()
                # self._eventmanager.add_event(Event.Event(Event.EventId.PLAYER_PRESS_E))

        # в другой раз
        def dialog_refrigerator2(self):

            if self._refrigerator_2.dialog_complete:
                self.set_update_function(self.wait1)
                self._information1.restart()

            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._refrigerator_2))
                # self._soundmanager.all_pause()

        # пульт от телика
        def dialog_refrigerator3(self):

            if self._refrigerator_3.dialog_complete:
                self.set_update_function(self.information_refrigerator_2)
                # self._information1.restart()

            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._refrigerator_3))
                # self._soundmanager.all_pause()

        # в другой раз 2
        def dialog_refrigerator4(self):
            if self._refrigerator_2.dialog_complete:
                self.set_update_function(self.wait3)
                self._information2.restart()

            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._refrigerator_2))
                # self._soundmanager.all_pause()

        # холодный
        def dialog_refrigerator5(self):
            if self._refrigerator_4.dialog_complete:
                self.set_update_function(self.nothing)
            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._refrigerator_4))
                # self._soundmanager.all_pause()
                self._player.inventory['TV_remote_control'] = True

        # открыть?
        def information_refrigerator_1(self):

            if self._information1.information_complete:
                if self._information1.yes_button:
                    self.set_update_function(self.ir1_yes)
                elif self._information1.no_button:
                    self.set_update_function(self.ir1_no)

            else:
                self._scene.uimanager.change_menu(
                    Menus.InformationPanel(self._scene.camera.surface, self._information1))
                self._soundmanager.all_pause()

        # взять?
        def information_refrigerator_2(self):

            if self._information2.information_complete:
                if self._information2.yes_button:
                    self.set_update_function(self.ir2_yes)
                elif self._information2.no_button:
                    self.set_update_function(self.ir2_no)

            else:
                self._scene.uimanager.change_menu(
                    Menus.InformationPanel(self._scene.camera.surface, self._information2))
                self._soundmanager.all_pause()

        # действие если открыть
        def ir1_yes(self):
            self._animationmanager.add_animation_entity(self._refrigerator_object)
            self.set_update_function(self.wait2)
            # print(f'YES!!!!!!!!!!!!!!!!!')

        # действие если не открывать
        def ir1_no(self):
            self.set_update_function(self.dialog_refrigerator2)

        # забрать
        def ir2_yes(self):
            self.set_update_function(self.dialog_refrigerator5)

        # оставить
        def ir2_no(self):
            self.set_update_function(self.dialog_refrigerator4)

        # ожидание открытия игроком холодильника
        def wait1(self):

            if self._player.horizontale_testing_rect.colliderect(self._refrigerator_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self.set_update_function(self.information_refrigerator_1)

        # ожидание анимации открытия холодильника
        def wait2(self):

            if self._refrigerator_object.current_animation.current_frame is \
                    self._refrigerator_object.current_animation.last_index_animation - 2:
                self.set_update_function(self.dialog_refrigerator3)
                self._refrigerator_2.reset()

        # ожидание действия с пультом
        def wait3(self):
            if self._player.horizontale_testing_rect.colliderect(self._refrigerator_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self.set_update_function(self.information_refrigerator_2)

        def nothing(self):
            pass

    class TV_event:
        def __init__(self, game_logic_object: Type['GameLogic()']):
            self._game_logic_object = game_logic_object  # экземпляр GameLogic
            self._shared_resources = SharedResources.SharedResources().shared_resources  # общие ресурсы

            self._player: Player.Player = Player.Player()

            from src.Game.Scene import Scene
            self._scene: Scene.Scene = self._shared_resources.get('scene')

            # from src.Game.Sound import Sound
            from src.Game.Managers import SoundManager
            self._soundmanager = SoundManager.SoundManager()

            self._eventmanager = EventManager.EventManager()

            from src.Game.GameObject.StaticObject import Trigger
            point_reference = self._shared_resources.get('point_reference')
            self._tv_area = Trigger.Trigger(name='refrigerator_area',
                                            pos=(point_reference[0] + 520, point_reference[1] + 260),
                                            size=(58, 32)).gameobject.rect
            self._shared_resources['tv_area'] = self._tv_area

            from src.Game.UI import Dialog
            self._dialog1: Dialog.Dialog = self._shared_resources.get('dialog1')

            self._update = self.dialog_tv1
            from src.Game.UI import Dialog, Information

            text1 = f'\n Чтобы включить телевизор придется\n немного поискать пульт.#500\n Благо он не мог далеко уйти#500\n (у него вообще-то нет ног)'
            icon1 = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/UNTITLED.png')).convert()

            dialog1 = Dialog.Dialog()

            dialog1.add_icon(icon1)
            dialog1.add_text(text1)

            self._tv_dialog1 = dialog1
            self._information1 = Information.Information('\nВключить телевизор?')

            # анимация телевизора
            from src.Game.GameObject.Entity import Entity
            from src.Game.Sound import Sound
            from src.Game.Animation import Animaton
            from src.Game.Managers import AnimationManager, SoundManager
            self._animationmanager = AnimationManager.AnimationManager()
            self._soundstorage = Sound.SoundStorage()

            self._tv = Entity.Entity(name=str(id), layer=3, size=(50, 22))
            self._tv.sprite.rect.topleft = (point_reference[0] + 524, point_reference[1] + 200)

            dance_9mm = pygame.image.load(os.path.join('src', 'Assets/testAnimations/dancespritesheet.png'))
            dance_9mm = Multitool.x_y_transform_spritesheet_to_animation(dance_9mm, (50, 22))
            # exit()

            animation = Animaton.Animation(Animaton.AnimationId.ANIMATION_1,
                                           dance_9mm,
                                           0,
                                           True,
                                           2,
                                           False)
            self._tv.add_animation(Animaton.AnimationId.ANIMATION_1, animation)
            self._tv.set_current_animation(Animaton.AnimationId.ANIMATION_1)
            self._tv_surface = pygame.Surface((50, 22))
            self._tv_surface.fill((10, 10, 10))
            self._tv.sprite.set_surface(self._tv_surface)
            animation = Animaton.Animation(Animaton.AnimationId.NONE,
                                           [self._tv_surface],
                                           0,
                                           False,
                                           0,
                                           False)
            self._tv.add_animation(Animaton.AnimationId.NONE, animation)

            from src.Game.Sound import Sound
            self._tv_music = Sound.Sound(Sound.SoundId.Memphis_Cult9Mm,
                                         os.path.join('src',
                                                      'Assets/Music/Memphis Cult - 9MM (Lyrics) _ watch my 9mm go bang.mp3'),
                                         0,
                                         self._player.horizontale_testing_rect.center,
                                         self._tv.gameobject.rect.center,
                                         400)

            self._spikers = Entity.Entity(name=str(id), layer=1, size=(32, 64))
            self._spikers.sprite.rect.topleft = (point_reference[0] + 593, point_reference[1] + 188)

            spikers_animation = pygame.image.load(os.path.join('src', 'Assets/testAnimations/spikers.png'))
            spikers_animation = Multitool.x_y_transform_spritesheet_to_animation(spikers_animation, (32, 64))

            animation = Animaton.Animation(Animaton.AnimationId.ANIMATION_1,
                                           spikers_animation,
                                           0,
                                           True,
                                           2,
                                           False)
            self._spikers.add_animation(Animaton.AnimationId.ANIMATION_1, animation)
            self._spikers.set_current_animation(Animaton.AnimationId.ANIMATION_1)
            self._spikers.sprite.set_surface(spikers_animation[0])

        def set_update_function(self, update):
            self._update = update

        @property
        def update(self):
            return self._update

        def none(self):
            pass

        def dialog_tv1(self):

            if self._tv_dialog1.dialog_complete:
                self._tv_dialog1.reset()
                # self.set_update_function(self._tv_dialog1)

            elif self._player.horizontale_testing_rect.colliderect(self._tv_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:

                if self._player.inventory.get('TV_remote_control'):
                    self.set_update_function(self.information_tv1)
                else:
                    self._game_logic_object.set_check_button_E_pressed(True)
                    self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._tv_dialog1))
                    self._soundmanager.all_pause()

        def information_tv1(self):
            if self._information1.information_complete:
                if self._information1.yes_button:
                    self.set_update_function(self.ir1_yes)
                elif self._information1.no_button:
                    self.set_update_function(self.ir1_no)

            else:
                self._scene.uimanager.change_menu(
                    Menus.InformationPanel(self._scene.camera.surface, self._information1))
                self._soundmanager.all_pause()

        def ir1_yes(self):
            self._animationmanager.add_animation_entity(self._tv)
            self._animationmanager.add_animation_entity(self._spikers)
            self._soundmanager.add_sound(self._tv_music)
            self.set_update_function(self.play_clip)
            pass

        def ir1_no(self):
            self.set_update_function(self.wait1)

        def play_clip(self):
            if not self._soundmanager.search(Sound.SoundId.Memphis_Cult9Mm):
                self._tv.current_animation.set_stop_animation(True)
                self._tv.set_current_animation(Animaton.AnimationId.NONE)

                self._spikers.current_animation.set_current_frame(0)
                self._spikers.current_animation.set_stop_animation(True)

                self.set_update_function(self.none)
            else:
                self._tv_music.set_target_coordinates(self._player.horizontale_testing_rect.center)

        def wait1(self):

            if self._player.horizontale_testing_rect.colliderect(self._tv_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self._information1.restart()
                self.set_update_function(self.information_tv1)

    class MrCreeper_event:
        def __init__(self, game_logic_object: Type['GameLogic()']):
            self._game_logic_object = game_logic_object  # экземпляр GameLogic
            self._shared_resources = SharedResources.SharedResources().shared_resources  # общие ресурсы

            self._player: Player.Player = Player.Player()

            from src.Game.Scene import Scene
            self._scene: Scene.Scene = self._shared_resources.get('scene')

            # from src.Game.Sound import Sound
            from src.Game.Managers import SoundManager
            self._soundmanager = SoundManager.SoundManager()

            self._eventmanager = EventManager.EventManager()

            from src.Game.GameObject.StaticObject import Trigger
            point_reference = self._shared_resources.get('point_reference')
            self._creep_area = Trigger.Trigger(name='creep_area',
                                               pos=(point_reference[0] + 225, point_reference[1] + 237),
                                               size=(63, 18)).gameobject.rect
            self._shared_resources['creep_area'] = self._creep_area

            from src.Game.UI import Dialog
            self._dialog1: Dialog.Dialog = self._shared_resources.get('dialog1')

            self._update = self.dialog_creep1
            from src.Game.UI import Dialog, Information

            text1 = f'\n Я очень сильно боюсь криперов.#400\n Именно поэтому я повесил рядом картину\n кошки'
            text2 = f'\n ...'
            icon1 = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/UNTITLED.png')).convert()

            dialog1 = Dialog.Dialog()
            dialog2 = Dialog.Dialog()

            dialog1.add_icon(icon1)
            dialog1.add_text(text1)

            dialog2.add_icon(icon1)
            dialog2.add_text(text2)

            self._creep_dialog1 = dialog1
            self._creep_dialog2 = dialog2

        def set_update_function(self, update):
            self._update = update

        @property
        def update(self):
            return self._update

        def none(self):
            pass

        def dialog_creep1(self):

            if self._creep_dialog1.dialog_complete:
                self.set_update_function(self.wait1)

            elif self._player.horizontale_testing_rect.colliderect(self._creep_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._creep_dialog1))
                # self._soundmanager.pause(Sound.SoundId.SOUND_PLAYER_STEP)
                self._soundmanager.all_pause()

        def wait1(self):

            if self._player.horizontale_testing_rect.colliderect(self._creep_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self.set_update_function(self.end)
                self._creep_dialog2.reset()

        def end(self):
            if self._creep_dialog2.dialog_complete:
                self.set_update_function(self.wait1)
                self._game_logic_object.set_check_button_E_pressed(True)
            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._creep_dialog2))
                # self._soundmanager.pause(Sound.SoundId.SOUND_PLAYER_STEP)
                self._soundmanager.all_pause()

    class Bed_event:
        def __init__(self, game_logic_object: Type['GameLogic()']):
            self._game_logic_object = game_logic_object  # экземпляр GameLogic
            self._shared_resources = SharedResources.SharedResources().shared_resources  # общие ресурсы

            self._player: Player.Player = Player.Player()

            from src.Game.Scene import Scene
            self._scene: Scene.Scene = self._shared_resources.get('scene')

            # from src.Game.Sound import Sound
            from src.Game.Managers import SoundManager
            self._soundmanager = SoundManager.SoundManager()

            self._eventmanager = EventManager.EventManager()

            from src.Game.GameObject.StaticObject import Trigger
            point_reference = self._shared_resources.get('point_reference')
            self._bed_area = Trigger.Trigger(name='bed_area',
                                               pos=(point_reference[0] + 79, point_reference[1] + 400),
                                               size=(50, 40)).gameobject.rect
            self._shared_resources['bed_area'] = self._bed_area

            from src.Game.UI import Dialog
            self._dialog1: Dialog.Dialog = self._shared_resources.get('dialog1')

            self._update = self.dialog_bed1
            from src.Game.UI import Dialog, Information

            text1 = f'\n Это моя кроватка.#600\n Наверное не мешало бы заправить её...'
            text2 = f'\n Думаю ничего страшного, если я сделаю это\n немного позже'
            text3 = f'\n Так намного лучше)'
            icon1 = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/UNTITLED.png')).convert()

            dialog1 = Dialog.Dialog()
            dialog2 = Dialog.Dialog()
            dialog3 = Dialog.Dialog()

            dialog1.add_icon(icon1)
            dialog1.add_text(text1)

            dialog2.add_icon(icon1)
            dialog2.add_text(text2)

            dialog3.add_icon(icon1)
            dialog3.add_text(text3)

            self._bed_dialog1 = dialog1
            self._bed_dialog2 = dialog2
            self._bed_dialog3 = dialog3

            self._information1 = Information.Information('\n\nзаправить кроватку?')

            from src.Game.GameObject.StaticObject import Decoration

            self._blanket = Decoration.Decoration(name='blanket',
                                                  pos=(point_reference[0] + 79, point_reference[1] + 347),
                                                  size=(64, 96),
                                                  layer=0)
            r'D:\программирование\python\GameV4\src\Assets\Sprites\Decoration\Bedroom_Singles_Shadowless_32x32_196.png'
            self._blanket_surface_no = pygame.image.load(os.path.join('src', 'Assets/Sprites/Decoration/Bedroom_Singles_Shadowless_32x32_196.png')).convert_alpha()
            self._blanket_surface_yes = pygame.image.load(os.path.join('src', 'Assets/Sprites/Decoration/Bedroom_Singles_Shadowless_32x32_197.png')).convert_alpha()
            self._blanket.sprite.set_surface(self._blanket_surface_no)

            from src.Game.Sound import Sound

            self._sound_covering = Sound.Sound(Sound.SoundId.COVERING,
                        os.path.join('src', 'Assets/Sounds/Other/bed-sheet-movement_mjjnbdvo.mp3'),
                        0,
                        None,
                        None,
                        -1)

        def set_update_function(self, update):
            self._update = update

        @property
        def update(self):
            return self._update

        def none(self):
            pass

        # кроватка
        def dialog_bed1(self):

            if self._bed_dialog1.dialog_complete:
                self.set_update_function(self.information1)

            elif self._player.horizontale_testing_rect.colliderect(self._bed_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._bed_dialog1))
                self._soundmanager.all_pause()

        # не очень хочетса
        def dialog_bed2(self):

            if self._bed_dialog2.dialog_complete:
                self.set_update_function(self.wait1)

            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._bed_dialog2))

        # так то лучше
        def dialog_bed3(self):

            if self._bed_dialog3.dialog_complete:
                self.set_update_function(self.none)

            else:
                self._scene.uimanager.change_menu(Menus.DialogPanel(self._scene.camera.surface, self._bed_dialog3))


        #заправить
        def information1(self):

            if self._information1.information_complete:
                if self._information1.yes_button:
                    self.set_update_function(self.ic1_yes)
                    pass
                elif self._information1.no_button:
                    self.set_update_function(self.ic1_no)
                    pass
            else:
                self._scene.uimanager.change_menu(Menus.InformationPanel(self._scene.camera.surface, self._information1))
                self._soundmanager.all_pause()

        def ic1_yes(self):
            self.set_update_function(self.dialog_bed3)
            self._blanket.sprite.set_surface(self._blanket_surface_yes)
            self._blanket.sprite.set_needs_updated(True)
            self._soundmanager.add_sound(self._sound_covering)

        def ic1_no(self):
            self.set_update_function(self.dialog_bed2)

        def wait1(self):
            if self._player.horizontale_testing_rect.colliderect(self._bed_area) and \
                    self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and \
                    not self._game_logic_object.check_button_E_pressed:
                self._information1.restart()
                self.set_update_function(self.information1)
                self._soundmanager.all_pause()

    def __init__(self):

        GameLogic._object_gamelogic = self

        self._eventmanager = EventManager.EventManager()
        self._player: Player.Player = Player.Player()
        self._player_animation_old_state = None

        from src.Game.Managers import SoundManager

        self._soundmanager = SoundManager.SoundManager()
        self._shared_resources = SharedResources.SharedResources().shared_resources

        from src.Game.Scene import Scene
        self._scene: Scene.Scene = self._shared_resources.get('scene')

        self._check_button_E_pressed = True
        self._check_button_ESC_pressed = True
        self._check_button_U_pressed = True # кнопка отладки

        # self._flag_E = False
        # self._flag_ESC = False

        self._refrigerator_event = GameLogic.Refrigerator_event(self)
        self._tv_event = GameLogic.TV_event(self)
        self._mrcreeper_event = GameLogic.MrCreeper_event(self)
        self._bed_event = GameLogic.Bed_event(self)

        from src.Game import GameInfo
        self._gameinfo = GameInfo.GameInfo()

    def update(self):

        if self._eventmanager.search(Event.EventId.PLAYER_PRESS_U) and not self._check_button_U_pressed:
            if self._gameinfo.debugging_flag: self._gameinfo.set_debugging_flag(False)
            else: self._gameinfo.set_debugging_flag(True)

        self._player.player_movement_update()
        self._scene.camera.set_position(self._player.gameobject.rect.center)

        if self._eventmanager.search(Event.EventId.PlAYER_PRESS_ESC) and not self._check_button_ESC_pressed:
            from src.Game.UI import Menus

            # if self._scene:
            self._soundmanager.all_pause()
            self._scene.uimanager.change_menu(Menus.Play_Menu(self._scene.camera.surface))
            self._eventmanager.del_event(Event.Event(Event.EventId.PlAYER_PRESS_ESC))
            return None

        self._refrigerator_event.update()
        self._tv_event.update()
        self._mrcreeper_event.update()
        self._bed_event.update()

        self.check_pressed_button_update()

    def check_pressed_button_update(self):

        if self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and not self._check_button_E_pressed:
            self._check_button_E_pressed = True
        elif not self._eventmanager.search(Event.EventId.PLAYER_PRESS_E) and self._check_button_E_pressed:
            self._check_button_E_pressed = False

        if self._eventmanager.search(Event.EventId.PlAYER_PRESS_ESC) and not self._check_button_ESC_pressed:
            self._check_button_ESC_pressed = True
        elif not self._eventmanager.search(Event.EventId.PlAYER_PRESS_ESC) and self._check_button_ESC_pressed:
            self._check_button_ESC_pressed = False

        if self._eventmanager.search(Event.EventId.PLAYER_PRESS_U) and not self._check_button_U_pressed:
            self._check_button_U_pressed = True
        elif not self._eventmanager.search(Event.EventId.PLAYER_PRESS_U) and self._check_button_U_pressed:
            self._check_button_U_pressed = False

    @property
    def check_button_E_pressed(self):
        return self._check_button_E_pressed

    @property
    def check_button_ESC_pressed(self):
        return self._check_button_ESC_pressed

    @property
    def check_button_U_pressed(self):
        return self._check_button_U_pressed

    def set_check_button_E_pressed(self, value: bool):
        self._check_button_E_pressed = value

    def set_check_button_ESC_pressed(self, value: bool):
        self._check_button_ESC_pressed = value

    def set_check_button_U_pressed(self, value: bool):
        self._check_button_U_pressed = value