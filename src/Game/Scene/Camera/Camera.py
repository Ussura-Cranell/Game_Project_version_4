from typing import Tuple
import pygame


class Camera:
    def __init__(self, scene):
        from src.Game import GameInfo
        gameinfo = GameInfo.GameInfo()

        self._scene_surface = scene.surface
        self._surface = pygame.Surface(gameinfo.screen_size)
        self._rect = pygame.Rect(self._surface.get_rect())
        self._camera_zoom = 0
        self.calculate_zoom_limits()
        self._camera_position: Tuple[int, int] = scene.surface.get_rect().center
        self._subsurface_rect = None
        self._screen_center = self._surface.get_rect().center

    @property
    def surface(self):
        return self._surface

    @property
    def rect(self):
        return self._rect

    def set_zoom(self, zoom: float):
        self._camera_zoom = zoom

    @property
    def zoom(self):
        return self._camera_zoom

    def update(self):
        camera_surface = self._surface
        camera_surface.fill((10, 10, 10))

        scene_surface = self._scene_surface
        camera_rect, scene_rect = camera_surface.get_rect(), scene_surface.get_rect()

        zoom, camera_size = self._camera_zoom, camera_rect.size

        zoom = max(self._min_zoom, min(self._max_zoom, zoom))

        subsurface_rect = pygame.Rect(0, 0, *camera_size).inflate(camera_size[0] * zoom, camera_size[1] * zoom)
        camera_pos = self._camera_position
        subsurface_rect.center = (camera_pos[0], camera_pos[1])

        subsurface_rect.left = max(0, min(subsurface_rect.left, scene_rect.w - subsurface_rect.width))
        subsurface_rect.top = max(0, min(subsurface_rect.top, scene_rect.h - subsurface_rect.height))

        self._camera_position = subsurface_rect.center

        self._subsurface_rect = subsurface_rect

        subsurface = pygame.transform.scale(scene_surface.subsurface(subsurface_rect), camera_size)
        subsurface_rect = subsurface.get_rect(center=camera_rect.center)

        self._surface.blit(subsurface, subsurface_rect)



    def calculate_zoom_limits(self):
        scene_size, camera_size = self._scene_surface.get_size(), self._surface.get_size()

        max_zoom_x = scene_size[0] / camera_size[0]
        max_zoom_y = scene_size[1] / camera_size[1]
        max_zoom = min(max_zoom_x, max_zoom_y)

        min_zoom = -0.9

        self._min_zoom = min_zoom
        self._max_zoom = max_zoom - 1

    def screen_to_scene_coordinates(self, screen_coords: Tuple[int, int]) -> Tuple[int, int]:
        """
        Convert screen coordinates to scene coordinates.
        """
        camera_rect = self._surface.get_rect()
        scene_rect = self._scene_surface.get_rect()

        zoom = max(self._min_zoom, min(self._max_zoom, self._camera_zoom))

        camera_pos = self._camera_position

        screen_x, screen_y = screen_coords
        camera_x = (screen_x - camera_rect.left - camera_rect.width / 2) / zoom + camera_pos[0]
        camera_y = (screen_y - camera_rect.top - camera_rect.height / 2) / zoom + camera_pos[1]

        camera_x = max(0, min(camera_x, scene_rect.width))
        camera_y = max(0, min(camera_y, scene_rect.height))

        return int(camera_x), int(camera_y)

    @property
    def position(self) -> Tuple[int, int]:
        return self._camera_position

    def set_position(self, position: Tuple[int, int]):
        self._camera_position = position

    @property
    def min_zoom(self):
        return self._min_zoom

    @property
    def max_zoom(self):
        return self._max_zoom

    @property
    def subsurface_rect(self):
        return self._subsurface_rect

    @property
    def screen_center(self):
        return self._screen_center
