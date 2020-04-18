from abc import ABC, abstractmethod


class BaseMassDraw(ABC):
    def __init__(self, parent):
        self.parent = parent

    @abstractmethod
    def execute(self):
        pass

    def _draw_entities(self, entity_group):
        self.parent.surface.fill(self.parent.settings.bg_color)
        for entity in entity_group:
            if hasattr(entity, 'draw'):
                entity.draw.execute()
            self.parent.surface.blit(*entity.draw_arguments)


class ViewMassDraw(BaseMassDraw):
    def execute(self):
        self._draw_entities(self.parent.views)


class CanvasMassDraw(BaseMassDraw):
    def execute(self):
        self._draw_entities(self.parent.sprites)
