import pygame

from src.Game.UI import Menus
from src.Game.UI.Button import Button



class UIManager:
    def __init__(self, camera, current_menu):
        from src.Game.Scene.Camera import Camera
        from src.Game.Managers import SoundManager
        import pygame

        self._time = pygame.time
        self._current_menu = current_menu(camera.surface) # Начальное состояние
        self._camera: Camera.Camera = camera
        self._buttonid: Button.ButtonId = Button.ButtonId
        self._soundmanager = SoundManager.SoundManager()

    @property
    def current_menu(self):
        return self._current_menu

    @property
    def button_id(self):
        return self._buttonid

    def change_menu(self, new_menu):
        # Метод для изменения текущего окна меню
        self._current_menu = new_menu

    def update(self):
        # Отрисовка текущего окна меню
        self.handle_events()
        self.current_menu.draw()

    def handle_events(self):
        # Обработка событий текущего окна меню
        num = self.current_menu.handle_events()
        if num is self._buttonid.PLAY_BUTTON:
            self._time.delay(100)
            self.change_menu(Menus.Play(self._camera.surface))

        elif num is self._buttonid.EXIT_BUTTON:
            self._time.delay(500)
            from src.Game import GameInfo
            GameInfo.GameInfo().reset_all()
            print(f'MEMORY USED: {GameInfo.GameInfo().takes_MB}')
            pygame.quit()
            exit(0)

        elif num is self._buttonid.BACK_BUTTON:
            self._time.delay(100)
            self.change_menu(Menus.MainMenu(self._camera.surface))

        elif num is self._buttonid.EPISODE_1:
            self._time.delay(500)
            self._buttonid = self._buttonid.EPISODE_1
            self.change_menu(Menus.Close(self._camera.surface))

        elif num is self._buttonid.EPISODE_2:
            self._time.delay(500)
            self._buttonid = self._buttonid.EPISODE_2
            self.change_menu(Menus.Close(self._camera.surface))

        elif num is self._buttonid.EPISODE_3:
            self._time.delay(500)
            self._buttonid = self._buttonid.EPISODE_3
            self.change_menu(Menus.Close(self._camera.surface))

        elif num is self._buttonid.PLAY_CONTINUE_MENU:
            self.change_menu(Menus.Close(self._camera.surface))
            print("PLAY_MENU!")

        elif num is self._buttonid.PLAY_QUIT_MENU:
            print("PLAY_QUIT_MENU")
            self.change_menu(Menus.MainMenu(self._camera.surface))


    def __str__(self):
        return f'current_menu: {self._current_menu}'

