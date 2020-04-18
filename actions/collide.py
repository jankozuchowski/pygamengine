import pygame


class Collide:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        result = False
        for sibling in self.parent.siblings:
            if sibling == self.parent:
                continue
            result = result or pygame.sprite.collide_rect(sibling, self.parent)
        return result
