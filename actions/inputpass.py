from abc import ABC, abstractmethod


class BaseInputPass(ABC):
    def __init__(self, parent):
        self.parent = parent

    @abstractmethod
    def execute(self, event):
        pass

    def _pass_input_to_group(self, group, event):
        for entity in group:
            if hasattr(entity, 'input'):
                entity.input.execute(event)


class ViewInputPass(BaseInputPass):
    def execute(self, event):
        self._pass_input_to_group(self.parent.views, event)


class CanvasInputPass(BaseInputPass):
    def execute(self, event):
        self._pass_input_to_group(self.parent.sprites, event)
