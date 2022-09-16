import os
import random

import engine
import moves
import console_util
from data import DefaultStats, PlayerStates
from fighters import Fighter


# TODO: change system to use "curses" instead of regular console logs


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def main():
    player_1 = Fighter("Player  1", DefaultStats(100, 10, 10, 1.1))
    player_2 = Fighter("Player  2", DefaultStats(100, 10, 10, 1.1))

    for move in moves.basic:
        player_1.add_move(move)

    for move in moves.basic:
        player_2.add_move(move)

    game_engine = engine.BattleEngine(player_1, player_2)
    # game_engine.text_queue.append("yo this a test")
    # game_engine.text_queue.append("fr yo we be testin")

    while True:

        if player_1.active_move is None:
            if player_2.state == PlayerStates.WAIT_FOR_OPPONENT:
                console_input = input("> ").lower()
    
        if player_2.active_move is None:
            if player_1.state == PlayerStates.WAIT_FOR_OPPONENT:
                move = random.choice(list(player_2.moves.items()))
                print(move)
                game_engine.activate_move(player_2, player_1, move[1])

        
        if console_input == "fight":
            game_engine.change_submenu(lambda: console_util.show_moves(player_1))
        elif console_input in player_1.moves:
            game_engine.activate_move(player_1, player_2, player_1.moves[console_input])
        elif console_input == "" or console_input == "back":
            game_engine.change_submenu(console_util.print_menu)
            
        clear()
        game_engine.update()


if __name__ == "__main__":
    main()
    clear()
    print("ok")
