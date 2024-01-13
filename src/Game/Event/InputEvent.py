from src.Game.Event import Event
from src.Game.Managers import EventManager
import pygame


class InputEvent:
    _input_event = None

    def __new__(cls):
        if not cls._input_event:
            cls._input_event = super(InputEvent, cls).__new__(cls)
        return cls._input_event

    def __init__(self):
        pass

        self._event_manager = EventManager.EventManager()

    def update(self):

        # события с промежуточным циклом жизни
        self._event_manager.del_event(Event.Event(Event.EventId.MOUSE_WHEEL_UP))
        self._event_manager.del_event(Event.Event(Event.EventId.MOUSE_WHEEL_DOWN))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Event.Event(Event.EventId.PLAYER_MOVE_LEFT)
                elif event.key == pygame.K_w:
                    Event.Event(Event.EventId.PLAYER_MOVE_UP)
                elif event.key == pygame.K_d:
                    Event.Event(Event.EventId.PLAYER_MOVE_RIGHT)
                elif event.key == pygame.K_s:
                    Event.Event(Event.EventId.PLAYER_MOVE_DOWN)
                elif event.key == pygame.K_LSHIFT:
                    Event.Event(Event.EventId.PLAYER_RUN)

                elif event.key == pygame.K_ESCAPE:
                    Event.Event(Event.EventId.PlAYER_PRESS_ESC)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self._event_manager.del_event(Event.Event(Event.EventId.PLAYER_MOVE_LEFT))
                elif event.key == pygame.K_w:
                    self._event_manager.del_event(Event.Event(Event.EventId.PLAYER_MOVE_UP))
                elif event.key == pygame.K_d:
                    self._event_manager.del_event(Event.Event(Event.EventId.PLAYER_MOVE_RIGHT))
                elif event.key == pygame.K_s:
                    self._event_manager.del_event(Event.Event(Event.EventId.PLAYER_MOVE_DOWN))
                elif event.key == pygame.K_LSHIFT:
                    self._event_manager.del_event(Event.Event(Event.EventId.PLAYER_RUN))

                elif event.key == pygame.K_ESCAPE:
                    self._event_manager.del_event(Event.Event(Event.EventId.PlAYER_PRESS_ESC))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    Event.Event(Event.EventId.MOUSE_LEFT)
                elif event.button == pygame.BUTTON_MIDDLE:
                    Event.Event(Event.EventId.MOUSE_MIDDLE)
                elif event.button == pygame.BUTTON_RIGHT:
                    Event.Event(Event.EventId.MOUSE_RIGHT)

            elif event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    Event.Event(Event.EventId.MOUSE_WHEEL_UP)
                elif event.y == -1:
                    Event.Event(Event.EventId.MOUSE_WHEEL_DOWN)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    self._event_manager.del_event(Event.Event(Event.EventId.MOUSE_LEFT))
                elif event.button == pygame.BUTTON_MIDDLE:
                    self._event_manager.del_event(Event.Event(Event.EventId.MOUSE_MIDDLE))
                elif event.button == pygame.BUTTON_RIGHT:
                    self._event_manager.del_event(Event.Event(Event.EventId.MOUSE_RIGHT))

            elif event.type == pygame.QUIT:
                Event.Event(Event.EventId.WINDOW_CLOSE)