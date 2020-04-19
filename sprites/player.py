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
    def __init__(self, settings, position, parent):
        super().__init__(settings, position, parent)
        self.playerActions = PlayerActions
        character_generator = Font(self.settings.font)
        self.surface = character_generator.get_character(
                char=self.settings.character,
                color=self.settings.color,
                bg_color=self.settings.bg_color,
                )
        self.input = PlayerCharacterInput(self)
        self.facing_direction = []

    def stop_action(self, key):
        for action in self.playerActions:
            if action.value == key:
                self.move.remove_direction(action.name)

    def start_action(self, key):
        for action in self.playerActions:
            if action.value == key:
                self._change_facing_direction(action.name)
                self.move.add_direction(action.name)

    def _change_facing_direction(self, direction):
        fdir = self.facing_direction
        fdir.append(direction)
        fdir = list(set(fdir))
        if 'W' in fdir and 'E' in fdir:
            fdir.remove('W')
            fdir.remove('E')
        if 'N' in fdir and 'S' in fdir:
            fdir.remove('N')
            fdir.remove('S')


class PlayerCharacterInput:
    def __init__(self, parent):
        self.parent = parent

    def execute(self, event):
        if event.type == pygame.KEYDOWN:
            self.parent.start_action(event.key)
        if event.type == pygame.KEYUP:
            self.parent.stop_action(event.key)
