from typing import Tuple
from src.Game.GameObject import GameObject


class Trigger:
    _default_name: str = "Trigger"

    def __init__(self,
                 name: str = _default_name,
                 pos: Tuple[int, int] = None,
                 size: Tuple[int, int] = None):
        self._gameobject: GameObject = GameObject.GameObject(name=name if name is not None else Trigger._default_name,
                                                             pos=pos,
                                                             size=size)

    def __str__(self) -> str:
        return f'Trigger:[gameobject:[{self._gameobject}]]'

    @property
    def gameobject(self) -> GameObject:
        return self._gameobject
