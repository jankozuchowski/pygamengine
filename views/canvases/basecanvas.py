from abc import ABC
import pygame
from actions.massdraw import CanvasMassDraw
from actions.massupdate import CanvasMassUpdate
from actions.inputpass import CanvasInputPass


class BaseCanvas(ABC):
    def __init__(self, settings, position):
        self.settings = settings
        self.x = position[0]
        self.y = position[1]
        self.height = position[2]
        self.width = position[3]
        self.surface = pygame.Surface((self.position[2], self.position[3]))
        self.sprites = pygame.sprite.Group()
        self.draw = CanvasMassDraw(self)
        self.update = CanvasMassUpdate(self)
        self.input = CanvasInputPass(self)

    def add_sprite(self, sprite):
        self.sprites.add(sprite)

    @property
    def position(self):
        return (
                self.x,
                self.y,
                self.width,
                self.height,
                )

    @property
    def draw_arguments(self):
        return (self.surface, self.position)
