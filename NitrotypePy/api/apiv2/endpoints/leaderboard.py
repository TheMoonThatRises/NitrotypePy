from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.leaderboard import LeaderboardTeams
from typing import List, Union


def leaderboard(
    position=-1, time="season"
) -> Union[LeaderboardTeams, List[LeaderboardTeams]]:
    """Returns nitrotype's leaderboards.

    Endpoint
    --------
        https://www.nitrotype.com/api/v2/leaderboards?time=season

    Parameters
    ----------
    position : int
        The team position
    time : str
        The time type; currently only supports season.

    Returns
    -------
    dict
        The top team or a dict of the nitrotype leaderboard.
    """

    endpoint = "leaderboards"

    if time:
        endpoint += "?time=" + str(time)

    leaderboards = api(endpoint)["scores"]

    if 0 <= position <= 100:
        return leaderboards[position]
    else:
        return leaderboards
