from abc import ABC, abstractmethod


class BaseMassUpdate(ABC):
    def __init__(self, parent):
        self.parent = parent

    @abstractmethod
    def execute(self):
        pass

    def _update_entities(self, group):
        for entity in group:
            if hasattr(entity, 'update'):
                entity.update.execute()


class ViewMassUpdate(BaseMassUpdate):
    def execute(self):
        self._update_entities(self.parent.views)


class CanvasMassUpdate(BaseMassUpdate):
    def execute(self):
        self._update_entities(self.parent.sprites)
