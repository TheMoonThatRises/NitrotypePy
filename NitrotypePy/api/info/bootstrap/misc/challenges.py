from typing import List, Union
from .....objects.api.info.bootstrap.misc.challenges import Challenges
from ..bootstrap import bootstrap


def challenges(challenge_id=0) -> Union[Challenges, List[Challenges], bool]:
    """Returns the challenge from the bootstrap.

    Endpoint: https://www.nitrotype.com/index/624/bootstrap.js

    :param challenge_id: The item to access from the bootstrap.
    :type challenge_id: int
    :returns: A dict of the challenge, or False if the challenge cannot be found.
    :rtype: dict
    """

    challenge_list = bootstrap("challenges")

    if challenge_id:
        for challenge in challenge_list:
            if challenge["challengeID"] == challenge_id:
                return challenge
    else:
        return challenge_list

    return False
