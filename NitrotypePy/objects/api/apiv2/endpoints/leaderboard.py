from typing import List, TypedDict


class LeaderboardTeams(TypedDict):
    typed: int
    secs: int
    played: int
    points: int
    speed: str
    dayRank: int
    prevRank: int
    rank: int
    teamID: int
    tag: str
    tagColor: str
    name: str
    createdStamp: int
    members: int
    userID: int


class Leaderboard:
    scores: List[LeaderboardTeams]
