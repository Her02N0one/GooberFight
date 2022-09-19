import os
import time

import console_util
import engine
import moves
from data import Stats
from engine import BattleEngine
from fighters import Fighter


# TODO: change system to use "curses" instead of regular console logs

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


class ConsoleEngine:
    def __init__(self, main_ui, secondary_ui):
        self.main_ui = main_ui
        self.secondary_ui = secondary_ui

    def change_main_ui(self, menu: callable):
        self.main_ui = menu

    def change_secondary_ui(self, menu: callable):
        self.secondary_ui = menu

    def update(self, battle_engine: BattleEngine):
        console_input = input("> ").lower()
        if console_input == "fight":
            self.change_secondary_ui(lambda: console_util.show_moves(battle_engine.attacker))

        elif console_input in ["", "back", "return"]:
            self.change_secondary_ui(console_util.print_menu)

        elif console_input in ["surrender", "quit", "exit"]:
            return -1

        for move in battle_engine.attacker.moves:
            if console_input == move.name:
                battle_engine.attacker.set_action(move)

    def render(self, battle_engine, update_queue=False):
        clear()
        self.main_ui()
        if battle_engine.has_text() and update_queue:
            console_util.delay_print(battle_engine.pop_text(), 0.05)
            time.sleep(0.08)
        else:
            if battle_engine.attacker.action is None:
                self.secondary_ui()


def main():
    player_1 = Fighter("Goober", Stats(100, 10, 15, 1.1))
    player_2 = Fighter("Shloober", Stats(100, 10, 10, 1.1))

    for move in moves.basic:
        player_1.add_move(move)
    player_2.add_move(moves.test)

    battle_engine = BattleEngine(player_1, player_2)
    console_engine = ConsoleEngine(lambda: console_util.print_battle(player_1, player_2), console_util.print_menu)

    clear()
    # when implemented, "outcome" will tell engine whether to start processing the text queue or not
    for current_round, outcome in battle_engine.wrap(console_engine.update):
        if outcome == -1:
            return -1
        console_engine.render(battle_engine, True)
    clear()


if __name__ == "__main__":
    main()
    clear()
    print("ok")
