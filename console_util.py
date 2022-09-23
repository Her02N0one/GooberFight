import sys
import time
import os

from fighters import Fighter


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def draw_border(text_array):
    a = len(max(text_array, key=len))
    print("╔" + ("═" * (a + 2) + "╗"))
    for line in text_array:
        print("║ " + line + " " * (a - len(line)) + " ║")
    print("╚" + ("═" * (a + 2) + "╝"))


def progress_bar(percent, length, prefix="", filled="#", empty="_"):
    amount_filled = int(length * percent)
    return f"{prefix}[{filled * amount_filled}{empty * (length - amount_filled)}]"


def player_data(player: Fighter):
    return [
        f"{player.name}",
        f"HP:{int(player.hp)}/{player.stats.health}    {progress_bar(player.get_health_percent(), 15)}",
    ]


def offset_multiline(string_array, offset):
    return [offset * " " + line for line in string_array]


def delay_print(text, delay):
    print("  ", end='')
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()
    time.sleep(0.2)


def print_battle(p1, p2):
    p1_data = player_data(p1)
    p2_data = player_data(p2)
    p1_design = offset_multiline(p1.design, 1)
    p2_design = offset_multiline(p2.design, 22)

    draw_border(
        [
            *p2_data,
            *p2_design,
            *p1_design,
            *p1_data
        ]
    )


def print_menu():
    print("╔════════════════╦════════════════╗")
    print("║    Fight       ║   Counter      ║")
    print("╠════════════════╬════════════════╣")
    print("║    Special     ║   Surrender    ║")
    print("╚════════════════╩════════════════╝")


def show_moves(player):
    print("╔═════════════════════════════════╗")
    if len(player.moves) > 0:
        for move in player.moves:
            print(f"║  {move.name}" + " " * (35 - len(move.name) - 4) + "║")
    else:
        print("ERROR: No Moves!?")
    print("╚═════════════════════════════════╝")
