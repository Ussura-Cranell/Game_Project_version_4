class AnimationManager:
    _animation_manager = None

    def __new__(cls):
        if not cls._animation_manager:
            cls._animation_manager = super(AnimationManager, cls).__new__(cls)
        return cls._animation_manager

    def __init__(self):
        self._animation_entitys = []

    def __str__(self) -> str:
        line = str()
        line += f'AnimationManager values:\n'
        for i in range(len(self._animation_entitys)):
            line += f'[{i}] :[{self._animation_entitys[i]}]\n'
        return line

    def add_animation_entity(self, animation_entity: 'Entity'):
        if animation_entity not in self._animation_entitys:
            self._animation_entitys.append(animation_entity)

    def update(self):
        for animation_entity in self._animation_entitys:
            if not animation_entity.current_animation.stop_animation:
                animation_entity.current_animation.next()
            animation_entity.sprite.set_surface(animation_entity.current_animation.frame)
            animation_entity.sprite.set_needs_updated(True)
    def reset(self):
        self._animation_entitys = []