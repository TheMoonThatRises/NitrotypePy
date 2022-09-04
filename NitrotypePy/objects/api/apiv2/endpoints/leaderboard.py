from typing import TypedDict

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
