import random
from typing import List, Tuple
import pygame
from src.Game.Scene.Layer import Layer
from src.Game.Scene.Camera import Camera
from src.Game.UI import UIManager


class Scene:

    def __init__(self, size: Tuple[int, int], current_menu):
        self._surface = pygame.Surface(size)
        self._layer_list: List[Layer.Layer] = []
        self._camera = Camera.Camera(self)
        self._uiManager = UIManager.UIManager(self._camera, current_menu)

    def add_sprite(self, sprite):
        if sprite.layer_index >= len(self._layer_list):
            for i in range(len(self._layer_list), sprite.layer_index + 1):
                self._layer_list.append(Layer.Layer(size=self._surface.get_rect().size, camera=self._camera))
        self._layer_list[sprite.layer_index].add_sprite(sprite)

    def __str__(self) -> str:
        line = str()
        line += f'Scene:[surface:[{self._surface}],layer_list:[\n'
        for i in range(len(self._layer_list)):
            line += f'[{i}] {self._layer_list[i]}'
        line += f']\n'
        return line

    def update(self):
        self._surface.fill((10, 10, 10))
        for layer in self._layer_list:
            layer.draw()
            self._surface.blit(layer.surface, layer.surface.get_rect())
        self._camera.update()
        self._uiManager.update()

    @property
    def uimanager(self):
        return self._uiManager

    # теперь все рисутется с помощбю камеры
    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    def get_layer(self, layer_index: int):
        return self._layer_list[layer_index]

    @property
    def camera(self):
        return self._camera

    def reset(self):
        self._layer_list: List[Layer.Layer] = []

    def testing_barriers(self, barriers, verticale_testing_rect = None, horizontale_testing_rect = None):
        from src.Game.GameObject.StaticObject import Trigger
        barriers: List[Trigger.Trigger]

        verticale_testing_rect: pygame.Rect = verticale_testing_rect
        horizontale_testing_rect: pygame.Rect = horizontale_testing_rect

        self._surface.fill((10, 10, 10))
        for layer in self._layer_list:
            layer.draw()
            self._surface.blit(layer.surface, layer.surface.get_rect())

        for barrier in barriers:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.rect(self._surface, color, barrier.gameobject.rect, 1)

        if verticale_testing_rect is not None:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.rect(self._surface, color, verticale_testing_rect, 1)

        if horizontale_testing_rect is not None:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.rect(self._surface, color, horizontale_testing_rect, 1)

        self._camera.update()
        self._uiManager.update()