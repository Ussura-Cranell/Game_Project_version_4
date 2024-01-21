from typing import Dict, Set


class GameObjectManager:
    _game_object_manager = None
    _initialized = False

    def __new__(cls):
        if not cls._game_object_manager:
            cls._game_object_manager = super(GameObjectManager, cls).__new__(cls)
        return cls._game_object_manager

    def __init__(self):

        if GameObjectManager._initialized: return None

        # print('init GameObjectManager')
        self._objects_by_layer = {}

        GameObjectManager._initialized = True

    def __str__(self) -> str:
        line = str()

        line += f'GameObjectManager values:\n'
        for value in self._objects_by_layer.values():
            for value_in_set in value:
                line += f'{value_in_set}\n'
        return line

    def add_object(self, game_object: 'GameObject.GameObject'):
        layer = game_object.layer
        if layer not in self._objects_by_layer:
            self._objects_by_layer[layer] = set()
        self._objects_by_layer[layer].add(game_object)

    def get_objects_by_layer(self, layer: int) -> Set['GameObject.GameObject']:
        return self._objects_by_layer.get(layer, set())

    def get_dict(self) -> Dict:
        return self._objects_by_layer

    def reset(self):
        self._objects_by_layer = {}