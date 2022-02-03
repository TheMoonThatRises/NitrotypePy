from typing import List
from .bootstrap.item.loot import Loot


class User:
    def __init__(self):
        self.userID: int
        self.username: str
        self.membership: str
        self.displayName: str
        self.title: str
        self.experience: int
        self.level: int
        self.teamID: int
        self.lookingForTeam: bool
        self.carID: int
        self.carHueAngle: int
        self.totalCars: int
        self.nitros: int
        self.nitrosUsed: int
        self.racesPlayed: int
        self.longestSession: int
        self.avgSpeed: int
        self.highestSpeed: int
        self.allowFriendRequest: bool
        self.profileViews: int
        self.createdStamp: int
        self.tag: str
        self.tagColor: str
        self.garage: List[str]
        self.cars: List[List[int, str, int]]
        self.loot: List[Loot]
