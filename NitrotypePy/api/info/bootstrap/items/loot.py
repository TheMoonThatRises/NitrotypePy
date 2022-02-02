from typing import List, Union
from .....objects.api.info.bootstrap.item.loot import Loot
from ..bootstrap import bootstrap

def loot(loot_id = 0) -> Union[Loot, List[Loot], bool]:
    loot_list = bootstrap('loot')

    if loot_id:
        for loot in loot_list:
            if loot['lootID'] == loot_id:
                return loot
    else:
        return loot_list

    return False
