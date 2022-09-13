import os
from data import DefaultStats, Fighter, punch

secret_code = "test"
a = 10

fella = [" o ", "/|\\", "/ \\"]

def progress_bar(percent, length, prefix="HP:", filled="#", empty="_"):
    ammount_filled = int(length*percent)
    return f"HP:[{filled*ammount_filled}{empty*(length-ammount_filled)}]"

def print_ui(player1, player2):
    pass
    print(f"{player2.name}:      {progress_bar(player2.get_health_percent(), 10)}")
    print("\n".join([(" " * 22) + line for line in fella]))
    print("\n".join(fella))
    print(f"{player1.name}:      {progress_bar(player1.get_health_percent(), 10)}")

def print_menu():
    print()
    print("| Fight       Counter   |")
    print("| Special     Surrender |")
    print()

def show_moves(player: Fighter):
    for move in player.moves:
        print(move)
    

def main():
    player_1 = Fighter("Goober", DefaultStats(100, 10, 10, 1.1))
    player_1.add_move(punch)
    player_2 = Fighter("Shloober", DefaultStats(100, 10, 10, 1.1))
    player_2.add_move(punch)

    print("Hit enter to start...")
    
    while True:
        i = input("> ")
        os.system('clear')
        print_ui(player_1, player_2)
        print("what u tryna do?: ")

        print()
        if i == "quit":
            return 0
        elif i == "fight":
            show_moves(player_1)
        elif i in player_1.moves:
            player_1.moves[i].move(player_1, player_2)
        else:
            print(f'did not understand input: "{i}"')
    return 0


if __name__ == "__main__":
    main()