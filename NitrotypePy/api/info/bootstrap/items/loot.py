from typing import List, Union
from .....objects.api.info.bootstrap.item.loot import Loot
from ..bootstrap import bootstrap


def loot(loot_id=0) -> Union[Loot, List[Loot], bool]:
    """Returns information about the loot.

    Endpoint: https://www.nitrotype.com/index/624/bootstrap.js

    :param loot_id: The loot to access from the bootstrap.
    :type loot_id: int
    :returns: A dict of information about the loot, or False if the loot cannot be found.
    :rtype: dict
    """

    loot_list = bootstrap("loot")

    if loot_id:
        for loot in loot_list:
            if loot["lootID"] == loot_id:
                return loot
    else:
        return loot_list

    return False
