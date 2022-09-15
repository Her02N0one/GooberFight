import console_util
import random

WAIT_FOR_OPPONENT = 0
SKIP_OPPONENTS_TURN = 1

# TODO: move functions which should be static into a seperate file.
class BattleEngine:
    """
    Holds the state of the current battle
    
    Wraps a text buffer that can be appended by reference 
    and will update each frame until done and then return to grabbing input.

    handels all access to private methods
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.text_queue = []
        self.p1_move = None
        self.p2_move = None
        self.current_submenu = self.print_menu

    def print_menu(self):
        print("╔════════════════╦════════════════╗")
        print("║    Fight       ║   Counter      ║")
        print("╠════════════════╬════════════════╣")
        print("║    Special     ║   Surrender    ║")
        print("╚════════════════╩════════════════╝")

    
    def show_moves(self, player):
        print("╔═════════════════════════════════╗")
        if len(player.moves) > 0:
            for move in player.moves:
                print(f"║  {move}" + " "*(35-len(move)-4) + "║")
        else:
            print("ERROR: No Moves!?")
        print("╚═════════════════════════════════╝")

    
    def parse_input(self, i):
        # TODO: maybe handle parsing inputs outside of the engine. so that it can stand on it's own.
        i = i.lower()
        if i == "fight":
            self.current_submenu = lambda: self.show_moves(self.p1)
        if i == "" or i.lower() == "back":
            self.current_submenu = self.print_menu
        if i in self.p1.moves:
            self.p1_move = self.p1.moves[i].move(self.p1, self.p2, self)
            print("test")
            self.text_queue.append(f"{self.p1.name} used {self.p1.moves[i].name}")
        if i == "special":
            pass
        if i == "surrender":
            return -2
    
    def update(self):
        outcome = None
        if self.p1_move is not None:
            try:
                outcome = next(self.p1_move)
            except StopIteration:
                self.p1_move = None
        
        if outcome == WAIT_FOR_OPPONENT:
            # self.p2_move = random.choice(self.p2.moves)
            print(self.p2_move)
        
        self.print_battle()
        self.print_sub_menu()

    
    def print_battle(self):
        p1_data = console_util.player_data(self.p1)
        p2_data = console_util.player_data(self.p2)
        p1_design = console_util.offset_multiline(self.p1.design, 1)
        p2_design = console_util.offset_multiline(self.p2.design, 22)

        console_util.draw_border(
            [
                *p2_data,
                *p2_design,
                *p1_design,
                *p1_data
            ]
        )

    def print_sub_menu(self):
        if len(self.text_queue) > 0:
            console_util.delay_print(self.text_queue[0], 0.05)
            self.text_queue.remove(self.text_queue[0])
            return
        self.current_submenu()
        