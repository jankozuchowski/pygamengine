from settings.colors import Colors


class Settings:
    def __init__(self):
        self.name = 'menu'
        self.width = 1000
        self.height = 1000
        self.bg_color = Colors.black.value
        self.font = Font()


class Font:
    def __init__(self):
        self.type = 'timesnewroman'
        self.size = 30
