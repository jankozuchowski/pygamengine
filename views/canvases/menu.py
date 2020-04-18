import pygame
from font import Font
from sprites.basesprite import BaseSprite
from settings.sprites.cont import Settings as ContSettings
from settings.sprites.quit import Settings as QuitSettings
# from settings.objects.settings import Settings as SettingsSettings
from actions.quitbus import quitbus
from actions.viewbus import viewbus
from views.canvases.basecanvas import BaseCanvas


class CanvasMenu(BaseCanvas):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.input = MenuInput(self)
        self.add_sprite(
            MenuString(
                ContSettings(),
                (
                    self.surface.get_rect().width / 2,
                    200,
#                   (self.surface.get_rect().height - 200) / 2,
                    0,
                    0,
                ),
            )
        )
#        self.add_view(
#            MenuString(
#                SettingsSettings(),
#                (
#                    self.surface.get_rect().width / 2,
#                    (self.surface.get_rect().height - 200) / 3 * 2,
#                    0,
#                    0,
#                ),
#            )
#        )
        self.add_sprite(
            QuitMenuString(
                QuitSettings(),
                (
                    self.surface.get_rect().width / 2,
                    400,
#                   (self.surface.get_rect().height - 200),
                    0,
                    0,
                ),
            )
        )
        self.active = 0
        self.change_view = None

    def _update_entities_activity(self, change):
        sprite_table = list(self.sprites)
        sprite_table[self.active].active = False
        self.active += change
        if self.active < 0:
            self.active = len(self.sprites) - 1
        if self.active > len(self.sprites) - 1:
            self.active = 0
        sprite_table[self.active].active = True

    def detect_view_switch(self, event):
        if self.change_view:
            next_view = self.change_view
            self.change_view = None
            return next_view


class MenuInput:
    def __init__(self, parent):
        self.parent = parent

    def execute(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = -1
                self.parent._update_entities_activity(change)
            elif event.key == pygame.K_DOWN:
                change = 1
                self.parent._update_entities_activity(change)
            elif event.key == pygame.K_RETURN:
                self.parent.change_view = list(self.parent.sprites)[self.parent.active].execute()
        self.parent.update.execute()


class MenuString(BaseSprite):
    def __init__(self, settings, position):
        dummy_parent_position = (0, 0, 0, 0)
        super().__init__(settings, position, dummy_parent_position)
        self.font = Font(settings.font)
        self.active = settings.active
        if hasattr(settings, 'next_view'):
            self.next_view = settings.next_view
        self.update = MenuUpdater(self)
        self.update.execute()
        self.draw = MenuDrawer(self)

    def execute(self):
        if hasattr(self, 'next_view'):
            viewbus.execute(self.next_view)
        self._rotate_option()
        self.update.execute()

    def _rotate_option(self):
        pass


class QuitMenuString(MenuString):
    def execute(self):
        quitbus.execute()


class MenuUpdater:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        self._update_active()

    def _update_active(self):
        if self.parent.active:
            string_color = self.parent.settings.active_color
        else:
            string_color = self.parent.settings.inactive_color
        self.parent.surface = self.parent.font.get_character(
                char=self.parent.settings.character,
                color=string_color,
                bg_color=self.parent.settings.bg_color,
                )


class MenuDrawer:
    def __init__(self, parent):
        self.parent = parent

    def execute(self):
        self.parent.surface.blit(*self.parent.draw_arguments)
