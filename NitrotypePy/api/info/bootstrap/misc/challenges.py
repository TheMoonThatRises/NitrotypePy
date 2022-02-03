from typing import List, Union
from .....objects.api.info.bootstrap.misc.challenges import Challenges
from ..bootstrap import bootstrap


def challenges(challenge_id=0) -> Union[Challenges, List[Challenges], bool]:
    challenge_list = bootstrap('challenges')

    if challenge_id:
        for challenge in challenge_list:
            if challenge['challengeID'] == challenge_id:
                return challenge
    else:
        return challenge_list

    return False
