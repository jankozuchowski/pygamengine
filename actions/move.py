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
        self.speed = parent.base_speed
        self.parent.collide = Collide(self.parent)

    def execute(self):
        if self.direction['N']:
            self.north()
        if self.direction['S']:
            self.south()
        if self.direction['W']:
            self.west()
        if self.direction['E']:
            self.east()

    def north(self):
        self.parent.y -= self.speed
        self.parent.collide.execute('N')

    def south(self):
        self.parent.y += self.speed
        self.parent.collide.execute('S')

    def west(self):
        self.parent.x -= self.speed
        self.parent.collide.execute('W')

    def east(self):
        self.parent.x += self.speed
        self.parent.collide.execute('E')

    def remove_direction(self, direction):
        self.direction[direction] = False

    def add_direction(self, direction):
        self.direction[direction] = True
