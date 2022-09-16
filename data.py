from dataclasses import dataclass
from enum import Enum


# select next move = allow player to input values
# wait for opponent = stop move, 

# this is really boggling me rn...

"""

if p1 has no running move and p2 is waiting for opponent
    p1 choses move
    
if p2 has no running move and p1 is waiting for opponent
    p2 choses move

if p2 code is skipping opponents turn, p1 is skipped
    otherwise p1 move code is run and is assigned to state

if p1 is skipping opponents turn, p2 is skipped
    otherwise p2 code is run
"""

class PlayerStates(Enum):
    WAIT_FOR_OPPONENT = 0
    MOVE_END = 0
    SKIP_OPPONENTS_TURN = 1


@dataclass
class DefaultStats:
    health: float
    defence: float
    speed: float
    attack: float



#I thing the "move" system should be used for more than just attacks. 
# it'll be more like an event queue system.
@dataclass
class DefaultAttack:
    name: str
    move: callable
