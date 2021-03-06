from sprites.basesprite import BaseSprite
import pygame


class Wall(BaseSprite):
    def __init__(self, settings, position):
        super().__init__(settings, position, (0, 0, 0, 0))
        self.surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(
                self.surface,
                settings.color,
                (0, 0, self.width, self.height),
                )
        self.move = Move()
        self.update = Updater()


class Move:
    def execute(self):
        pass


class Updater:
    def execute(self):
        pass
