import pygame

class Font:
    def __init__(self, settings):
        pygame.font.init()
        self.font = pygame.font.SysFont(settings.type, settings.size)

    def get_character(self, char, color, bg_color):
        return self.font.render(char, True, color, bg_color)
