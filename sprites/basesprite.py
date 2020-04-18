import pygame
from actions.move import Move

# self.surface = pygame.image.load('path/to/image.bmp')
# rect = self.surface.get_rect()


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, settings, position, parent):
        super().__init__()
        self.siblings = parent.sprites
        self.settings = settings
        self.x = position[0]
        self.y = position[1]
        self.width = position[2]
        self.height = position[3]
        parent_position = parent.position
        self.east_wall = parent_position[2]
        self.south_wall = parent_position[3]
        self.base_speed = settings.speed
        self.update = BaseCharacterUpdater(self)
        self.move = Move(self)

    @property
    def position(self):
        return (
                self.x,
                self.y,
                self.width,
                self.height,
                )

    @property
    def rect(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))

    @property
    def draw_arguments(self):
        return (self.surface, self.position)


class BaseCharacterUpdater:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        self.parent.move.execute()
