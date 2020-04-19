import pygame


class Collide:
    def __init__(self, parent):
        self.parent = parent

    def execute(self, direction):
        self._colliding_with_walls()
        return self._colliding_with_siblings(direction)

    def _colliding_with_siblings(self, direction):
        collided = False
        for sibling in self.parent.siblings:
            if sibling == self.parent:
                continue
            collided = pygame.sprite.collide_rect(sibling, self.parent)
            if collided:
                self._fix_position(sibling, direction)
        return collided

    def _colliding_with_walls(self):
        sprite = self.parent
        if sprite.x + sprite.width > sprite.east_wall:
            sprite.x = sprite.east_wall - sprite.width
        if sprite.x < 0:
            sprite.x = 0
        if sprite.y + sprite.height > sprite.south_wall:
            sprite.y = sprite.south_wall - sprite.height
        if sprite.y < 0:
            sprite.y = 0

    def _fix_position(self, sibling, direction):
        position = sibling.position
        my_position = self.parent.position
        if direction == 'W':
            if my_position[0] < position[0] + position[2]:
                self.parent.x = position[0] + position[2]
        if direction == 'E':
            if my_position[0] + my_position[2] > position[0]:
                self.parent.x = position[0] - my_position[2]
        if direction == 'N':
            if my_position[1] < position[1] + position[3]:
                self.parent.y = position[1] + position[3]
        if direction == 'S':
            if my_position[1] + my_position[3] > position[1]:
                self.parent.y = position[1] - my_position[3]
