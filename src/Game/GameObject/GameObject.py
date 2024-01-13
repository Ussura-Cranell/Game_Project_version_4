from typing import Tuple, Optional
import pygame
from src.Game.Managers import ObjManager


class GameObject:
    _default_name: str = "Game_Object"
    _default_rect_position: Tuple[int, int] = (0, 0)
    _default_rect_size: Tuple[int, int] = (100, 100)

    _counting_instances: int = 0
    _game_object_manager = ObjManager.GameObjectManager()

    def __init__(self,
                 name: str = _default_name,
                 pos: Optional[Tuple[int, int]] = None,
                 size: Optional[Tuple[int, int]] = None,
                 layer: int = 0):
        self._name: str = name if name is not None else GameObject._default_name
        self._rect: pygame.Rect = pygame.Rect(
            pos if pos is not None else GameObject._default_rect_position,
            size if size is not None else GameObject._default_rect_size
        )
        self._layer: int = layer
        self._id: int = GameObject._counting_instances
        GameObject._counting_instances += 1

        if GameObject._game_object_manager is not None:
            GameObject._game_object_manager.add_object(self)

    def __str__(self) -> str:
        return f'GameObject:[id: {self._id}, layer: {self._layer}, name: "{self._name}", rect:[lt_pos: {self._rect.topleft}, c_pos: {self._rect.center}, size: {self._rect.size}]]'

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @property
    def layer(self) -> int:
        return self._layer

    def set_name(self, name: str) -> None:
        self._name = name

    def set_rect(self, rect: pygame.Rect) -> None:
        self._rect = rect

    @classmethod
    def set_game_object_manager(cls, game_object_manager: ObjManager.GameObjectManager) -> None:
        cls._game_object_manager = game_object_manager
