from enum import Enum, auto
from typing import Dict, List, Any, Optional
from src.Game.Managers import EventManager


class EventId(Enum):
    PLAYER_MOVE_LEFT = auto()
    PLAYER_MOVE_UP = auto()
    PLAYER_MOVE_RIGHT = auto()
    PLAYER_MOVE_DOWN = auto()

    PlAYER_PRESS_ESC = auto()

    PLAYER_RUN = auto()

    MOUSE_LEFT = auto()
    MOUSE_RIGHT = auto()
    MOUSE_MIDDLE = auto()

    MOUSE_WHEEL_UP = auto()
    MOUSE_WHEEL_DOWN = auto()

    COLLISION_TWO_OBJECT = auto()

    EVENT_1 = auto()
    EVENT_2 = auto()
    EVENT_3 = auto()
    EVENT_4 = auto()
    EVENT_5 = auto()

    WINDOW_CLOSE = auto()


class Event:
    _event_manager = EventManager.EventManager()

    def __init__(self, id_event: EventId, params: Optional[Dict[str, List[Any]]] = None):
        self._id_event: EventId = id_event
        self._params: Dict[str, List[Any]] = params if params is not None else {}
        if Event._event_manager is not None:
            Event._event_manager.add_event(self)

    def __str__(self) -> str:
        return f"Event:[id_event: {self._id_event.name}, Params: {self._params}]"

    def __eq__(self, other):
        if isinstance(other, Event):
            return self._id_event == other._id_event and set(self._params.values()) == set(other._params.values())
