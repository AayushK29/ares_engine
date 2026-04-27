from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    username: str
    elo: int
    latency: int
    region: str 

class PartyJoin(BaseModel):
    players: List[Player]
