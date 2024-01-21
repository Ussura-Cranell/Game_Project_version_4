import random
import pygame.image
from src.Game.UI.Button import Button
import os


class MainMenu:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        screen.fill((10, 10, 10))
        image = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/74087bb27eb2d8984a558bbbd76ddef3.png')).convert_alpha()
        image = MainMenu.size_image(image, 0.5)
        self._text_menu = [image, image.get_rect()]
        self._text_menu[1].top = min(image.get_size()) * 1.5
        self._text_menu[1].centerx = screen.get_rect().centerx
        self._buttons = []

        image_nothing = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Play Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Play col_Button.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_BUTTON, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Settings Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Settings  col_Button.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.SETTING_BUTTON, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Exit Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Exit  col_Button.png')).convert_alpha()
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
                    os.path.join('src', 'Assets/Sounds/UI/selected.mp3'),
                    0,
                    None,
                    None,
                    -1)

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    os.path.join('src', 'Assets/Sounds/UI/enter.mp3'),
                    0,
                    None,
                    None,
                    -1)
        SoundManager.SoundManager().reset()
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
        return pygame.transform.scale(surface, (int(surface.get_size()[0] * size), int(surface.get_size()[1] * size)))

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
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/episode1.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/color episode1.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_1, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/episode2.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/color episode2.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_2, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/episode3.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Episode/color episode3.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.EPISODE_3, image_nothing, image_selected))

        num = 200
        for button in self._buttons[::-1]:
            button.rect.centerx = screen.get_rect().centerx
            button.rect.bottom = screen.get_rect().bottom - num
            num += button.rect.h + 50

        image_nothing = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Back Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Back  col_Button.png')).convert_alpha()
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
                    os.path.join('src', 'Assets/Sounds/UI/selected.mp3'),
                    0,
                    None,
                    None,
                    -1)

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    os.path.join('src', 'Assets/Sounds/UI/enter.mp3'),
                    0,
                    None,
                    None,
                    -1)

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
        # print(f'play menu init')
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
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Continue Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Continue  col_Button.png')).convert_alpha()
        image_nothing = MainMenu.size_image(image_nothing, 0.5)
        image_selected = MainMenu.size_image(image_selected, 0.5)
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_CONTINUE_MENU, image_nothing, image_selected))

        image_nothing = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Large Buttons/Quit Button.png')).convert_alpha()
        image_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Large Buttons/Colored Large Buttons/Quit  col_Button.png')).convert_alpha()
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
                    os.path.join('src', 'Assets/Sounds/UI/selected.mp3'),
                    0,
                    None,
                    None,
                    -1)

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    os.path.join('src', 'Assets/Sounds/UI/enter.mp3'),
                    0,
                    None,
                    None,
                    -1)

        self._is_entered = False

    def draw(self):
        # print(f'play menu draw')
        self._screen_night.fill((0, 0, 0, 200))
        self._screen.blit(self._screen_night, self._screen_night.get_rect())
        for button in self._buttons:
            if button.condition == Button.ButtonСondition.NOTHING:
                self._screen.blit(button.surface, button.rect)
            elif button.condition == Button.ButtonСondition.SELECRED:
                self._screen.blit(button.surface_selected, button.rect)

    def handle_events(self):
        # print(f'play menu update')

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

                    # print(f'entered id button: {button.button_id}')
                    return button.button_id
            else:
                button.set_condition(Button.ButtonСondition.NOTHING)

