import os

import engine
import moves
from data import DefaultStats
from fighters import Fighter


# TODO: change system to use "curses" instead of regular console logs


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def main():
    player_1 = Fighter("Goober", DefaultStats(100, 10, 10, 1.1))
    player_2 = Fighter("Shloober", DefaultStats(100, 10, 10, 1.1))

    for move in moves.basic:
        player_1.add_move(move)

    for move in moves.basic:
        player_2.add_move(move)

    game_engine = engine.BattleEngine(player_1, player_2)
    # game_engine.text_queue.append("yo this a test")
    # game_engine.text_queue.append("fr yo we be testin")

    while True:
        if len(game_engine.text_queue) < 1 and game_engine.p1_move is None:
            output = game_engine.parse_input(input("> "))
            if output == -2:
                return -1
        clear()
        game_engine.update()


if __name__ == "__main__":
    main()
    clear()
    print("ok")
