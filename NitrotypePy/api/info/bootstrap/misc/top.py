from typing import Dict
from ..bootstrap import bootstrap


def top(type="users") -> Dict[str, int]:
    """Returns the top players/teams.

    Endpoint
    --------
        https://www.nitrotype.com/index/624/bootstrap.js

    Parameters
    ----------
    type : str
        Choose either top players or top teams.

    Returns
    -------
    dict
        A dict of all the top players or teams, depending on type.
    """

    return bootstrap("top_players")[type]
