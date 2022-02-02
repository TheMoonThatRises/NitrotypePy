from ...apiv2.api import api

def teams(team_name = ''):
    return api('teams/' + team_name)
