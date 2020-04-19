from actions.collide import Collide


class Move:
    def __init__(self, parent):
        self.parent = parent
        self.direction = {
                'N': False,
                'S': False,
                'W': False,
                'E': False,
                }
        self.moving = True
        self.speed = parent.base_speed
        self.parent.collide = Collide(self.parent)

    def execute(self):
        if self.moving:
            if self.direction['N']:
                self.parent.y -= self.speed
                self.parent.collide.execute('N')
            if self.direction['S']:
                self.parent.y += self.speed
                self.parent.collide.execute('S')
            if self.direction['W']:
                self.parent.x -= self.speed
                self.parent.collide.execute('W')
            if self.direction['E']:
                self.parent.x += self.speed
                self.parent.collide.execute('E')

    def add_direction(self, direction):
        self.direction[direction] = True

    def remove_direction(self, direction):
        self.direction[direction] = False
