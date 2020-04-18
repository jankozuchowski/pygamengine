import pygame
from enum import Enum
from sprites.basesprite import BaseSprite
from font import Font


class PlayerActions(Enum):
    N = pygame.K_UP
    S = pygame.K_DOWN
    W = pygame.K_LEFT
    E = pygame.K_RIGHT
#    pygame.K_e = 'A'


class Player(BaseSprite):
    def __init__(self, settings, position, constraints):
        super().__init__(settings, position, constraints)
        self.playerActions = PlayerActions
        character_generator = Font(self.settings.font)
        self.surface = character_generator.get_character(
                char=self.settings.character,
                color=self.settings.color,
                bg_color=self.settings.bg_color,
                )
        self.input = PlayerCharacterInput(self)

    def _switch_movement(self, key):
        for action in self.playerActions:
            if action.value == key:
                self._update_movement(action.name)

    def _update_movement(self, direction):
        if direction in self.move.direction:
            self.move.direction.remove(direction)
            if len(self.move.direction) == 0:
                self.move.moving = False
        else:
            self.move.direction.append(direction)
            self.move.moving = True


class PlayerCharacterInput:
    def __init__(self, parent):
        self.parent = parent

    def execute(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.parent._switch_movement(event.key)
