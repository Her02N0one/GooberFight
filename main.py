import os
from data import DefaultStats
from fighters import Fighter
import moves
import console_util
import engine

# TODO: change system to use "curses" instead of regualr console logs
# will tramendously increase the things that we can do. ui can be navigated with arrowkeys etc.
# however it also increases render complexity so maybe I'll do that once we've at least got opponent ai implemented
# ohhhhsdfhksdjfhs

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
        os.system('clear')
        game_engine.update()


if __name__ == "__main__":
    if (debug := False):
        import repl_test
    else:
        main()
        os.system('clear')
        print("ok")
