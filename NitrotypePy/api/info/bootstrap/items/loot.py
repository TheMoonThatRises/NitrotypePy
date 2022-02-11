from typing import List, Union
from .....objects.api.info.bootstrap.item.loot import Loot
from ..bootstrap import bootstrap


def loot(loot_id=0) -> Union[Loot, List[Loot], bool]:
    """Returns information about the loot.

    Endpoint
    --------
        https://www.nitrotype.com/index/624/bootstrap.js

    Parameters
    ----------
    loot_id : int
        The loot to access from the bootstrap.

    Returns
    -------
    dict
        A dict of information about the loot, or False if the loot cannot be found.
    """

    loot_list = bootstrap("loot")

    if loot_id:
        for loot in loot_list:
            if str(loot["lootID"]) == str(loot_id):
                return loot
    else:
        return loot_list

    return False
