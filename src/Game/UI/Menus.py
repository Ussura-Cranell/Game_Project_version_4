import pygame.image
from src.Game.UI.Button import Button


class MainMenu:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen

        image = pygame.image.load(r'..\..\src\Assets\Sprites\74087bb27eb2d8984a558bbbd76ddef3.png').convert_alpha()
        image = MainMenu.size_image(image, 0.5)
        self._text_menu = [image, image.get_rect()]
        self._text_menu[1].top = min(image.get_size())*1.5
        self._text_menu[1].centerx = screen.get_rect().centerx


        self._buttons = []

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Play Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Play col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_BUTTON, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Settings Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Settings  col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.SETTING_BUTTON, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Exit Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Exit  col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EXIT_BUTTON, image_nothing, image_selected))


        num = 50
        for button in self._buttons[::-1]:
            button.rect.centerx = screen.get_rect().centerx
            button.rect.bottom = screen.get_rect().bottom - num
            num += button.rect.h + 20


        from src.Game.Managers import EventManager
        self._eventmanager = EventManager.EventManager()
        from src.Game.Event import Event
        self._eventid = Event.EventId
        from src.Game.Managers import SoundManager
        self._soundmanager = SoundManager.SoundManager()
        from src.Game.Sound import Sound
        self._soundid = Sound.SoundId
        self._soundstorage = Sound.SoundStorage()
        Sound.Sound(Sound.SoundId.SELECTED_BUTTON,
                    r'..\Assets\Sounds\UI\selected.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    r'..\Assets\Sounds\UI\enter.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        self._is_entered = False

    def draw(self):

        for button in self._buttons:
            if button.condition == Button.ButtonСondition.NOTHING:
                self._screen.blit(button.surface, button.rect)
            elif button.condition == Button.ButtonСondition.SELECRED:
                self._screen.blit(button.surface_selected, button.rect)
        self._screen.blit(self._text_menu[0], self._text_menu[1])

    def handle_events(self):

        bool = self._eventmanager.search(self._eventid.MOUSE_LEFT) is not None

        mouse_pos = pygame.mouse.get_pos()
        for button in self._buttons:
            if button.rect.collidepoint(*mouse_pos):
                if button.condition is not Button.ButtonСondition.SELECRED:
                    self._soundmanager.add_sound(self._soundstorage.get_sound(self._soundid.SELECTED_BUTTON))
                    button.set_condition(Button.ButtonСondition.SELECRED)
                elif bool and self._is_entered is False:
                    if button.button_id is not Button.ButtonId.SETTING_BUTTON:
                        self._is_entered = True
                        self._soundmanager.add_sound(self._soundstorage.get_sound(self._soundid.ENTERED_BUTTON))
                        return button.button_id
            else:
                button.set_condition(Button.ButtonСondition.NOTHING)

    @classmethod
    def size_image(cls, surface: pygame.Surface, size: float) -> pygame.Surface:
        return pygame.transform.scale(surface, (surface.get_size()[0] * size, surface.get_size()[1] * size))

class SettingsMenu:
    def __init__(self):
        # Инициализация элементов меню настроек
        pass
    def draw(self, screen):
        # Отрисовка элементов меню настроек на экране
        pass
    def handle_events(self):
        # Обработка событий для меню настроек
        # Переключение состояний, если нужно
        pass


class Play:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        self._buttons = []

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\episode1.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\color episode1.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_1, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\episode2.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\color episode2.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_2, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\episode3.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Episode\color episode3.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_3, image_nothing, image_selected))

        num = 200
        for button in self._buttons[::-1]:
            button.rect.centerx = screen.get_rect().centerx
            button.rect.bottom = screen.get_rect().bottom - num
            num += button.rect.h + 50

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Back Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Back  col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.4)
        image_selected = MainMenu.size_image(image_selected, 0.4)
        button = Button.Button(Button.ButtonId.BACK_BUTTON, image_nothing, image_selected)
        self._buttons.append(button)
        button.rect.top += 50
        button.rect.left += 50

        from src.Game.Managers import EventManager
        self._eventmanager = EventManager.EventManager()
        from src.Game.Event import Event
        self._eventid = Event.EventId
        from src.Game.Managers import SoundManager
        self._soundmanager = SoundManager.SoundManager()
        from src.Game.Sound import Sound
        self._soundid = Sound.SoundId
        self._soundstorage = Sound.SoundStorage()

        Sound.Sound(Sound.SoundId.SELECTED_BUTTON,
                    r'..\Assets\Sounds\UI\selected.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    r'..\Assets\Sounds\UI\enter.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        self._is_entered = False

    def draw(self):
        for button in self._buttons:
            if button.condition == Button.ButtonСondition.NOTHING:
                self._screen.blit(button.surface, button.rect)
            elif button.condition == Button.ButtonСondition.SELECRED:
                self._screen.blit(button.surface_selected, button.rect)

    def handle_events(self):
        from src.Game.UI.Button import Button
        if self._eventmanager.search(self._eventid.PlAYER_PRESS_ESC):

            return Button.ButtonId.BACK_BUTTON
        bool = self._eventmanager.search(self._eventid.MOUSE_LEFT) is not None

        mouse_pos = pygame.mouse.get_pos()
        # print(f'mouse_pos: {mouse_pos}')

        for button in self._buttons:
            if button.rect.collidepoint(*mouse_pos):
                if button.condition is not Button.ButtonСondition.SELECRED:
                    sound = self._soundstorage.get_sound(self._soundid.SELECTED_BUTTON)
                    self._soundmanager.add_sound(sound)
                    button.set_condition(Button.ButtonСondition.SELECRED)
                elif bool and self._is_entered is False:
                    self._is_entered = True
                    self._soundmanager.add_sound(self._soundstorage.get_sound(self._soundid.ENTERED_BUTTON))
                    return button.button_id
            else:
                button.set_condition(Button.ButtonСondition.NOTHING)

class Close:
    def __init__(self, screen: pygame.Surface):
        pass

    def draw(self):
        pass

    def handle_events(self):
        pass

class Play_Menu:
    def __init__(self, screen: pygame.Surface):
        pass
        print(f'play menu init')
        from src.Game.Managers import EventManager
        self._eventmanager = EventManager.EventManager()
        from src.Game.Managers import SoundManager
        self._soundmanager = SoundManager.SoundManager()

        from src.Game.Event import Event
        self._eventid = Event.EventId
        self._event = Event.Event
        self._screen: pygame.Surface = screen
        self._screen_night = pygame.Surface(size=self._screen.get_size(), flags=pygame.SRCALPHA)
        self._buttons = []

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Continue Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Continue  col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_CONTINUE_MENU, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Quit Button.png').convert_alpha()
        image_selected = pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Quit  col_Button.png').convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_QUIT_MENU, image_nothing, image_selected))

        num = 200
        for button in self._buttons[::-1]:
            button.rect.centerx = screen.get_rect().centerx
            button.rect.bottom = screen.get_rect().bottom - num
            num += button.rect.h + 50

        from src.Game.Sound import Sound
        self._soundstorage = Sound.SoundStorage()
        self._soundid = Sound.SoundId

        Sound.Sound(Sound.SoundId.SELECTED_BUTTON,
                    r'..\Assets\Sounds\UI\selected.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    r'..\Assets\Sounds\UI\enter.mp3',
                    0,
                    screen.get_rect().center,
                    screen.get_rect().center,
                    max(screen.get_rect().size))

        self._is_entered = False

    def draw(self):
        print(f'play menu draw')
        self._screen_night.fill((0, 0, 0, 200))
        self._screen.blit(self._screen_night, self._screen_night.get_rect())
        for button in self._buttons:
            if button.condition == Button.ButtonСondition.NOTHING:
                self._screen.blit(button.surface, button.rect)
            elif button.condition == Button.ButtonСondition.SELECRED:
                self._screen.blit(button.surface_selected, button.rect)

    def handle_events(self):
        print(f'play menu update')

        from src.Game.UI.Button import Button

        if self._eventmanager.search(self._eventid.PlAYER_PRESS_ESC):
            self._eventmanager.del_event(self._event(self._eventid.PlAYER_PRESS_ESC))
            return Button.ButtonId.PLAY_CONTINUE_MENU
        bool = self._eventmanager.search(self._eventid.MOUSE_LEFT) is not None

        mouse_pos = pygame.mouse.get_pos()

        for button in self._buttons:
            if button.rect.collidepoint(*mouse_pos):
                if button.condition is not Button.ButtonСondition.SELECRED:
                    sound = self._soundstorage.get_sound(self._soundid.SELECTED_BUTTON)
                    self._soundmanager.add_sound(sound)
                    button.set_condition(Button.ButtonСondition.SELECRED)
                elif bool and self._is_entered is False:
                    self._is_entered = True
                    self._soundmanager.add_sound(self._soundstorage.get_sound(self._soundid.ENTERED_BUTTON))
                    pygame.time.delay(400)

                    print(f'entered id button: {button.button_id}')
                    return button.button_id
            else:
                button.set_condition(Button.ButtonСondition.NOTHING)