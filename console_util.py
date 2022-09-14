
def draw_border(text_array):
    a = len(max(text_array, key=len))
    print("╔" + ("═" * (a+2) + "╗"))
    for line in text_array:
        print("║ " + line + " " * ((a-len(line))) + " ║")
    print("╚" + ("═" * (a+2) + "╝"))
