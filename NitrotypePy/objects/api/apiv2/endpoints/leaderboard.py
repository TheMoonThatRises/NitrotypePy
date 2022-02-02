from typing import List


class LeaderboardTeams:
    def __init__(self):
        self.typed: int
        self.secs: int
        self.played: int
        self.points: int
        self.speed: str
        self.dayRank: int
        self.prevRank: int
        self.rank: int
        self.teamID: int
        self.tag: str
        self.tagColor: str
        self.name: str
        self.createdStamp: int
        self.members: int
        self.userID: int


class Leaderboard:
    def __init__(self):
        self.scores: List[LeaderboardTeams]
