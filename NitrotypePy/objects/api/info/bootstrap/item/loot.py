from ..basic_object import Options
from typing import TypedDict


class Loot(TypedDict):
    lootID: int
    type: str
    name: str
    options: Options
    lastModified: int
