from settings.sprites.wall import Settings as WallSettings
from sprites.wall import Wall


class Settings:
    def __init__(self):
        self.cell_side = 30
        self.mapping = {
                '-': [Wall, WallSettings]
                }
