from typing import Tuple, Dict, Type
from src.Game.GameObject import GameObject
from src.Game.Sprite import Sprite
from src.Game.Animation import Animaton


class Entity:
    _default_name = "Entity"
    _default_rect_position = (0, 0)
    _default_rect_size: Tuple[int, int] = (100, 100)

    def __init__(self,
                 name: str = _default_name,
                 pos: Tuple[int, int] = _default_rect_position,
                 size: Tuple[int, int] = _default_rect_size,
                 layer: int = 0,
                 movement_speed: int = 0):
        self._gameobject = GameObject.GameObject(name=name, pos=pos, size=size, layer=layer)
        self._sprite = Sprite.Sprite(rect=self._gameobject.rect, size=size, layer_index=self._gameobject.layer)
        self._sprite.set_gameobject(self._gameobject)

        self._current_animation: Animaton.Animation = None
        self._animations: Dict[Animaton.AnimationId, Type[Animaton.Animation]] = {}

        self._movement_speed = movement_speed

    def __str__(self) -> str:
        return f'Entity:[gameobject:[{self.gameobject}], sprite:[surface: {self._sprite.surface}], current_animation:[{self._current_animation}]]'

    @property
    def gameobject(self) -> GameObject.GameObject:
        return self._gameobject

    @property
    def sprite(self) -> Sprite.Sprite:
        return self._sprite

    def set_sprite(self, sprite: Sprite.Sprite):
        self._sprite = sprite

    def add_animation(self, id_animation: Animaton.AnimationId, animation: Animaton.Animation):
        self._animations[id_animation] = animation

    def set_current_animation(self, id_animation: Animaton.AnimationId):
        self._current_animation = self._animations.get(id_animation)

    @property
    def current_animation(self) -> Animaton.Animation:
        return self._current_animation

    @property
    def movement_speed(self):
        return self._movement_speed

    def set_movement_speed(self, movement_speed: int):
        self._movement_speed = movement_speed

    @property
    def animations(self):
        return self._animations
