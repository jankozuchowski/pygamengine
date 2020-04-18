from settings.colors import Colors


class Settings:
    def __init__(self):
        self.speed = 10
        self.character = '@'
        self.color = Colors.white.value
        self.bg_color = Colors.black.value
        self.font = Font()


class Font:
    def __init__(self):
        self.type = 'timesnewroman'
        self.size = 16
