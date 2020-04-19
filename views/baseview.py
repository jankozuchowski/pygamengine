from actions.inputpass import ViewInputPass
from actions.massdraw import ViewMassDraw
from actions.massupdate import ViewMassUpdate
from abc import ABC
import pygame


class BaseView(ABC):
    def __init__(self, settings, position):
        self.settings = settings
        self.x = position[0]
        self.y = position[1]
        self.width = position[2]
        self.height = position[3]
        self.surface = pygame.Surface((self.position[2], self.position[3]))
        self.views = []
        self.change_view = {
                }
        self.draw = ViewMassDraw(self)
        self.update = ViewMassUpdate(self)
        self.input = ViewInputPass(self)

    @property
    def position(self):
        return (
                self.x,
                self.y,
                self.width,
                self.height,
                )

    @property
    def name(self):
        return self.settings.name

    def add_view(self, view):
        self.views.append(view)

    def detect_view_switch(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.change_view:
                return self.change_view[event.key]
        return None

    @property
    def draw_arguments(self):
        return (self.surface, self.position)
