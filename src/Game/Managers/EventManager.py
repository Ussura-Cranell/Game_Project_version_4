class EventManager:
    _event_manager = None

    def __new__(cls):
        if not cls._event_manager:
            cls._event_manager = super(EventManager, cls).__new__(cls)
        return cls._event_manager

    def __init__(self):
        self._events = []

    def __str__(self) -> str:
        line = str()
        line += f'EventManager values:\n'
        for i in range(len(self._events)):
            line += f'[{i}] event:[{self._events[i]}]\n'
        return line

    def add_event(self, event: 'Event'):
        if event not in self._events:
            self._events.append(event)

    def del_event(self, event: 'Event'):
        for element in self._events:
            if event == element:
                self._events.remove(element)
                break

    def del_by_id_event(self, id_event):
        for element in self._events:
            if id_event == element._id_event:
                self._events.remove(element)
                break

    def pop_event(self, index: int):
        if 0 <= index < len(self._events):
            self._events.pop(index)

    def search(self, id_event):
        for element in self._events:
            if id_event == element._id_event:
                return element
        return None

    def reset(self):
        self._events = []


