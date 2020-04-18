import pygame


class Collide:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        return self._colliding_with_siblings() or self._colliding_with_walls()

    def _colliding_with_siblings(self):
        result = False
        for sibling in self.parent.siblings:
            if sibling == self.parent:
                continue
            result = result or pygame.sprite.collide_rect(sibling, self.parent)
        return result

    def _colliding_with_walls(self):
        max_x = self.parent.east_wall - self.parent.surface.get_rect().width
        max_y = self.parent.south_wall - self.parent.surface.get_rect().height
        min_x = 0
        min_y = 0
        if self.parent.x > max_x:
            return True
        if self.parent.x < min_x:
            return True
        if self.parent.y > max_y:
            return True
        if self.parent.y < min_y:
            return True
        return False
