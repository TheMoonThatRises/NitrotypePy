from typing import TypedDict


Challenges = TypedDict(
    "Challenges",
    {
        "challengeID": int,
        "duration": str,
        "type": str,
        "reward": int,
        "goal": int,
        "expiration": int,
    },
)
