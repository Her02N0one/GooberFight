import sys
import time


def draw_border(text_array):
    a = len(max(text_array, key=len))
    print("╔" + ("═" * (a + 2) + "╗"))
    for line in text_array:
        print("║ " + line + " " * ((a - len(line))) + " ║")
    print("╚" + ("═" * (a + 2) + "╝"))


def progress_bar(percent, length, prefix="", filled="#", empty="_"):
    ammount_filled = int(length * percent)
    return f"{prefix}[{filled * ammount_filled}{empty * (length - ammount_filled)}]"


def player_data(player):
    return [
        f"{player.name}",
        f"HP:{int(player.match_stats.hp)}/{player.stats.health}    {progress_bar(player.get_health_percent(), 15)}",
    ]


def offset_multiline(string_array, offset):
    return [offset * " " + line for line in string_array]


def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()
    time.sleep(0.2)


def table(w, h):
    pass
