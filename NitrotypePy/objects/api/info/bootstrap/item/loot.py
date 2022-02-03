from .basic_object import Options


class Loot:
    def __init__(self):
        self.lootID: int
        self.type: str
        self.name: str
        self.options: Options
        self.lastModified: int