from . import Dialog
class DialogPanel():
    def __init__(self, screen: pygame.Surface, dialog:Dialog.Dialog):

        from src.Game.Managers import EventManager
        from src.Game.Event import Event
        self._eventmanager = EventManager.EventManager()
        self._eventid = Event.EventId

        from src.Game.Managers import SoundManager
        from src.Game.Sound import Sound
        self._soundmanager = SoundManager.SoundManager()
        self._sound = Sound

        if self._eventmanager.search(self._eventid.PLAYER_PRESS_E):
            self._eventmanager.del_event(self._eventmanager.del_event(Event.Event(self._eventid.PLAYER_PRESS_E)))
            #

        self._screen = screen
        self._dialog = dialog

        import os
        #r'D:\программирование\python\GameV4\src\Assets\Sprites\UIDialog\dialogpanel.png'
        self._dialog_panel = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/') + 'dialogpanel.png').convert_alpha()
        self._dialog_panel = pygame.transform.scale(self._dialog_panel, (151*6, 45*6))
        self._rect_dialog_panel = self._dialog_panel.get_rect()
        self._rect_dialog_panel.bottom = self._screen.get_rect().bottom - 25
        self._rect_dialog_panel.centerx = self._screen.get_rect().centerx
        # print(f'_rect_dialog_panel:{self._rect_dialog_panel}')


        # surface текста на панели диалога - общего
        self._rect_text_surface = pygame.Rect(self._rect_dialog_panel)
        self._rect_text_surface.topleft = (self._rect_text_surface.topleft[0] + 50*6, self._rect_text_surface.topleft[1] + 5*6)
        # print(f'_rect_text_surface:{self._rect_text_surface}')
        # exit()
        self._rect_text_surface.size = (95*6, 35*6)
        self._text_surface = pygame.Surface(self._rect_text_surface.size, flags=pygame.SRCALPHA)
        # self._text_surface.fill((83, 5, 250, 100))
        self._text_surface.fill((0, 0, 0, 0))

        # surface icon на панели диалога - общего
        self._rect_icon_surface = pygame.Rect(self._rect_dialog_panel)
        self._rect_icon_surface.topleft = (
        self._rect_icon_surface.topleft[0] + 4 * 6 , self._rect_text_surface.topleft[1] - 1 * 6)
        self._rect_icon_surface.size = (41 * 6, 37 * 6)
        # self._icon_surface = pygame.Surface(self._rect_icon_surface.size, flags=pygame.SRCALPHA)
        # self._icon_surface = self._dialog.current_icon
        self._icon_surface = pygame.transform.scale(self._dialog.current_icon, (41 * 6, 37 * 6))
        # self._icon_surface = self._dialog.current_icon
        # self._icon_surface.fill((83, 5, 250, 100))

        self._current_text_index = 0

        self._the_whole_text = '' # аналогия с surface text общего назначения
        self._current_line = ''
        self._line_indentation = 0 # отступ строки

        self._flag_dialogue_over = False
        self._flag_waiting_input = False
        self._flag_check_press_E = False
        self._char = ''

        self._screen_night = pygame.Surface(size=self._screen.get_size(), flags=pygame.SRCALPHA)
        self._screen_night.fill((0, 0, 0, 200))
        self._delay_part = 0

        self._continue_surface = pygame.image.load(os.path.join('src', 'Assets/Sprites/UIDialog/') + 'continue.png').convert_alpha()
        self._continue_surface = pygame.transform.scale(self._continue_surface, (48, 48))
        self._continue_surface_rect = pygame.Rect(self._continue_surface.get_rect())
        self._continue_surface_rect.bottomright = self._rect_dialog_panel.bottomright
        self._continue_surface_rect.x -= 40
        self._continue_surface_rect.y -= 30

        self._continue_surface_flag = False

    def draw(self):
        # print(f'dialog draw')
        # print(f'dialog panel')

        self._screen.blit(self._screen_night, self._screen_night.get_rect())
        self._screen.blit(self._dialog_panel, self._rect_dialog_panel)
        self._screen.blit(self._text_surface, self._rect_text_surface)
        self._screen.blit(self._icon_surface, self._rect_icon_surface)

        if self._continue_surface_flag:
            self._screen.blit(self._continue_surface, self._continue_surface_rect)

        # print(f'dialog text:\n{self._the_whole_text}')
        pass

    def handle_events(self):
        # print(f'dialog handle_events')


        # if self._eventmanager.search(self._eventid.PLAYER_PRESS_E) and self._flag_check_press_E:
        #     # игрок зажал клавишу E
        #     pass

        # if self._eventmanager.search(self._eventid.PlAYER_PRESS_ESC):
        #     self._eventmanager.del_event(self._eventid.PlAYER_PRESS_ESC)
        #     print(f'Выход из диалога (диалог не завершен)')
        #     if self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
        #         self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)
        #     from src.Game.UI.Button import Button
        #     self._dialog.reset()
        #     return Button.ButtonId.PLAY_CONTINUE_MENU
        #     # exit()

        if self._eventmanager.search(self._eventid.PLAYER_PRESS_E) and not self._flag_check_press_E:
            self._flag_check_press_E = True
            # игрок просто нажал клавишу E
            if self._char == -1:
                # self._eventmanager.del_event(self._eventid.PLAYER_PRESS_E)
                # self._flag_check_press_E = True
                # self._dialog.set_flag_check_press_E(True)
                # print(f'Нормальный выход из диалога')
                if self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
                    self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)
                from src.Game.UI.Button import Button
                self._dialog.set_dialog_complete(True)
                return Button.ButtonId.PLAY_CONTINUE_MENU
                # exit()

            if not self._flag_dialogue_over:
                # print(f'игрок нажал на пропуск диалога')
                self._the_whole_text = self._dialog.current_text
                self._line_indentation = 0
                # тут должна быть логика, прогрузки всех строк сразу
                for line in self._the_whole_text.split('\n'):
                    parts = line.split('#')
                    line = parts[0]
                    line = self._dialog.current_font.render(line, False, (0, 0, 0, 255))
                    self._text_surface.blit(line, (0, self._line_indentation))
                    self._line_indentation += 30
                # e
                self._char = self._dialog.next_dialog()
                self._flag_dialogue_over = True
                self._flag_waiting_input = True
                if self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
                    self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)
            else:
                # print(f'игрок хочет перейти к следующему диалогу!')

                self._continue_surface_flag = False

                # self._text_surface.fill((83, 5, 250, 100)) # очистить полотно текста
                self._text_surface.fill((0, 0, 0, 0))  # очистить полотно текста
                self._line_indentation = 0 # перевести картеку обратно на 1 строчку
                self._current_line = '' # очистить строку
                self._the_whole_text = '' # очистить весь текст
                self._flag_dialogue_over = False
                self._flag_waiting_input = False

                # print(f'_icon_surface: {id(self._icon_surface)}')
                icon = pygame.transform.scale(self._dialog.current_icon, (41 * 6, 37 * 6))
                #icon = self._dialog.current_icon
                self._icon_surface = icon
                # print(f'_icon_surface: {id(self._icon_surface)}')
                # exit()
                pass
        elif not self._eventmanager.search(self._eventid.PLAYER_PRESS_E):
        # игрок не нажимает клавишу E
            pass
            self._flag_check_press_E = False
                # exit()

        if not self._flag_waiting_input:
            self._char = self._dialog.next()
            if self._char == -1:
                # print(f'Диалоги закончились!')
                self._flag_dialogue_over = True
                self._flag_waiting_input = True
                if self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
                    self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)
                #exit()
        else:
            self._dialog_panel.blit(self._continue_surface, (self._continue_surface.get_rect()[0]+200,
                                                             self._continue_surface.get_rect()[1]+50))


        if self._char is None:
            self._flag_dialogue_over = True
            self._flag_waiting_input = True
            if self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
                self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)

        if not self._flag_dialogue_over:

            if self._char is '#':
                self._char = ''
                self._delay_part = ''
                while self._char is not '\n':
                    self._char = self._dialog.next()
                    self._delay_part += self._char
                self._delay_part = int(self._delay_part)

            if self._char is '\n':
                self._the_whole_text += self._current_line +'\n'
                self._current_line = ''
                self._line_indentation += 30
                # сместить rect строки на несколько пикселей вниз
                self._soundmanager.remove(self._sound.SoundId.SOUND_DIALOG)
                pygame.time.delay(self._delay_part)
                self._delay_part = 0

            else:
                self._current_line += self._char
                line = self._dialog.current_font.render(self._current_line, False, (0, 0, 0, 255))
                self._text_surface.blit(line, (0, self._line_indentation))
                if not self._soundmanager.search(self._sound.SoundId.SOUND_DIALOG):
                    self._soundmanager.add_sound(self._sound.SoundStorage().get_sound(self._sound.SoundId.SOUND_DIALOG))

                # создать строку surface с + 1 символом
                # спроецировать строку surface на общий текст
            # print(f'line: {self._current_line}')
            pass
        else:
            # print(f'диалог завершен!')
            # print(f'ожидание пользовательского ввода...')
            # self._dialog_panel.blit(self._continue_surface, self._continue_surface_rect)
            self._continue_surface_flag = True

