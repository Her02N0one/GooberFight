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
    handles access to fighter instances.
    """

    def __init__(self, p1: Fighter, p2: Fighter):
        # should all be private members
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
            order.sort(key=lambda fighter: fighter.stats.speed, reverse=True)  # sort list by speed

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
        yield 0
        while True:
            # input state
            while self.attacker.is_idle():
                yield func(self)

            # battle state
            for _ in self._update():
                yield 0

    def _activate_move(self, attacker: Fighter):
        self.add_text(f"{attacker.name} used {attacker.action.name}")
        attacker.activate_action(self.get_opponent(attacker), self)

    # heart of the engine
    def _update(self):
        if self.opponent.is_idle():
            # TODO: player 2 AI will go here.
            self.opponent.set_action(self.opponent.moves[0])

        # TODO: make action system handling work for actions that happen during the input state.
        if not self.attacker.is_idle() and not self.opponent.is_idle():
            for current_attacker in self.get_order():
                if not current_attacker.action_is_active():
                    self._activate_move(current_attacker)
                    yield

                for _ in current_attacker.do_action():
                    yield
        yield


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
