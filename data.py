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
    END = 0  # action is done, and is set to None
    PAUSE = 1  # action is done, but is not set to None
    CONTINUE = 2  # action is not done.


@dataclass
class Action:
    """Container for actions that modify battle state.

    This is the body of the docstring description.
    """

    name: str
    action: Callable[['Fighter', 'BattleEngine'], Iterator[ActionState]]
