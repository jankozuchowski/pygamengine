from views.baseview import BaseView
import pygame
from canvases.board import Board
from settings.canvases.board import Settings


class Game(BaseView):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.change_view = {
                pygame.K_ESCAPE: 'menu',
                }
        self.add_view(
                Board(Settings(), (
                    0,
                    0,
                    self.surface.get_rect().width / 10 * 8,
                    self.surface.get_rect().height / 10 * 8,
                    ))
                )
