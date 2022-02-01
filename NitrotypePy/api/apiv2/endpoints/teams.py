from ...apiv2 import api

def teams(team_name = ''):
    return api.api('teams/' + team_name)
