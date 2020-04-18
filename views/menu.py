from actions.inputpass import ViewInputPass
from views.baseview import BaseView
from views.canvases.menu import CanvasMenu


class Menu(BaseView):
    def __init__(self, settings, position):
        super().__init__(settings, position)
        self.input = ViewInputPass(self)
        self.add_view(
                CanvasMenu(settings, position)
                )
