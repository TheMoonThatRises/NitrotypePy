from ...apiv2.api import api

def leaderboard(time = 'season'):
    endpoint = 'leaderboards'

    if time:
        endpoint += '?time=' + time

    return api(endpoint)
