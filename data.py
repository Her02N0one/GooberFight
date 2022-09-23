from dataclasses import dataclass
from enum import Enum

from typing import Callable, Iterator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import BattleEngine
    from fighters import Fighter


@dataclass
class Stats:
    health: float
    defence: float
    speed: float
    attack: float


class ActionState(Enum):
    END = 0  # action_generator is done, and is set to None
    PAUSE = 1  # action_generator is done, but is not set to None
    CONTINUE = 2  # action_generator is not done.

class BattleState(Enum):
    CHOICE = 0
    

# TODO: actions should have a second, optional callable. that describes how it changes the players state. weather or not state is reverted will be described in the generator.
# it's basically the same as the primary action, except it's called before the main battle state begins.
@dataclass
class Action:
    """Container for actions that modify battle state.

    This is the body of the docstring description.
    """
    
    name: str
    action_generator: Callable[['Fighter', 'BattleEngine'], Iterator[ActionState]]
