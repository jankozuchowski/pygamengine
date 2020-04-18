import pygame
from views.game import Game
from views.menu import Menu
from settings.canvases.game import Settings as GameSettings
from settings.canvases.menu import Settings as MenuSettings
from actions.viewbus import viewbus


class Screen:
    def __init__(self, settings):
        self.settings = settings
        if not self.settings.fullscreen:
            self.surface = pygame.display.set_mode(
                    (self.settings.width, self.settings.height)
                    )
        if self.settings.fullscreen:
            self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.height = self.surface.get_rect().height
        self.settings.width = self.surface.get_rect().width
        pygame.display.set_caption("game title")
        self.views = []
        # self.views.append(Game(self.settings.views.game, (0,0,100,100)))
        self.views.append(Game(
            GameSettings(),
            self.position,
            ))
        self.views.append(Menu(
            MenuSettings(),
            self.position,
            ))
        self.active_view_name = 'game'
        self.viewbus = viewbus
        self.viewbus.parent = self

    @property
    def active_view(self):
        for view in self.views:
            if view.name == self.active_view_name:
                return view

    def update(self):
        self.active_view.update.execute()
        self.active_view.draw.execute()
        self.draw()

    def draw(self):
        self.surface.blit(*self.active_view.draw_arguments)
        pygame.display.flip()

    @property
    def position(self):
        return self.surface.get_rect()

    def input(self, event):
        change_view = self.active_view.detect_view_switch(event)
        if change_view:
            self.active_view_name = change_view
            return
        self.active_view.input.execute(event)
