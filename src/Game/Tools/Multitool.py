from typing import Tuple, List

import pygame

def x_y_transform_spritesheet_to_animation(spritesheet: pygame.Surface, image_size: Tuple[int, int]):
    size_spritesheet: List[int, int] = list(spritesheet.get_size())
    chunks: List[pygame.Surface] = []
    count = 0

    print(f'image size: {size_spritesheet}')

    for y in range(0, size_spritesheet[1], image_size[1]):
        for x in range(0, size_spritesheet[0], image_size[0]):
            rect = pygame.Rect(x, y, image_size[0], image_size[1])
            print(f'{count} frame selected: ({x // image_size[0]}, {y // image_size[1]})')
            chunk = spritesheet.subsurface(rect)
            count += 1

            chunks.append(chunk)
    return chunks


def y_x_transform_spritesheet_to_animation(spritesheet: pygame.Surface, image_size: Tuple[int, int]):
    size_spritesheet = list(spritesheet.get_size())
    chunks: List[int, int] = []
    rect = pygame.Rect(0, 0, image_size[0], image_size[1])
    count = 0

    for x in range(0, size_spritesheet[0], image_size[0]):
        for y in range(0, size_spritesheet[1], image_size[1]):
            rect.update(x, y, image_size[0], image_size[1])
            print(f'{count} frame selected: ({x / image_size[0]:.0f}, {y / image_size[1]:.0f})')
            chunk = spritesheet.subsurface(rect)
            count += 1
            chunks.append(chunk)
    return chunks

def change_scale_image_index(original_image: pygame.Surface, scale_factor: float):

    new_width = int(original_image.get_width() * scale_factor)
    new_height = int(original_image.get_height() * scale_factor)

    return pygame.transform.scale(original_image, (new_width, new_height))

def change_scale_image_size(original_image: pygame.Surface, size: Tuple[int, int]):

    return pygame.transform.scale(original_image, (size[0], size[1]))
