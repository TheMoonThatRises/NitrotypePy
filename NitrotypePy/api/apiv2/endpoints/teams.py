from ...apiv2.api import api


def teams(team_name=""):
    """Returns most of the nitrotype's teams information.

    Endpoint
    --------
        https://www.nitrotype.com/api/v2/teams/{team_name}

    Parameter
    ---------
    team_name : str
        The tag of the team.

    Returns
    -------
    dict
        A dict of the team's information.
    """

    return api("teams/" + str(team_name))
