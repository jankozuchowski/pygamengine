class VectorMove:
    def __init__(self, parent):
        self.vectors = []
        self.parent = parent

    def add_vector(self, direction, speed, duration):
        self.vectors.append({
            'direction': direction,
            'speed': speed,
            'duration': duration})

    def _remove_empty_vectors(self):
        for i in len(self.vectors):
            if self.vectors[i]['duration'] == 0:
                self.vectors.remove(i)

    def execute(self):
        return self.vector_move()

    def vector_move(self):
        for i in range(len(self.vectors)):
            vector = self.vectors[i]
            vector['duration'] -= 1
            self._move_north(vector['direction'], vector['speed'])
            self._move_south(vector['direction'], vector['speed'])
            self._move_east(vector['direction'], vector['speed'])
            self._move_west(vector['direction'], vector['speed'])
        self.remove_empty_vectors()

    def _move_north(self, direction, speed):
        if 'N' in direction:
            self.parent.y -= speed

    def _move_south(self, y, direction, speed):
        if 'S' in direction:
            self.parent.y += speed

    def _move_east(self, x, direction, speed):
        if 'E' in direction:
            self.parent.x += speed

    def _move_west(self, x, direction, speed):
        if 'W' in direction:
            self.parent.x -= speed
