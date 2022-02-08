from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.leaderboard import Leaderboard


def leaderboard(time="season") -> Leaderboard:
    """Returns nitrotype's leaderboards.

    Endpoint: https://www.nitrotype.com/api/v2/leaderboards?time=season

    :param time: The time type; currently only supports season.
    :type time: str
    :returns: A dict of the nitrotype leaderboard.
    :rtype: dict
    """

    endpoint = "leaderboards"

    if time:
        endpoint += "?time=" + str(time)

    return api(endpoint)
