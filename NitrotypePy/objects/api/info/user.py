from typing import List, Tuple, TypedDict
from .bootstrap.item.loot import Loot


User = TypedDict(
    "User",
    {
        "userID": int,
        "username": str,
        "membership": str,
        "displayName": str,
        "title": str,
        "experience": int,
        "level": int,
        "teamID": int,
        "lookingForTeam": bool,
        "carID": int,
        "carHueAngle": int,
        "totalCars": int,
        "nitros": int,
        "nitrosUsed": int,
        "racesPlayed": int,
        "longestSession": int,
        "avgSpeed": int,
        "highestSpeed": int,
        "allowFriendRequest": bool,
        "profileViews": int,
        "createdStamp": int,
        "tag": str,
        "tagColor": str,
        "garage": List[str],
        "cars": List[Tuple[int, str, int]],
        "loot": List[Loot],
    },
)
