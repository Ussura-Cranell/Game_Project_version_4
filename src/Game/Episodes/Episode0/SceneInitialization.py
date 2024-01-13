from typing import Tuple, List
import pygame.image
import os


class SceneInitialization:
    def __init__(self, shared_resources: dict):

        def create_barrier(id: List[int], group, point_reference, ltop_pos: Tuple[int, int], x: int = 1, y: int = 1):
            from src.Game.GameObject.StaticObject import Trigger
            group.add(Trigger.Trigger(name=str(id[0]),
                                      pos=(point_reference[0] + ltop_pos[0], point_reference[1] + ltop_pos[1]),
                                      size=(x, y)))
            id[0] += 1

        def create_level_decoration(name: str, layer: int, size: Tuple[int, int],
                                    point_reference: Tuple[int, int],
                                    pos: Tuple[int, int]):
            from src.Game.GameObject.StaticObject import Decoration
            decoration = Decoration.Decoration(name=name, layer=layer, size=size)
            print(f'name: {name}')

            image = pygame.image.load(os.path.join('src', 'Assets/Episodes/Episode0/level/') + name).convert_alpha()
            decoration.sprite.set_surface(image)
            decoration.sprite.rect.topleft = (point_reference[0] + pos[0], point_reference[1] + pos[1])

        def create_object_barrier(id: List[int],
                                      name: str,
                                      layer: int,
                                      group,
                                      point_reference,
                                      ltop_pos: Tuple[int, int],
                                      size: Tuple[int, int],
                                      h_rect:int):

            from src.Game.GameObject.StaticObject import Decoration
            decoration = Decoration.Decoration(name=name, layer=layer, size=size, pos=(point_reference[0] + ltop_pos[0], point_reference[1] + ltop_pos[1]))

            image = pygame.image.load(os.path.join('src', 'Assets/Episodes/Episode0/level/objects/') + name).convert_alpha()
            decoration.sprite.set_surface(image)
            id[0] += 1
            from src.Game.GameObject.StaticObject import Trigger
            trigger = Trigger.Trigger(name=str(id[0]),
                                      pos=(point_reference[0] + ltop_pos[0], point_reference[1] + ltop_pos[1]),
                                      size=size)
            old_bottom = trigger.gameobject.rect.bottom
            trigger.gameobject.rect.size = (trigger.gameobject.rect.width, h_rect)
            trigger.gameobject.rect.bottom = old_bottom
            group.add(trigger)
            return trigger

        self._shared_resources = shared_resources

        from src.Game.Scene import Scene
        from src.Game.UI import Menus
        from src.Game import GameInfo
        from src.Game.Sprite import Sprite
        from src.Game.Animation import Animaton
        from src.Game.GameObject.Entity import Player
        from src.Game.Managers import AnimationManager

        from src.Game.Tools import Multitool

        animationmanager = AnimationManager.AnimationManager()

        gameinfo = GameInfo.GameInfo()

        self._scene = Scene.Scene(gameinfo.screen_size, Menus.Close)
        self._sprite = Sprite
        self._sprite.Sprite.set_scene(self._scene)

        point_reference = [300, 100]

        # загрузка уровня -----------------------------------------------------------------------------

        create_level_decoration(name='decoration/floor694x564.png', layer=0, size=(694, 564), point_reference=point_reference, pos=(0, 0))
        create_level_decoration(name='bathroom corner.png', layer=2, size=(44, 564), point_reference=point_reference, pos=(32, 227))
        create_level_decoration(name='child walls.png', layer=2, size=(288, 64), point_reference=point_reference, pos=(78, 311))
        create_level_decoration(name='exit walls.png', layer=2, size=(296, 64), point_reference=point_reference, pos=(366, 437))
        create_level_decoration(name='kitchen walls.png', layer=2, size=(256, 64), point_reference=point_reference, pos=(303, 173))
        create_level_decoration(name='passage wall.png', layer=2, size=(30, 32), point_reference=point_reference, pos=(178, 247))
        create_level_decoration(name='passage wall.png', layer=2, size=(30, 32), point_reference=point_reference, pos=(664, 308))
        create_level_decoration(name='walls.png', layer=0, size=(694, 564), point_reference=point_reference, pos=(0, 0))
        create_level_decoration(name='down shadow.png', layer=3, size=(54, 12), point_reference=point_reference, pos=(481, 552))
        create_level_decoration(name='right shadow.png', layer=4, size=(54, 12), point_reference=point_reference, pos=(663, 256))

        # доп

        create_level_decoration(name='decoration/hallway115x75.png', layer=1, size=(115, 75),
                                point_reference=point_reference, pos=(447, 455))
        create_level_decoration(name='decoration/living room background222x260.png', layer=1, size=(222, 260),
                                point_reference=point_reference, pos=(415, 183))
        create_level_decoration(name='decoration/kitchen background234x84.png', layer=0, size=(234, 84),
                                point_reference=point_reference, pos=(310, 0))
        create_level_decoration(name='decoration/bathroom background145x110.png', layer=0, size=(145, 110),
                                point_reference=point_reference, pos=(29, 84))
        create_level_decoration(name='decoration/badroom background262x173.png', layer=0, size=(262, 173),
                                point_reference=point_reference, pos=(72, 321))

        # барьеры -------------------------------------------------------------------------------------------------

        barriers, id = set(), [1]

        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(31, 128), y=131)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(32, 259), x=45)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(77, 260), y=237)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(78, 497), x=256)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(334, 375), y=122)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(365, 375), y=126)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(433, 501), y=51)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(434, 552), x=46)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(480, 553), y=8)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(481, 561), x=54)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(535, 553), y=8)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(536, 552), x=53)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(589, 501), y=51)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(662, 341), y=160)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(663, 340), x=29)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(692, 308), y=33)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(663, 307), x=29)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(662, 237), y=70)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(559, 63), y=173)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(303, 62), x=256)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(302, 63), y=173)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(176, 128), y=108)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(32, 127), x=144)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(176, 280), y=94)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(207, 280), y=94)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(177, 279), x=30)
        ###
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(78, 374), x=181)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(315, 374), x=50)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(366, 500), x=114)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(536, 500), x=126)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(177, 236), x=161)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(394, 236), x=268)

        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(79, 349), x=32, y=77)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(112, 361), x=28, y=36)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(141, 374), x=30, y=19)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(172, 374), x=24, y=8)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(197, 374), x=60, y=22)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(308, 466), x=26, y=28)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(33, 128), x=40, y=62)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(79, 116), x=62, y=39)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(148, 128), x=24, y=24)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(310, 63), x=234, y=21)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(474, 222), x=116, y=38)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(593, 237), x=32, y=15)
        create_barrier(id=id, group=barriers, point_reference=point_reference, ltop_pos=(534, 502), x=22, y=14)

        # декорации с барьером

        create_object_barrier(id, 'christmas tree80x111.png', 2, barriers, point_reference, (376, 322), (80, 111), 60)
        create_object_barrier(id, 'the left sofa44x82.png', 2, barriers, point_reference, (452, 250), (44, 82), 50)
        create_object_barrier(id, 'the lower sofa96x54.png', 2, barriers, point_reference, (506, 305), (96, 54), 40)
        create_object_barrier(id, 'table living room40x54.png', 2, barriers, point_reference, (512, 243), (40, 54), 25)
        create_object_barrier(id, 'the table in the kitchen175x68.png', 2, barriers, point_reference, (388, 104), (175, 68), 30)
        dop_setting = create_object_barrier(id, 'plant44x60.png', 2, barriers, point_reference, (154, 183), (44, 60), 20)
        old_center_pos_rect = dop_setting.gameobject.rect.center
        dop_setting.gameobject.rect.size = (20, dop_setting.gameobject.rect.height)
        dop_setting.gameobject.rect.center = old_center_pos_rect
        create_object_barrier(id, 'washing machine56x82.png', 2, barriers, point_reference, (79, 221), (56, 82), 30)
        create_object_barrier(id, 'badroom drums90x56.png', 2, barriers, point_reference, (92, 428), (90, 56), 30)
        create_object_barrier(id, 'table with a book32x91.png', 2, barriers, point_reference, (307, 376), (32, 91), 65)
        create_object_barrier(id, 'armchair38x52.png', 2, barriers, point_reference, (268, 402), (38, 52), 25)
        create_object_barrier(id, 'duck56x67.png', 2, barriers, point_reference, (46, 192), (56, 67), 20)

        # проверка количества барьеров
        print(f'len barriesr: {len(barriers)}')

        # проверка пересечений барьеров
        for barrier1 in barriers:
            for barrier2 in barriers:
                if barrier1 != barrier2:
                    if barrier1.gameobject.rect.colliderect(barrier2.gameobject.rect):
                        print(f'пересечение {barrier1.gameobject.name} и {barrier2.gameobject.name}')
                        #exit()
        # exit()

        self._shared_resources['barriers'] = barriers

        # загрузка игрока -------------------------------------------------------------------------------------------

        player = Player.Player(name='Testing Player 1', size=(47, 45), layer=2)
        self._scene.get_layer(2).set_drawing_by_coordinates(True)
        player.set_movement_speed(5)


        player_animation_sheet = pygame.image.load(os.path.join('src', 'Assets/Sprites/Entity/Human/player47x45.png'))
        running_player_animation_chunks = Multitool.x_y_transform_spritesheet_to_animation(
            player_animation_sheet, (47, 45))

        # инвертирую направления анимации
        running_player_animation_chunks += [pygame.transform.flip(chunk, True, False) for chunk in
                                            running_player_animation_chunks[0:9:]]
        running_player_animation_chunks += [pygame.transform.flip(chunk, True, False) for chunk in
                                            running_player_animation_chunks[9:18:]]
        running_player_animation_chunks += [pygame.transform.flip(chunk, True, False) for chunk in
                                            running_player_animation_chunks[27:36:]]

        running_player_animation_chunks = [Multitool.change_scale_image_index(chunk, 1.25) for chunk in
                                           running_player_animation_chunks]
        player.sprite.rect.size = running_player_animation_chunks[0].get_size()

        player_animation_sequence = [Animaton.AnimationId.PLAYER_MOVE_DOWN_RIGHT,
                                     Animaton.AnimationId.PLAYER_MOVE_UP_RIGHT,
                                     Animaton.AnimationId.PLAYER_MOVE_DOWN,
                                     Animaton.AnimationId.PLAYER_MOVE_RIGHT,
                                     Animaton.AnimationId.PLAYER_MOVE_UP,
                                     Animaton.AnimationId.PLAYER_MOVE_DOWN_LEFT,
                                     Animaton.AnimationId.PLAYER_MOVE_UP_LEFT,
                                     Animaton.AnimationId.PLAYER_MOVE_LEFT]

        num_flag_animation = 0
        for id_animation in player_animation_sequence:
            animation = Animaton.Animation(id_animation,
                                           running_player_animation_chunks[num_flag_animation:num_flag_animation + 9],
                                           0,
                                           True,
                                           2,
                                           True)
            player.add_animation(id_animation, animation)
            num_flag_animation += 9

        player.set_current_animation(Animaton.AnimationId.PLAYER_MOVE_DOWN)
        animationmanager.add_animation_entity(player)
        print(animationmanager)

        player.gameobject.rect.topright = self._scene.surface.get_rect().center
        self._shared_resources['player'] = player

        print(player.animations)
        # exit()

        from src.Game.GameObject.Entity import Entity
        tv = Entity.Entity(name=str(id), layer=3, size=(50, 22))
        tv.sprite.rect.topleft = (point_reference[0] + 524, point_reference[1] + 200)

        dance_9mm = pygame.image.load(os.path.join('src', 'Assets/testAnimations/dancespritesheet.png'))
        dance_9mm = Multitool.x_y_transform_spritesheet_to_animation(dance_9mm, (50, 22))
        # exit()

        animation = Animaton.Animation(id_animation.ANIMATION_1,
                                           dance_9mm,
                                           0,
                                           True,
                                           2,
                                           False)
        tv.add_animation(id_animation.ANIMATION_1, animation)

        surface = pygame.Surface((50, 22))
        surface.fill('black')
        animation = Animaton.Animation(id_animation.NONE,
                                       [surface],
                                       0,
                                       False,
                                       2,
                                       False)
        tv.add_animation(id_animation.NONE, animation)

        tv.set_current_animation(id_animation.NONE)
        animationmanager.add_animation_entity(tv)
        self._shared_resources['tv'] = tv


        from src.Game.Sound import Sound
        from src.Game.Managers import SoundManager
        self._soundstorage = Sound.SoundStorage()
        self._soundmanager = SoundManager.SoundManager()
        tv_music = Sound.Sound(Sound.SoundId.Memphis_Cult9Mm,
                               os.path.join('src', 'Assets/Music/Memphis Cult - 9MM (Lyrics) _ watch my 9mm go bang (256  kbps).mp3'),
                               0,
                               self.scene.surface.get_rect().center,
                               tv.sprite.rect.center,
                               400)
        self._soundstorage.add_sound(Sound.SoundId.Memphis_Cult9Mm, tv_music)

        self._shared_resources['soundstorage'] = self._soundstorage
        self._shared_resources['tv_music'] = tv_music

        from src.Game.GameObject.StaticObject import Trigger
        self._shared_resources['tv_trigger'] = Trigger.Trigger('tv_trigger',
                                                               (point_reference[0] + 496,
                                                                point_reference[1] + 240),
                                                               (96, 45))

        from src.Game.GameObject.Entity import Entity
        spikers = Entity.Entity(name=str(id), layer=1, size=(32, 64))
        spikers.sprite.rect.topleft = (point_reference[0] + 593, point_reference[1] + 188)

        spikers_animation = pygame.image.load(os.path.join('src', 'Assets/testAnimations/spikers.png'))
        spikers_animation = Multitool.x_y_transform_spritesheet_to_animation(spikers_animation, (32, 64))

        animation = Animaton.Animation(id_animation.ANIMATION_1,
                                       spikers_animation,
                                       0,
                                       True,
                                       2,
                                       False)
        spikers.add_animation(id_animation.ANIMATION_1, animation)
        animation = Animaton.Animation(id_animation.NONE,
                                       [spikers_animation[0]],
                                       0,
                                       False,
                                       2,
                                       False)
        spikers.add_animation(id_animation.NONE, animation)

        spikers.set_current_animation(id_animation.NONE)
        animationmanager.add_animation_entity(spikers)
        self._shared_resources['spikers'] = spikers

        character_steps = Sound.Sound(Sound.SoundId.SOUND_PLAYER_STEP,
                               os.path.join('src', 'Assets/Sounds/Other/player steps4.mp3'),
                               -1,
                               self.scene.surface.get_rect().center,
                               self.scene.surface.get_rect().center,
                               -1)
        self._shared_resources['sound_step'] = character_steps

    @property
    def scene(self):
        return self._scene

    @property
    def shared_resources(self):
        return self._shared_resources
