from sprites.npc import Npc
from sprites.player import Player
from settings.sprites.npc import Settings as NpcSettings
from settings.sprites.player import Settings as PlayerSettings
from settings.actions.loadmap import Settings as LoadMapSettings
from actions.loadmap import LoadMap
from maps.first_week import first_week
from canvases.basecanvas import BaseCanvas
from actions.massupdate import CanvasMassUpdate


class Board(BaseCanvas):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.add_sprite(
            Player(
                PlayerSettings(),
                (
                    self.surface.get_rect().width / 2,
                    self.surface.get_rect().height / 2,
                    30,
                    30,
                ),
                self,
            )
        )
#        self.add_sprite(
#            Npc(
#                NpcSettings(),
#                (500, 420, 30, 30),
#                self,
#            )
#        )
        self.loadMap = LoadMap(LoadMapSettings(), self)
        self.loadMap.load(first_week)
        self.update = BoardUpdater(self)


class BoardUpdater(CanvasMassUpdate):
    def execute(self):
        super().execute()
