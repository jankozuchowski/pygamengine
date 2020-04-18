from settings.colors import Colors

class Settings:
    def __init__(self):
        self.name = 'game'
        self.width = 1000
        self.height = 1000
        self.bg_color = Colors.black.value
        self.speed = 0.5