from . import Information
class InformationPanel:
    def __init__(self, screen: pygame.Surface, information: Information.Information):

        from src.Game.Managers import EventManager
        from src.Game.Event import Event
        self._eventmanager = EventManager.EventManager()
        self._eventid = Event.EventId
        from src.Game.Managers import SoundManager
        self._soundmanager = SoundManager.SoundManager()

        if self._eventmanager.search(self._eventid.PLAYER_PRESS_E):
            self._eventmanager.del_event(self._eventmanager.del_event(Event.Event(self._eventid.PLAYER_PRESS_E)))

        self._screen = screen
        self._information = information
        self._information_panel = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/UIDialog/') + 'justpanel.png').convert_alpha()

        self._information_panel = pygame.transform.scale(self._information_panel, (151 * 6, 45 * 6))
        self._rect_information_panel = self._information_panel.get_rect()
        self._rect_information_panel.bottom = self._screen.get_rect().bottom - 25
        self._rect_information_panel.centerx = self._screen.get_rect().centerx
        # print(f'_rect_dialog_panel:{self._rect_information_panel}')

        # surface текста на панели диалога - общего
        self._rect_text_surface = pygame.Rect(self._rect_information_panel)
        self._rect_text_surface.topleft = (
        self._rect_text_surface.topleft[0] + 6 * 6, self._rect_text_surface.topleft[1] + 5 * 6) # + 50 * 6
        # print(f'_rect_text_surface:{self._rect_text_surface}')
        # exit()
        self._rect_text_surface.size = (139 * 6, 35 * 6)
        self._text_surface = pygame.Surface(self._rect_text_surface.size, flags=pygame.SRCALPHA)
        # self._text_surface.fill((83, 5, 250, 100))
        self._text_surface.fill((0, 0, 0, 0))

        self._screen_night = pygame.Surface(size=self._screen.get_size(), flags=pygame.SRCALPHA)
        self._screen_night.fill((0, 0, 0, 200))

        self._line_indentation = 0  # отступ строки
        self._flag_check_press_E = False

        # print()
        for line in self._information.text.split('\n'):
            text = self._information.current_font.render(line, False, (0, 0, 0))
            text_rect = pygame.Rect((0, 0), text.get_size())
            text_rect.centerx = self._screen.get_rect().centerx/2 + 120
            # print(f'text_rect:{text_rect} text_rect.centerx:{text_rect.centerx}')
            # print(f'_rect_information_panel:{self._rect_information_panel} _rect_information_panel.centerx:{self._rect_information_panel.centerx}')
            # print(f'_rect_text_surface:{self._rect_text_surface} _rect_text_surface.centerx:{self._rect_text_surface.centerx}')
            # text_rect.x += text.get_size()[0]
            text_rect.top = self._line_indentation
            self._text_surface.blit(text, text_rect)
            self._line_indentation += 30
            # print()
            pass
        #exit()
        # testing ---------------
        # self._yes_button = pygame.Surface((150, 50))
        # self._yes_button.fill((83, 5, 250))
        # self._yes_button_rect = pygame.Rect(self._yes_button.get_rect())
        # self._yes_button_rect.center = self._rect_information_panel.center
        # self._yes_button_rect.x += 150
        # self._yes_button_rect.bottom = self._rect_information_panel.bottom
        # self._yes_button_rect.y -= 50

        # buttons ---------

        self._buttons = []

        # yes button
        _yes_surface_nothing = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Square Buttons/Square Buttons/V Square Button.png')).convert_alpha()
        _yes_surface_nothing = pygame.transform.scale(_yes_surface_nothing, (15 * 3, 15 * 3))
        # _yes_rect = _yes_surface_nothing.get_rect()

        _yes_surface_selected = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Square Buttons/Colored Square Buttons/V col_Square Button.png')).convert_alpha()
        _yes_surface_selected = pygame.transform.scale(_yes_surface_selected, (15 * 3, 15 * 3))

        # no button
        _no_surface_nothing = pygame.image.load(
            os.path.join('src', 'Assets/Sprites/Menu Buttons/Square Buttons/Square Buttons/X Square Button.png')).convert_alpha()
        _no_surface_nothing = pygame.transform.scale(_no_surface_nothing, (15 * 3, 15 * 3))
        # _no_rect = _no_surface_nothing.get_rect()

        _no_surface_selected = pygame.image.load(
            os.path.join('src',
                         'Assets/Sprites/Menu Buttons/Square Buttons/Colored Square Buttons/X col_Square Button.png')).convert_alpha()
        _no_surface_selected = pygame.transform.scale(_no_surface_selected, (15 * 3, 15 * 3))

        from src.Game.UI.Button import Button
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_CONTINUE_MENU, _yes_surface_nothing, _yes_surface_selected))
        self._buttons.append(Button.Button(Button.ButtonId.PLAY_CONTINUE_MENU, _no_surface_nothing, _no_surface_selected))

        self._is_entered = False

        self._buttons[0].rect.center = self._rect_information_panel.center
        self._buttons[1].rect.center = self._rect_information_panel.center

        x = 70
        y = 70

        self._buttons[0].rect.x += x
        self._buttons[1].rect.x -= x

        self._buttons[0].rect.y += y
        self._buttons[1].rect.y += y

        from src.Game.Sound import Sound
        self._soundstorage = Sound.SoundStorage()
        self._soundid = Sound.SoundId

        Sound.Sound(Sound.SoundId.SELECTED_BUTTON,
                    os.path.join('src', 'Assets/Sounds/UI/selected.mp3'),
                    0,
                    None,
                    None,
                    -1)

        Sound.Sound(Sound.SoundId.ENTERED_BUTTON,
                    os.path.join('src', 'Assets/Sounds/UI/enter.mp3'),
                    0,
                    None,
                    None,
                    -1)

        pass

    def draw(self):
        self._screen.blit(self._screen_night, self._screen_night.get_rect())
        self._screen.blit(self._information_panel, self._rect_information_panel)
        self._screen.blit(self._text_surface, self._rect_text_surface)
        # self._screen.blit(self._yes_button, self._yes_button_rect)

        for button in self._buttons:
            if button.condition == Button.ButtonСondition.NOTHING:
                self._screen.blit(button.surface, button.rect)
            elif button.condition == Button.ButtonСondition.SELECRED:
                self._screen.blit(button.surface_selected, button.rect)

        pass

    def handle_events(self):

        # if self._eventmanager.search(self._eventid.PLAYER_PRESS_E) and not self._flag_check_press_E:
        #     self._flag_check_press_E = True
        #     self._information.set_flag_check_press_E(True)
        #     from src.Game.UI.Button import Button
        #     return Button.ButtonId.PLAY_CONTINUE_MENU

        # elif not self._eventmanager.search(self._eventid.PLAYER_PRESS_E):
        # # игрок не нажимает клавишу E
        #     self._flag_check_press_E = False

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
                    if button is self._buttons[0]:
                        self._information.set_yes_button(True)
                    elif button is self._buttons[1]:
                        self._information.set_no_button(True)
                    self._information.set_information_complete(True)
                    return button.button_id
            else:
                button.set_condition(Button.ButtonСondition.NOTHING)