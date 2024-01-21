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

        from . import SharedResources, SceneInitialization, GameLogic

        shared_resources = SharedResources.SharedResources()
        scene_init = SceneInitialization.SceneInitialization()
        scene = scene_init.scene
        gamelogic = GameLogic.GameLogic()

        while self._game_run:
            window.clear_console()

            if isinstance(scene.uimanager.current_menu, Menus.Close):

                inputevent.update()
                gamelogic.update()
                soundmanager.update()
                animationmanager.update()

                if gameinfo.debugging_flag: scene.testing_barriers()
                else: scene.update()

                screen.blit(scene.camera.surface, scene.camera.rect)
                pygame.display.flip()

                window.clock.tick(22)

            elif isinstance(scene.uimanager.current_menu, Menus.Play_Menu):
                window.clear_console()
                # print(f'игра временно на паузе, подыши и расслабься')
                inputevent.update()
                soundmanager.update()
                scene.update()
                screen.blit(scene.camera.surface, scene.camera.rect)
                pygame.display.flip()

            elif isinstance(scene.uimanager.current_menu, Menus.DialogPanel) or \
                    isinstance(scene.uimanager.current_menu, Menus.InformationPanel):
                window.clear_console()
                # print(f'Игровой диалог')
                inputevent.update()
                # animationmanager.update()
                # inputevent.track_only_dialog_keys()
                soundmanager.update()
                scene.update()
                screen.blit(scene.camera.surface, scene.camera.rect)
                pygame.display.flip()
                window.clock.tick(25)

            elif isinstance(scene.uimanager.current_menu, Menus.MainMenu):
                from src.Game.UI.Button import Button
                self._mode = Button.ButtonId.PLAY_QUIT_MENU
                self._game_run = False

                pygame.time.delay(500)

            print(f'FPS: {window.clock.get_fps():.0f}')
            print(f'Memory used: {gameinfo.takes_MB} MB')

    @property
    def mode(self) -> int:
        return self._mode
