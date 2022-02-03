from typing import Union
from ..access import access
from ...objects.api.info.user import User
import re
import json


def user(username='') -> Union[User, bool]:
    user_page = access('racer/' + username)
    user_data = re.findall("RACER_INFO.+\]\},", user_page)

    if user_data:
        return json.loads(user_data[0][12:-1])
    else:
        return False
