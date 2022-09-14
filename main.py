import os
from data import DefaultStats
from fighters import Fighter
import moves
import console_util

# TODO: Break up "data" library because it's way too vague
# TODO: Rework text based drawing system to be more dynamicly generated allowing for decorators and stuff and borders tables etc.
fella = [
    ' o ', 
    '/|\\',
    '/ \\'
]

def progress_bar(percent, length, prefix="", filled="#", empty="_"):
    ammount_filled = int(length*percent)
    return f"{prefix}[{filled*ammount_filled}{empty*(length-ammount_filled)}]"

def print_ui(player1, player2):
    l = [
        f"{player2.name}:     {progress_bar(player2.get_health_percent(), 15)}",
        f"HP:{player2.match_stats.hp}/{player2.stats.health}",
        22*" " + fella[0],
        22*" " + fella[1],
        22*" " + fella[2],
        1*" " + fella[0],
        1*" " + fella[1],
        1*" " + fella[2],
        f"{player1.name}:       {progress_bar(player1.get_health_percent(), 15)}",
        f"HP:{player1.match_stats.hp}/{player1.stats.health}"
    ]

    console_util.draw_border(l)


def print_menu():
    print("╔════════════════╦════════════════╗")
    print("║    Fight       ║   Counter      ║")
    print("╠════════════════╬════════════════╣")
    print("║    Special     ║   Surrender    ║")
    print("╚════════════════╩════════════════╝")

def show_moves(player: Fighter):
    print("╔═════════════════════════════════╗")
    if len(player.moves) > 0:
        for move in player.moves:
            print(f"║  {move} ")
    else:
        print("No Moves!?")
    print("╚═════════════════════════════════╝")

    

def main():
    # lots of debug and stub functions here, would love to get rid
    # TODO: create a battle engine class, to handle state in a safer way.
    player_1 = Fighter("Goober", DefaultStats(100, 10, 10, 1.1))
    for move in moves.basic:
        player_1.add_move(move)
    player_2 = Fighter("Shloober", DefaultStats(100, 10, 10, 1.1))

    print_ui(player_1, player_2)
    print_menu()
    while True:

        # after last frame finishes, take new input, then clear and redraw.
        i = input("> ").lower()
        os.system('clear')

        # if the input is the name of a move, have that move be used on the opponent.
        if i in player_1.moves:
            player_1.moves[i].move(player_1, player_2)
        
        
        print_ui(player_1, player_2)
        
        if i == "fight":
            show_moves(player_1)
        elif i == "counter":
            print("!!NYI!!")
        elif i == "special":
            print("!!NYI!!")
        elif i == "surrender":
            os.system('clear')
            print("ok")
            return 0
        elif i in player_1.moves:
            print_menu()
        elif i == "":
            print_menu()
        else:
            print_menu()
            print(f'did not understand input: "{i}"')

if __name__ == "__main__":
    main()