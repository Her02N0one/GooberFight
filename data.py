from dataclasses import dataclass

@dataclass
class DefaultStats:
    health: float
    defence: float
    speed: float
    attack: float

@dataclass
class PerFightStats: # will be reset to defaults after every fight
    modifiable_stats: DefaultStats
    hp: float
    battle_conditions: int # flags for conditions, probably. unused so far

@dataclass
class DefaultAttack:
    name: str
    move: callable
