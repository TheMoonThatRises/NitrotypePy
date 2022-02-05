from typing import List, TypedDict


LeaderboardTeams = TypedDict(
    "LeaderboardTeams",
    {
        "typed": int,
        "secs": int,
        "played": int,
        "points": int,
        "speed": str,
        "dayRank": int,
        "prevRank": int,
        "rank": int,
        "teamID": int,
        "tag": str,
        "tagColor": str,
        "name": str,
        "createdStamp": int,
        "members": int,
        "userID": int,
    },
)


Leaderboard = TypedDict("Leaderboard", {"scores": List[LeaderboardTeams]})
