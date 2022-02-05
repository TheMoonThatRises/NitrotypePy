from typing import Union
from ..access import access
from ...objects.api.info.user import User
import re
import json


def user(username="") -> Union[User, bool]:
    """Returns the user's information.

    If news_id is specified, then it will return that specific news.
    Endpoint: https://www.nitrotype.com/racer/{username}

    :param username: The player's username.
    :type username: str
    :returns: A dict of the user's information, or False if user cannot be found.
    :rtype: dict
    """

    user_page = access("racer/" + username)
    user_data = re.findall("RACER_INFO.+\]\},", user_page)

    if user_data:
        return json.loads(user_data[0][12:-1])
    else:
        return False
