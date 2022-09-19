import data

fella = (
    ' o ',
    '/|\\',
    '/ \\'
)


# will NEVER be passed battle engine as an argument directly. meant to stand on its own
# engine should never be imported into this module

class Fighter:  # TODO: use functions to access dataclasses, shortens code and increases readability
    move_limit = 4

    def __init__(self, name, stats, design=fella):
        # copy of things that can change per battle. so that they can be reverted when necessary
        self._name = name
        self._design = design
        self._stats = stats

        self.name = self._name
        self.design = self._design
        self.stats = self._stats
        self.hp = self.stats.health

        # could be coupled
        # TODO: change to action "queue" system
        # so that not all actions have to end the players turn.
        self.action = None
        self.state = None

        self.moves = []

        self.alive = True

    def is_idle(self):
        return self.action is None 

    def action_is_active(self):
        return (self.action is not None) and (type(self.action) != data.Action)

    def add_move(self, move: data.Action):
        if (len(self.moves) + 1) <= self.move_limit:
            self.moves.append(move)

    def set_action(self, action):
        self.action = action

    def activate_action(self, opponent, engine):
        if not self.action_is_active():
            self.action = self.action.action_generator(self, opponent, engine)
            self.state = data.ActionState.CONTINUE

    def do_action(self):
        while self.action_is_active():
            self.iterate_action()
            yield
            if self.state == data.ActionState.CONTINUE:
                continue
            if self.state == data.ActionState.PAUSE:
                break

    def iterate_action(self):
        try:
            self.state = next(self.action)
        except StopIteration:
            self.finish_action()

        if self.state == data.ActionState.END:
            self.finish_action()

    def finish_action(self):
        self.action = None
        self.state = None

    def get_health_percent(self):
        return self.hp / self.stats.health

    def reset_stats(self):
        self.name = self._name
        self.design = self._design
        self.stats = self._stats
        self.alive = True

    def decrease_hp(self, amount):
        if self.hp == 0:
            return -1

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0
            self.alive = False
            return -1

        return self.hp
