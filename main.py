import os
from data import DefaultStats, Fighter, punch
# TODO: Break up "data" library because it's way too vague

fella = [
    ' o ', 
    '/|\\',
    '/ \\'
]

def progress_bar(percent, length, prefix="", filled="#", empty="_"):
    ammount_filled = int(length*percent)
    return f"{prefix}[{filled*ammount_filled}{empty*(length-ammount_filled)}]"

def print_ui(player1, player2):
    print(f"{player2.name}:     {progress_bar(player2.get_health_percent(), 15)}")
    print(f"HP:{player2.match_stats.hp}/{player2.stats.health}")
    print("\n".join([(" " * 22) + line for line in fella]))
    print("\n".join([(" " * 1) + line for line in fella]))
    print(f"{player1.name}:       {progress_bar(player1.get_health_percent(), 15)}")
    print(f"HP:{player1.match_stats.hp}/{player1.stats.health}")


def print_menu():
    print()
    print("| Fight       Counter   |")
    print("| Special     Surrender |")
    print()

def show_moves(player: Fighter):
    for move in player.moves:
        print(f"| {move}")
    

def main():
    # lots of debug and stub functions here, would love to get rid
    # TODO: create a battle engine class, to handle state in a safer way.
    player_1 = Fighter("Goober", DefaultStats(100, 10, 10, 1.1))
    player_1.add_move(punch)
    player_2 = Fighter("Shloober", DefaultStats(100, 10, 10, 1.1))
    player_2.add_move(punch)

    print_ui(player_1, player_2)
    print_menu()
    while True:

        # take input, then clear and redraw.
        i = input("> ").lower()
        os.system('clear')

        # if the input is the name of a move, have that move be used on the opponent.
        if i in player_1.moves:
            player_1.moves[i].move(player_1, player_2)
        
        
        print_ui(player_1, player_2)
        
        if i == "fight":
            show_moves(player_1)
        elif i == "counter":
            print("NYI")
        elif i == "special":
            print("NYI")
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