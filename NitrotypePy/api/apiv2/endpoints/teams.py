from ...apiv2.api import api


def teams(team_name=""):
    """Returns most of the nitrotype's teams information.

    Endpoint: https://www.nitrotype.com/api/v2/teams/{team_name}

    :param team_name: The tag of the team.
    :type team_name: str
    :returns: A dict of the team's information.
    :rtype: dict
    """

    return api("teams/" + team_name)
