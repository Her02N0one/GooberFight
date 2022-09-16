import random

import console_util

WAIT_FOR_OPPONENT = 0
SKIP_OPPONENTS_TURN = 1
SKIP_PLAYERS_TURN = 2


# TODO: move functions which should be static into a separate file.
class BattleEngine:
    """
    Holds the state of the current battle
    
    Wraps a text buffer that can be appended by reference 
    and will update each frame until done and then return to grabbing input.

    handles all access to private methods
    """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.text_queue = []
        self.p1_move = None
        self.p2_move = None
        self.p1_outcome = None
        self.p2_outcome = None
        self.current_submenu = console_util.print_menu

    def parse_input(self, i):
        # TODO: maybe handle parsing inputs outside of the engine. so that it can stand on it's own.
        i = i.lower()
        if i == "fight":
            self.current_submenu = lambda: console_util.show_moves(self.p1)
        elif i == "" or i.lower() == "back":
            self.current_submenu = console_util.print_menu

        elif i in self.p1.moves:

            self.p1_move = self.p1.moves[i].move(self.p1, self.p2, self)
            self.text_queue.append(f"{self.p1.name} used {self.p1.moves[i].name}")

            mv = random.choice(list(self.p2.moves.keys()))
            self.p2_move = self.p2.moves[mv].move\
                (self.p2, self.p1, self)
            self.text_queue.append(f"{self.p2.name} used {mv}")

        elif i == "special":
            pass
        elif i == "surrender":
            return -2

    def update(self):
        """

        :return:
        """
        # holy fucking shit this code is so bad to look at I hate it
        # TODO: Fix this grossness

        if self.p1_move is not None:
            try:
                self.p1_outcome = next(self.p1_move)
            except StopIteration:
                self.p1_move = None
                self.p1_outcome = None


        if self.p1_outcome == WAIT_FOR_OPPONENT:
            move = random.choice(list(self.p2.moves.keys()))
            self.p2_move = self.p2.moves[move].move(self.p2, self.p1, self)
            self.text_queue.append(f"{self.p2.name} used {move}")

        if self.p2_outcome != WAIT_FOR_OPPONENT:
            if self.p2_move is not None:
                try:
                    self.p2_outcome = next(self.p2_move)
                except StopIteration:
                    self.p2_move = None
                    self.p2_outcome = None

        console_util.print_battle(self.p1, self.p2)
        self.print_sub_menu()

    def print_sub_menu(self):
        if len(self.text_queue) > 0:
            console_util.delay_print(self.text_queue[0], 0.05)
            self.text_queue.remove(self.text_queue[0])
            return
        self.current_submenu()
