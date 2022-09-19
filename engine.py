from typing import Callable

import data
from fighters import Fighter
import random

# TODO: make sure certain methods are "private"
# and make sure state can be modified with it's public methods
class BattleEngine:
    """
    Holds the state of the current battle
    
    Wraps a text buffer that should hold info on what's happening, to display.
    """

    def __init__(self, p1: Fighter, p2: Fighter):
        self.attacker = p1
        self.opponent = p2
        self._text_queue = []

    # Fighter related methods
    def get_opponent(self, player):
        if player == self.attacker:
            return self.opponent
        if player == self.opponent:
            return self.attacker

    def get_order(self):
        order = [self.attacker, self.opponent]

        if self.attacker.stats.speed == self.opponent.stats.speed:
            random.shuffle(order)
        else:
            order.sort(key=lambda fighter: fighter.stats.speed, reverse=True)

        return order

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

    def wrap(self, func):
        for current_round in self._update():
            for outcome in self._scheduled_state_change(func):
                yield current_round, outcome

    def _scheduled_state_change(self, func):
        yield  # return to render before parsing, so screen can appear
        while self.attacker.is_idle() and (self.opponent.is_idle() or self.opponent.state == data.ActionState.PAUSE):
            yield func(self)

    # heart of the engine
    def _update(self):
        current_round = 0
        while True:
            current_round += 1
            if not self.attacker.is_idle() and self.opponent.action is None:
                # player 2 AI will go here.
                self.opponent.set_action(self.opponent.moves[0])

            if self.attacker.action is not None and self.opponent.action is not None:

                for current_attacker in self.get_order():

                    if not current_attacker.action_is_active():
                        self.add_text(f"{current_attacker.name} used {current_attacker.action.name}")
                        current_attacker.activate_action(self.get_opponent(current_attacker), self)
                        yield

                    for _ in current_attacker.do_action():
                        yield current_round
            yield current_round


"""
game engine should be able to handle all possible states of the game.
which means the battle engine could potentially become more of an abstract class.
"""


class GameEngine:
    def __init__(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def render(self, *args, **kwargs):
        pass
