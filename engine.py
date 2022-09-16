import random
import console_util
from fighters import Fighter
import data



# TODO: move functions which should be static into a separate file.
class BattleEngine:
    """
    Holds the state of the current battle
    
    Wraps a text buffer that can be appended by reference 
    and will update each frame until done and then return to grabbing input.

    handles all access to private methods
    """

    def __init__(self, p1: Fighter, p2: Fighter):
        self.p1 = p1
        self.p2 = p2
        self.text_queue = []
        self.current_submenu = console_util.print_menu

    # maybe "submenu" could be a class instead of a function
    def change_submenu(self, new_submenu):
        self.current_submenu = new_submenu
    
    def activate_move(self, player: Fighter, opponent: Fighter, attack: data.DefaultAttack):
        player.active_move = attack.move(player, opponent, self)
    

    def update(self):

        if self.p1.active_move is not None:
            try:
                self.p1.state = next(self.p1.active_move)
            except StopIteration:
                self.p1.active_move = None

        if self.p2.active_move is not None:
            try:
                self.p1.state = next(self.p2.active_move)
            except StopIteration:
                self.p2.active_move = None

        
        console_util.print_battle(self.p1, self.p2)
        self.print_sub_menu()

    def print_sub_menu(self):
        if len(self.text_queue) > 0:
            console_util.delay_print(self.text_queue[0], 0.05)
            self.text_queue.remove(self.text_queue[0])
            return
        self.current_submenu()
