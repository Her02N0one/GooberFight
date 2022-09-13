from dataclasses import dataclass


@dataclass
class DefaultStats:
    health: float
    defence: float
    speed: float
    attack: float


@dataclass
class DefultAttack:
    name: str
    move: callable


@dataclass
class DefultStyle:
    name : str
    moves : list