from actions.inputpass import ViewInputPass
from views.baseview import BaseView
from canvases.menu import CanvasMenu
from settings.canvases.menu import Settings


class Menu(BaseView):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.input = ViewInputPass(self)
        self.add_view(
                CanvasMenu(Settings(), position)
                )
