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
        self.action = None
        self.state = None

        self.moves = []

        self.alive = True

    def add_move(self, move: data.Action):
        if (len(self.moves) + 1) <= self.move_limit:
            self.moves.append(move)

    def activate_move(self, move):
        if move in self.moves:
            self.action = move
        else:
            return -1

    def do_action(self):
        if self.action is not None:
            while True:
                self.iterate_action()

                if self.action is None or self.state == data.ActionState.PAUSE:
                    break
                if self.state == data.ActionState.CONTINUE:
                    yield
            yield

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
