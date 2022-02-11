from typing import List, Union
from .....objects.api.info.bootstrap.misc.challenges import Challenges
from ..bootstrap import bootstrap


def challenges(challenge_id=0) -> Union[Challenges, List[Challenges], bool]:
    """Returns the challenge from the bootstrap.

    Endpoint
    --------
        https://www.nitrotype.com/index/624/bootstrap.js

    Parameters
    ----------
    challenge_id : int
        The item to access from the bootstrap.

    Returns
    -------
    dict
        A dict of the challenge, or False if the challenge cannot be found.
    """

    challenge_list = bootstrap("challenges")

    if challenge_id:
        for challenge in challenge_list:
            if str(challenge["challengeID"]) == str(challenge_id):
                return challenge
    else:
        return challenge_list

    return False
