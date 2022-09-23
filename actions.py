from dataclasses import dataclass
from enum import Enum

from typing import Callable, Iterator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import BattleEngine
    from fighters import Fighter

# TODO: add action class here. maybe make it a class and not a dataclass.
class ActionState(Enum):
    END = 0  # action_generator is done, and is set to None
    PAUSE = 1  # action_generator is done, but is not set to None
    CONTINUE = 2  # action_generator is not done.

@dataclass
class Action:
    state: ActionState
    name: str
    action_generator: Callable[['Fighter', 'Fighter', 'BattleEngine'], Iterator[ActionState]]


class ActionBuilder:
    def __init__(self, id: str):
        self.id = id
        self.state = None

    def 
    
    def build(self, attacker, opponent, engine) -> Action:
        pass



if __name__ == '__main__':
    print(ActionFactory())