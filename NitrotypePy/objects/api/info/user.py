from typing import List, TypedDict
from .bootstrap.item.loot import Loot


class User(TypedDict):
    userID: int
    username: str
    membership: str
    displayName: str
    title: str
    experience: int
    level: int
    teamID: int
    lookingForTeam: bool
    carID: int
    carHueAngle: int
    totalCars: int
    nitros: int
    nitrosUsed: int
    racesPlayed: int
    longestSession: int
    avgSpeed: int
    highestSpeed: int
    allowFriendRequest: bool
    profileViews: int
    createdStamp: int
    tag: str
    tagColor: str
    garage: List[str]
    cars: List[List[int, str, int]]
    loot: List[Loot]
