from settings.views.menu import Font
from settings.colors import Colors


class Settings:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.bg_color = Colors.black.value
        self.speed = 0.5
        self.character = 'Continue'
        self.active_color = Colors.yellow.value
        self.inactive_color = Colors.blue.value
        self.font = Font()
        self.active = True
        self.next_view = 'game'
