
class ActionState(Enum):
    END = 0  # action_generator is done, and is set to None
    PAUSE = 1  # action_generator is done, but is not set to None
    CONTINUE = 2  # action_generator is not done.


@dataclass
class Action:
    name: str
    action_generator: Callable[['Fighter', 'Fighter', 'BattleEngine'], Iterator[ActionState]]
