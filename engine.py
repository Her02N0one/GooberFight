from typing import Callable
import time

import console_util
import data
from fighters import Fighter
import random


class GameEngine:
    def __init__(self, *args, **kwargs):
        pass

    def input(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass


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
        self.player = p1
        self.opponent = p2
        self._text_queue = []

    # Fighter related methods
    def get_opponent(self, player):
        if player == self.player:
            return self.opponent
        if player == self.opponent:
            return self.player

    def _activate_move(self, attacker: Fighter):
        self.add_text(f"{attacker.name} used {attacker.action.name}")
        attacker.activate_action(self.get_opponent(attacker), self)
    
    def get_order(self):
        order = [self.player, self.opponent]
        if self.player.stats.speed == self.opponent.stats.speed:
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

    def wrap(self, frontend_engine: GameEngine):
        while True:
            frontend_engine.update(self)
            while self.player.is_idle():
                frontend_engine.input(self)
                frontend_engine.update(self)

            while self.opponent.is_idle():
                self.opponent.set_action(self.opponent.moves[0])  # TODO: player 2 AI will go here.
                frontend_engine.update(self)

            for _ in self._battle_stage():
                frontend_engine.update(self)


      
    def _battle_stage(self):
        if not self.player.is_idle() and not self.opponent.is_idle():
            for current_attacker in self.get_order():
                if not current_attacker.action_is_active():
                    self._activate_move(current_attacker)
                    yield

                for _ in current_attacker.do_action():
                    yield


FAST_TEXT = False
class ConsoleEngine(GameEngine):
    def __init__(self, main_ui, secondary_ui):
        self.main_ui = main_ui
        self.secondary_ui = secondary_ui

    def change_main_ui(self, menu: callable):
        self.main_ui = menu

    def change_secondary_ui(self, menu: callable):
        self.secondary_ui = menu

    def input(self, battle_engine: BattleEngine):
        console_input = input("> ").lower()
        if console_input == "fight":
            self.change_secondary_ui(lambda: console_util.show_moves(battle_engine.player))

        elif console_input in ["", "back", "return"]:
            self.change_secondary_ui(console_util.print_menu)

        elif console_input in ["surrender", "quit", "exit"]:
            return -1

        for move in battle_engine.player.moves:
            if console_input == move.name:
                battle_engine.player.set_action(move)

        
    def update(self, battle_engine):
        console_util.clear()
        self.main_ui()
        if battle_engine.has_text():
            if FAST_TEXT:
                print("  " +battle_engine.pop_text())
                time.sleep(0.25)
            else:
                console_util.delay_print(battle_engine.pop_text(), 0.05)
                time.sleep(0.25)
        else:
            if battle_engine.player.is_idle():
                self.secondary_ui()
