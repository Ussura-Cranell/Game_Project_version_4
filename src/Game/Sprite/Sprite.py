from typing import Tuple, Optional
from src.Game.GameObject import GameObject
import pygame


class Sprite:
    _scene: 'Scene.Scene' = None

    _default_rect_size: Tuple[int, int] = (100, 100)
    _default_layer_index: int = 0

    def __init__(self, rect: pygame.Rect, size: Tuple[int, int] = _default_rect_size, layer_index: int = _default_layer_index,
                 gameobject: Optional[GameObject.GameObject] = None):

        if Sprite._scene is None:
            raise RuntimeError("Нельзя создать sprite без указания сцены")

        self._rect = rect
        self._surface = pygame.Surface(size)
        self._needs_updated = True
        self._layer_index = layer_index

        self._gameobject = gameobject

        # добавление спрайта на сцену
        Sprite._scene.add_sprite(self)

    def __str__(self):
        return f'Sprite:[layer_index:[{self._layer_index}],rect:[{self._rect}],surface:[{self._surface}]]'

    @classmethod
    def set_scene(cls, scene: 'Scene.Scene'):
        cls._scene = scene

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def set_surface(self, surface: pygame.Surface):
        self._surface = surface

    def set_needs_updated(self, update: bool):
        self._needs_updated = update

    @property
    def needs_updated(self) -> bool:
        return self._needs_updated

    @property
    def layer_index(self) -> int:
        return self._layer_index

    def set_gameobject(self, gameobject: GameObject.GameObject):
        self._gameobject = gameobject

    @property
    def gameobject(self):
        return self._gameobject
