from settings.sprites.kitchen import Settings as KitchenSettings
from sprites.kitchen import Kitchen
from settings.sprites.office import Settings as OfficeSettings
from sprites.office import Office
from settings.sprites.toilet import Settings as ToiletSettings
from sprites.toilet import Toilet
from settings.sprites.wall import Settings as WallSettings
from sprites.wall import Wall


class Settings:
    def __init__(self):
        self.cell_side = 30
        self.mapping = {
                '-': [Wall, WallSettings, True],
                'k': [Kitchen, KitchenSettings, False],
                'o': [Office, OfficeSettings, False],
                't': [Toilet, ToiletSettings, False],
                }
