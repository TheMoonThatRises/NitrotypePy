from ...apiv2.api import api
from ....objects.api.apiv2.endpoints.leaderboard import Leaderboard


def leaderboard(time='season') -> Leaderboard:
    endpoint = 'leaderboards'

    if time:
        endpoint += '?time=' + time

    return api(endpoint)
