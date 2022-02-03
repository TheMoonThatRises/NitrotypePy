from typing import TypedDict

class Challenges(TypedDict):
    challengeID: int
    duration: str
    type: str
    reward: int
    goal: int
    expiration: int
