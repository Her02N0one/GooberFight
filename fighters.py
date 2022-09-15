import data

fella = [
    ' o ',
    '/|\\',
    '/ \\'
]
smella = [
    ' + ',
    '/|\\',
    '/ \\'
]


class Fighter:  # TODO: use functions to access dataclasses, shortens code and increases readability
    move_limit = 4

    def __init__(self, name, stats, design=fella):
        self.name = name
        self.stats = stats
        self.design = design
        self.match_stats = data.PerFightStats(stats, stats.health, 0)
        self.moves = dict()
        self.alive = True

    def get_health_percent(self):
        return self.match_stats.hp / self.stats.health

    def start_match(self):  # will be called by engine automatically.
        # reset any stats that were temporarily changed when match starts
        self.match_stats = data.PerFightStats(self.stats, self.stats.health, 0)
        self.alive = True

    def add_move(self, move: data.DefaultAttack):
        if (len(self.moves) + 1) <= self.move_limit:
            self.moves[move.name] = move

    def decrease_hp(self, amount):
        if (self.match_stats.hp - self.match_stats.hp) < 0:
            self.alive = False
            return -1
        self.match_stats.hp -= amount

    def power_up(self, stats, design=smella):
        self.match_stats.hp + 20
        self.match_stats.attack + 10
        self.match_stats.defense - 5
