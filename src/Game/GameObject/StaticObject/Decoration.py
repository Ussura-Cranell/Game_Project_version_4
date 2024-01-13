from typing import Tuple
from src.Game.GameObject import GameObject
from src.Game.Sprite import Sprite


class Decoration:

    _default_name = "Decoration"
    _default_rect_position = (0, 0)
    _default_rect_size: Tuple[int, int] = (100, 100)

    def __init__(self,
                 name: str = _default_name,
                 pos: Tuple[int, int] = _default_rect_position,
                 size: Tuple[int, int] = _default_rect_size,
                 layer: int = 0):

        self._gameobject = GameObject.GameObject(name=name, pos=pos, size=size, layer=layer)
        self._sprite = Sprite.Sprite(rect=self._gameobject.rect, size=size,layer_index=self._gameobject.layer)
        self._sprite.set_gameobject(self._gameobject)

    def __str__(self) -> str:
        return f'Decoration:[gameobject:[{self.gameobject}], sprite:[surface: {self._sprite.surface}]]'

    @property
    def gameobject(self) -> GameObject.GameObject:
        return self._gameobject

    @property
    def sprite(self) -> Sprite.Sprite:
        return self._sprite

    def set_sprite(self, sprite: Sprite.Sprite):
        self._sprite = sprite
