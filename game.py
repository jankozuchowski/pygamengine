import sys
import pygame
from screen import Screen
from settings.screen import Settings
from actions.quitbus import quitbus


class Game:

    def __init__(self):
        self.screen = Screen(Settings())
        self.run = True
        self.quitbus = quitbus
        self.quitbus.parent = self

    def _decide_to_die(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    def _read_input(self):
        for event in pygame.event.get():
            self._decide_to_die(event)
            self.screen.input(event)

    def run_game(self):
        while self.run:
            self._read_input()
            self.screen.update()


if __name__ == '__main__':
    game = Game()
    game.run_game()
