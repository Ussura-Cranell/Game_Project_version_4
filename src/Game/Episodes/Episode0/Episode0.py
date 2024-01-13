from typing import Set
from src.Game.UI import Menus


class Init:
    def __init__(self):
        self._mode = 0
        self._game_run = True

    def start(self):
        from src.Game.Managers import AnimationManager, ObjManager, SoundManager, EventManager
        from src.Game.Event import InputEvent
        from src.Game.Window import Window
        from src.Game import GameInfo
        from src.Game.UI.Button import Button
        import pygame

        buttonid = Button.ButtonId
        objectmanager = ObjManager.GameObjectManager()
        animationmanager = AnimationManager.AnimationManager()
        soundmanager = SoundManager.SoundManager()
        eventmanager = EventManager.EventManager()
        gameinfo = GameInfo.GameInfo()
        window = Window.Window()
        inputevent = InputEvent.InputEvent()
        soundmanager.update()
        animationmanager.update()
        screen = window.screen

        self._shared_resources = {}
        self._shared_resources['animationmanager'] = animationmanager

        from src.Game.Episodes.Episode0 import SceneInitialization
        scene_init = SceneInitialization.SceneInitialization(self._shared_resources) # инициализация сцены

        from . import GameLogic
        gamelogic = GameLogic.GameLogic(self._shared_resources) # инициализация обработки событий

        scene = scene_init.scene
        scene.camera.set_zoom(-0.65)
        self._shared_resources['scene'] = scene

        from src.Game.GameObject.Entity import Player
        player: Player.Player = self._shared_resources.get('player')
        from src.Game.GameObject.StaticObject import Trigger
        barriers: Set[Trigger.Trigger] = self._shared_resources.get('barriers')

        while self._game_run:
            window.clear_console()

            if isinstance(scene.uimanager.current_menu, Menus.Close):
                # print(animationmanager)
                # print(soundmanager)

                scene.camera.set_position(player.gameobject.rect.center)

                inputevent.update()
                gamelogic.update()
                soundmanager.update()
                animationmanager.update()
                scene.update()
                # scene.testing_barriers(barriers, self._shared_resources.get('verticale_testing_rect'), self._shared_resources.get('horizontale_testing_rect'))
                screen.blit(scene.camera.surface, scene.camera.rect)
                pygame.display.flip()

                window.clock.tick(60)

            elif isinstance(scene.uimanager.current_menu, Menus.Play_Menu):
                window.clear_console()
                # print(f'игра временно на паузе, подыши и расслабься')
                inputevent.update()
                soundmanager.update()
                scene.update()
                screen.blit(scene.camera.surface, scene.camera.rect)
                pygame.display.flip()

            elif isinstance(scene.uimanager.current_menu, Menus.MainMenu):
                return scene.uimanager.button_id.PLAY_QUIT_MENU

            print(f'FPS: {window.clock.get_fps()}')
            print(f'Memory used: {gameinfo.takes_MB} MB')
