

class Sceneinitialization:

    def __init__(self):
        from src.Game.GameObject.StaticObject import Decoration
        from src.Game.Scene import Scene
        from src.Game.Sprite import Sprite
        import pygame.image

        self._scene = Scene.Scene(size=(800*2.5, 600*2.5))

        Sprite.Sprite.set_scene(self._scene)

        play_button_frame = [pygame.image.load(
            r'..\Assets\Sprites\Menu Buttons\Large Buttons\Colored Large Buttons\Play col_Button.png').convert_alpha(),
                             pygame.image.load(
                                 r'..\Assets\Sprites\Menu Buttons\Large Buttons\Large Buttons\Play Button.png').convert_alpha()]

        play_button = Decoration.Decoration(size=(600, 200))
        play_button.sprite.set_surface(play_button_frame[1])
        play_button.gameobject.rect.center = self._scene.surface.get_rect().center

        self._global_values = {}
        self._global_values['play_button'] = play_button
        self._global_values['play_button_frame'] = play_button_frame

    @property
    def scene(self):
        return self._scene

    @property

    def global_values(self):
        return self._global_values

