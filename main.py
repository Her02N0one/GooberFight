import os
import time

import console_util
import engine
import moves
from data import Stats
from engine import BattleEngine
from fighters import Fighter


# TODO: change system to use "curses" instead of regular console logs

# TODO: Rename all instances of "move" to action. because the "move" system will actually be the only system for
#  triggering events

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


class ConsoleEngine:
    def __init__(self, battle_engine: engine.BattleEngine, main_ui, secondary_ui):
        self.main_ui = main_ui
        self.secondary_ui = secondary_ui
        self.battle_engine = battle_engine
        self.player_1 = self.battle_engine.p1
        self.player_2 = self.battle_engine.p2

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
            if self.player_1.action is None:
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
            
            while player_1.idle():  # take input and update ui until a move is selected.
                console_input = input("> ").lower()

                if console_input == "fight":
                    console_engine.change_secondary_ui(lambda: console_util.show_moves(player_1))

                elif console_input in ["", "back", "return"]:
                    console_engine.change_secondary_ui(console_util.print_menu)

                elif console_input in ["surrender", "quit", "exit"]:
                    return

                for move in player_1.moves:
                    if console_input == move.name:
                        player_1.activate_move(move)

                console_engine.update_console()




if __name__ == "__main__":
    clear()
    main()
    clear()
    print("ok")
