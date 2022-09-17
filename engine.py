
import data
from fighters import Fighter


class BattleEngine:
    """
    Holds the state of the current battle
    
    Wraps a text buffer that should hold info on what's happening, to display.
    """

    def __init__(self, p1: Fighter, p2: Fighter):
        self.p1 = p1
        self.p2 = p2
        self._text_queue = []

    # Fighter related methods
    def get_opponent(self, player):
        if player == self.p1:
            return self.p2
        if player == self.p2:
            return self.p1

    def get_order(self):
        order = [self.p1, self.p2]
        order.sort(key=lambda fighter: fighter.stats.speed, reverse=True)
        return order

    # Action Related methods
    def activate_action(self, attacker: Fighter):
        if type(attacker.action) == data.Action:
            self.add_text(f"{attacker.name} used {attacker.action.name}")
            attacker.action = attacker.action.action(attacker, self)
            attacker.state = data.ActionState.CONTINUE

    def do_action(self, attacker: Fighter):
        self.activate_action(attacker)
        yield

        for _ in attacker.do_action():
            yield

    # text queue methods
    def has_text(self):
        return len(self._text_queue) > 0

    def pop_text(self):
        if self.has_text():
            text = self._text_queue[0]
            self._text_queue.remove(self._text_queue[0])
            return text

    def add_text(self, text: str):
        self._text_queue.append(text)

    # heart of the engine
    def update(self):
        while True:
            if self.p2.action is None:
                # player 2 AI will go here.
                self.p2.activate_move(self.p2.moves[0])

            if self.p1.action is not None and self.p2.action is not None:
                for player in self.get_order():
                    for _ in self.do_action(player):
                        yield
            yield
