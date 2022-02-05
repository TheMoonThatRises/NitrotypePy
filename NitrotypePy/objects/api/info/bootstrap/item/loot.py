from ..basic_object import Options
from typing import TypedDict


Loot = TypedDict(
    "Loot",
    {"lootID": int, "type": str, "name": str, "options": Options, "lastModified": int},
)
