from ...access import access
import json


def bootstrap(item=""):
    """Returns the item requested from the bootstrap.

    Endpoint
    --------
        https://www.nitrotype.com/index/624/bootstrap.js

    Parameters
    ----------
    item : str
        The item to access from the bootstrap.

    Returns
    -------
    dict
        A dict of the item, or False if the item cannot be found.
    """

    bootstrap_items = json.loads(access("index/624/bootstrap.js")[40:-15])

    for bootstrap_item in bootstrap_items:
        if bootstrap_item[0].lower() == item.lower():
            return bootstrap_item[1]

    return False
