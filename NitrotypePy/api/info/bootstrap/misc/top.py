from typing import Dict
from ..bootstrap import bootstrap


def top(type="users") -> Dict[str, int]:
    return bootstrap["top_players"][type]
