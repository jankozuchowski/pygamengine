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
    def execute(self):
        self._random()
        super().execute()

    def _random(self):
        direction = random.randrange(5)
        if direction == 1:
            self.north()
        if direction == 2:
            self.south()
        if direction == 3:
            self.west()
        if direction == 4:
            self.east()
