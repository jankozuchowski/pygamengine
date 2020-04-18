from views.baseview import BaseView
import pygame
from views.canvases.board import Board


class Game(BaseView):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.change_view = {
                pygame.K_ESCAPE: 'menu',
                }
        self.add_view(
                Board(settings, (0, 0, 500, 500))
                )
