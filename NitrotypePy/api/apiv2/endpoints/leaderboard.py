from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.leaderboard import Leaderboard


def leaderboard(time="season") -> Leaderboard:
    """Returns nitrotype's leaderboards.

    Endpoint
    --------
        https://www.nitrotype.com/api/v2/leaderboards?time=season

    Parameters
    ----------
    time : str
        The time type; currently only supports season.

    Returns
    -------
    dict
        A dict of the nitrotype leaderboard.
    """

    endpoint = "leaderboards"

    if time:
        endpoint += "?time=" + str(time)

    return api(endpoint)
