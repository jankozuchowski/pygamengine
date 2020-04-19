import pygame
from sprites.npc import Npc
from sprites.player import Player
from settings.sprites.npc import Settings as NpcSettings
from settings.sprites.player import Settings as PlayerSettings
from settings.actions.loadmap import Settings as LoadMapSettings
from actions.loadmap import LoadMap
from maps.first_week import first_week
from canvases.basecanvas import BaseCanvas
from actions.massdraw import CanvasMassDraw
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
        self.add_sprite(
            Npc(
                NpcSettings(),
                (500, 420, 30, 30),
                self,
            )
        )
        self.loadMap = LoadMap(LoadMapSettings(), self)
        self.loadMap.load(first_week)
        self.update = BoardUpdater(self)
        self.player_name = 'player'
        self.draw = BoardDrawer(self)

    @property
    def player_sprite(self):
        for sprite in self.sprites:
            if hasattr(sprite, 'name'):
                if sprite.name == self.player_name:
                    return sprite


class BoardUpdater(CanvasMassUpdate):
    def execute(self):
        super().execute()


class BoardDrawer(CanvasMassDraw):
    def execute(self):
        super().execute()
        self._scroll_surface()

    def _scroll_surface(self):
        player_pos = self.parent.player_sprite.position
        parent_pos = self.parent.position
        scrollx = (parent_pos[2] / 2) - player_pos[0]
        scrolly = (parent_pos[3] / 2) - player_pos[1]
        self.parent.surface.scroll(int(scrollx), int(scrolly))
        self._overwrite_scrolling_remainders(scrollx, scrolly)

    def _overwrite_scrolling_remainders(self, scrollx, scrolly):
        surface = self.parent.surface
        parent_pos = self.parent.position
        # bg_color = self.parent.settings.bg_color
        bg_color = (255, 255, 255)
        xrect = (0, 0, 0, 0)
        yrect = (0, 0, 0, 0)
        if scrollx >= 0:
            xrect = pygame.Rect(0, 0, scrollx, parent_pos[3])
        if scrollx < 0:
            xrect = pygame.Rect(
                    parent_pos[2],
                    0,
                    scrollx,
                    parent_pos[3],
                    )
        if scrolly >= 0:
            yrect = pygame.Rect(0, 0, parent_pos[2], scrolly)
        if scrolly < 0:
            yrect = pygame.Rect(
                    0,
                    parent_pos[3],
                    parent_pos[2],
                    scrolly,
                    )
        pygame.draw.rect(surface, bg_color, xrect)
        pygame.draw.rect(surface, bg_color, yrect)
