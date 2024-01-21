from typing import Dict


class SharedResources:
    _shared_resources = None
    _initialized = False
    pass

    def __new__(cls):
        if not cls._shared_resources:
            cls._shared_resources = super(SharedResources, cls).__new__(cls)
        return cls._shared_resources

    def __init__(self):
        if SharedResources._initialized: return None

        # init
        self._shared_resources_data = dict()

        SharedResources._initialized = True

    @property
    def shared_resources(self):
        return self._shared_resources_data

    def __str__(self):
        line = str()
        num = 0
        for key in self._shared_resources_data.keys():
            line += f'[{num}] key:"{key}"\n'
            num += 1
        return line
