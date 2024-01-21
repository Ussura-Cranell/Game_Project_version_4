import pygame.display


class Init:
    def __init__(self):
        self._mode = 0
        self._game_run = True

    def start(self):

        from src.Game.Managers import AnimationManager, SoundManager
        from src.Game.Event import InputEvent
        from src.Game.Window import Window
        from src.Game import GameInfo
        from src.Game.Scene import Scene
        from src.Game.UI import Menus

        animationmanager = AnimationManager.AnimationManager()
        soundmanager = SoundManager.SoundManager()
        gameinfo = GameInfo.GameInfo()
        window = Window.Window()
        inputevent = InputEvent.InputEvent()
        soundmanager.update()
        animationmanager.update()

        screen = window.screen
        scene = Scene.Scene((gameinfo.screen_size), Menus.MainMenu)

        while self._game_run:

            window.clear_console()

            inputevent.update()
            soundmanager.update()
            animationmanager.update()
            scene.update()
            screen.blit(scene.camera.surface, scene.camera.rect)
            pygame.display.flip()

            # print(f'Main menu')
            print(f'FPS: {window.clock.get_fps()}')
            print(f'Memory used: {gameinfo.takes_MB} MB')

            if type(scene.uimanager.current_menu) is Menus.Close:

                self._mode = scene.uimanager.button_id
                scene.reset()
                self._game_run = False

            window.clock.tick(30)

    @property
    def mode(self) -> int:
        return self._mode