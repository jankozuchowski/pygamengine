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
            self._fix_movement_wall_colision()

    def _fix_movement_wall_colision(self):
        max_x = self.parent.east_wall - self.parent.surface.get_rect().width
        max_y = self.parent.south_wall - self.parent.surface.get_rect().height
        min_x = 0
        min_y = 0
        if self.parent.x > max_x:
            self.parent.x = max_x
        if self.parent.x < min_x:
            self.parent.x = min_x
        if self.parent.y > max_y:
            self.parent.y = max_y
        if self.parent.y < min_y:
            self.parent.y = min_y

    def add_direction(self, direction):
        if direction in ['N', 'S', 'W', 'E', []]:
            self.direction = direction
