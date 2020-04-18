import pygame


class Input():
    def __init__(self, parent, key_bindings):
        self.parent = parent
        self.key_bindings = key_bindings

    def execute(self, event):
        return self._keyboard_input(event)

    def _keyboard_input(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key in self.key_bindings:
                return self.key_bindings[event.key]
