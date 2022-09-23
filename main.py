import console_util
import moves
from data import Stats
from engine import BattleEngine, ConsoleEngine
from fighters import Fighter


# TODO: change system to use "curses" instead of regular console logs
def main():
    player_1 = Fighter("Goober", Stats(1000, 10, 15, 1.1))
    player_2 = Fighter("Shloober", Stats(1000, 10, 10, 1.1))

    style_input = input("choose style: ")
    if style_input == "boxing":
        [player_1.add_move(move) for move in moves.boxing]
    else:
        [player_1.add_move(move) for move in moves.basic]
        
    player_2.add_move(moves.test)
    battle_engine = BattleEngine(player_1, player_2)
    console_engine = ConsoleEngine(lambda: console_util.print_battle(player_1, player_2), console_util.print_menu)

    console_util.clear()
    battle_engine.wrap(console_engine)
    console_util.clear()


if __name__ == "__main__":
    main()
    console_util.clear()
    print("ok")
