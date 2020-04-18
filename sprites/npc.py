import random
from sprites.basesprite import BaseSprite
from actions.move import Move
from font import Font


class Npc(BaseSprite):
    def __init__(self, settings, position, parent):
        super().__init__(settings, position, parent)
        self.move = NpcMove(self)
        character_generator = Font(self.settings.font)
        self.surface = character_generator.get_character(
                char=self.settings.character,
                color=self.settings.color,
                bg_color=self.settings.bg_color,
                )


class NpcMove(Move):
    def __init__(self, parent):
        super().__init__(parent)
        self.direction = []

    def execute(self):
        self._random()
        super().execute()

    def _random(self):
        direction = random.randrange(5)
        if direction == 0:
            self.direction = []
        if direction == 1:
            self.direction.append('N')
        if direction == 2:
            self.direction.append('S')
        if direction == 3:
            self.direction.append('W')
        if direction == 4:
            self.direction.append('E')
