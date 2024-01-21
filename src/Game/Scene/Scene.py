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

        from src.Game.Episodes.Episode0 import SharedResources
        self._sharedresources = SharedResources.SharedResources().shared_resources
        self._color_red = [255, 0, 0]
        self._color_red_flag = False

        self._color_green = [0, 255, 0]
        self._color_green_flag = False

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

    def testing_barriers(self):

        num = 15

        if self._color_red_flag:
            self._color_red[1] += num
            self._color_red[2] += num

            if self._color_red[1] > 255:
                self._color_red[1] = 255
                self._color_red[2] = 255
                self._color_red_flag = False
        else:
            self._color_red[1] -= num
            self._color_red[2] -= num

            if self._color_red[1] < 0:
                self._color_red[1] = 0
                self._color_red[2] = 0
                self._color_red_flag = True
        num2 = 85

        if self._color_green_flag:
            self._color_green[0] += num2
            self._color_green[2] += num2

            if self._color_green[0] > 255:
                self._color_green[0] = 255
                self._color_green[2] = 255
                self._color_green_flag = False
        else:
            self._color_green[0] -= num2
            self._color_green[2] -= num2

            if self._color_green[0] < 0:
                self._color_green[0] = 0
                self._color_green[2] = 0
                self._color_green_flag = True

        from src.Game.GameObject.StaticObject import Trigger
        barriers:List[Trigger.Trigger] = self._sharedresources.get('barriers')

        self._surface.fill((10, 10, 10))
        for layer in self._layer_list:
            layer.draw()
            self._surface.blit(layer.surface, layer.surface.get_rect())

        for barrier in barriers:
            pygame.draw.rect(self._surface, self._color_red, barrier.gameobject.rect, 1)

        horizontale_testing_rect = self._sharedresources.get('horizontale_testing_rect')
        if horizontale_testing_rect:
            pygame.draw.rect(self._surface, self._color_red, horizontale_testing_rect, 1)

        refrigerator_area = self._sharedresources.get('refrigerator_area')
        if refrigerator_area:
            pygame.draw.rect(self._surface, self._color_green, refrigerator_area, 1)

        tv_area = self._sharedresources.get('tv_area')
        if tv_area:
            pygame.draw.rect(self._surface, self._color_green, tv_area, 1)

        creep_area = self._sharedresources.get('creep_area')
        if creep_area:
            pygame.draw.rect(self._surface, self._color_green, creep_area, 1)

        bed_area = self._sharedresources.get('bed_area')
        if bed_area:
            pygame.draw.rect(self._surface, self._color_green, bed_area, 1)

        self._camera.update()
        self._uiManager.update()