class LoadMap:
    def __init__(self, settings, parent):
        self.settings = settings
        self.parent = parent

    def load(self, map_layout):
        side = self.settings.cell_side
        for i in range(len(map_layout)):
            row = i
            for j in range(len(map_layout[row])):
                column = j
                mapping_cell = map_layout[row][column]
                map_cell = self.settings.mapping.get(mapping_cell)
                if map_cell:
                    map_object_settings = map_cell[1]()
                    map_object_class_instance = map_cell[0](
                            map_object_settings,
                            (column*side, row*side, side, side),
                            self.parent,
                            )
                    if map_cell[2]:
                        self.parent.sprites.add(map_object_class_instance)
                    else:
                        self.parent.sprites_without_collision.add(
                            map_object_class_instance
                            )

    def transform(self, map_layout):
        pass
