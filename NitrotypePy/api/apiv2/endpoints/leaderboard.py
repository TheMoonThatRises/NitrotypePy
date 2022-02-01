from ...apiv2 import api

def leaderboard(time = 'season'):
    endpoint = 'leaderboards'

    if time:
        endpoint += '?time=' + time

    return api.api(endpoint)
