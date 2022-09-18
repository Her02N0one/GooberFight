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
    def __init__(self, battle_engine: BattleEngine, main_ui, secondary_ui):
        self.main_ui = main_ui
        self.secondary_ui = secondary_ui
        self.battle_engine = battle_engine
        self.attacker = self.battle_engine.attacker
        self.opponent = self.battle_engine.opponent

    def parse_input(self, console_input: str):
        console_input = console_input.lower()
        if console_input == "fight":
            self.change_secondary_ui(lambda: console_util.show_moves(self.attacker))

        elif console_input in ["", "back", "return"]:
            self.change_secondary_ui(console_util.print_menu)

        elif console_input in ["surrender", "quit", "exit"]:
            return

        for move in self.battle_engine.attacker.moves:
            if console_input == move.name:
                self.battle_engine.attacker.activate_move(move)

    def change_main_ui(self, menu: callable):
        self.main_ui = menu

    def change_secondary_ui(self, menu: callable):
        self.secondary_ui = menu

    def update_console(self):
        clear()
        self.main_ui()
        if self.battle_engine.has_text():
            console_util.delay_print(self.battle_engine.pop_text(), 0.05)
            time.sleep(0.08)
        else:
            if self.attacker.action is None:
                self.secondary_ui()


def main():
    player_1 = Fighter("Player 1", Stats(100, 10, 10, 1.1))
    player_2 = Fighter("Player 2", Stats(100, 10, 20, 1.1))

    for move in moves.basic:
        player_1.add_move(move)

    player_2.add_move(moves.test)

    battle_engine = BattleEngine(player_1, player_2)
    console_engine = ConsoleEngine(battle_engine, lambda: console_util.print_battle(player_1, player_2),
                                   console_util.print_menu)

    while True:
        for _ in battle_engine.update():
            console_engine.update_console()

            while battle_engine.attacker.is_idle():
                console_engine.parse_input(input("> ").lower())
                console_engine.update_console()


if __name__ == "__main__":
    clear()
    main()
    clear()
    print("ok")
