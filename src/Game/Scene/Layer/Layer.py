import random
from typing import Tuple, List, Optional
from src.Game.Sprite import Sprite
from src.Game.Scene.Camera import Camera

import pygame


class Layer:
    def __init__(self, size: Tuple[int, int], drawing_by_coordinates: bool = False, camera: Optional[Camera.Camera] = None):
        self._sprite_list: List[Sprite.Sprite] = []
        self._surface = pygame.Surface(size=size, flags=pygame.SRCALPHA)
        self._drawing_by_coordinates = drawing_by_coordinates
        self._camera: Optional[Camera.Camera] = camera

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    def add_sprite(self, sprite: Sprite.Sprite):
        self._sprite_list.append(sprite)

    def draw(self):

        for sprite in self._sprite_list:
            is_in_camera_view = self._camera.subsurface_rect.colliderect(sprite.rect) \
                if self._camera.subsurface_rect is not None else True

            if sprite.needs_updated and is_in_camera_view:
                self._surface.fill((0, 0, 0, 0))  # complete cleaning of the layer
                if self._drawing_by_coordinates:
                    self._sprite_list = sorted(self._sprite_list, key=lambda sprite: sprite.rect.bottom)

                for sprite in self._sprite_list:
                    self._surface.blit(sprite.surface, sprite.rect)
                    sprite.set_needs_updated(False)

    def __str__(self) -> str:
        line = str()
        line += f'Layer:[surface:[{self._surface}],sprite_list:['
        for sprite in self._sprite_list:
            line += f'\n\t{sprite}'
        line += f']\n'
        return line

    def set_drawing_by_coordinates(self, drawing_by_coordinates:bool):
        self._drawing_by_coordinates = drawing_by_coordinates
