from typing import Tuple

from src.Game.GameObject.Entity import Entity


class Player(Entity.Entity):

    _default_name = "Player"
    _default_rect_position = (0, 0)
    _default_rect_size = (1024, 2048)

    def __init__(self,
                 name: str = _default_name,
                 pos: Tuple[int, int] = _default_rect_position,
                 size: Tuple[int, int] = _default_rect_size,
                 layer: int = 0):
        super().__init__(name, pos, size, layer)
