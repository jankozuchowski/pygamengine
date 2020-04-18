from actions.collide import Collide


class Move:
    def __init__(self, parent):
        self.parent = parent
        self.direction = []
        self.moving = True
        self.speed = parent.base_speed
        self.parent.collide = Collide(self.parent)

    def execute(self):
        if self.moving:
            if 'N' in self.direction:
                self.parent.y -= self.speed
                if self.parent.collide.execute():
                    self.parent.y += self.speed
            if 'S' in self.direction:
                self.parent.y += self.speed
                if self.parent.collide.execute():
                    self.parent.y -= self.speed
            if 'W' in self.direction:
                self.parent.x -= self.speed
                if self.parent.collide.execute():
                    self.parent.x += self.speed
            if 'E' in self.direction:
                self.parent.x += self.speed
                if self.parent.collide.execute():
                    self.parent.x -= self.speed

    def add_direction(self, direction):
        if direction in ['N', 'S', 'W', 'E', []]:
            self.direction = direction
