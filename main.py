import os
from data import DefaultStats

a = 10

fella = [" o ", "/|\\", "/ \\"]


def print_ui():
    print("Goober:      HP:[##########]")
    print("\n".join([(" " * 22) + line for line in fella]))
    print("\n".join(fella))
    print("Shloober:    HP:[##########]")
    print()
    print("| Fight       Counter   |")
    print("| Special     Surrender |")
    print()
    print("what u tryna do?: ")


class Fighter:

    def __init__(self, name, stats: DefaultStats):
        self.name = name
        self.stats = stats


## since it looks better with an enter between the options and the imput thing, u gotta expand ur consol to see the whole screen
def main():
    print_ui()
    while True:
        i = input("> ")
        os.system('clear')
        print_ui()

        if i == "quit":
            return 0
        elif i == "":
            pass
        else:
            print(f'did not understand input: "{i}"')
    return 0


if __name__ == "__main__":
    main()