import data

fella = [' o ', '/|\\', '/ \\']
smella = [' + ', '/|\\', '/ \\']


class Fighter:  # TODO: use functions to access dataclasses, shortens code and increases readability
    move_limit = 4

    def __init__(self, name, stats, design=fella):
        # copy of things that can change per battle. so that they can be reverted when nessicary
        self._name = name
        self._design = design
        self._stats = stats

        
        self.name = self._name
        self.design = self._design
        self.stats = self._stats
        self.hp = self.stats.health
        
        self.active_move = None
        self.state = data.PlayerStates.WAIT_FOR_OPPONENT

        self.moves = dict()
        
        self.alive = True
        self.powered = False
    
    def get_health_percent(self):
        return self.hp / self.stats.health

    def reset_stats(self):
        self.name = self._name
        self.design = self._design
        self.stats = self._stats
        self.alive = True

    def add_move(self, move: data.DefaultAttack):
        if (len(self.moves) + 1) <= self.move_limit:
            self.moves[move.name] = move

    def decrease_hp(self, amount):
        if self.hp == 0:
            return -1
            
        self.hp -= amount
        
        if self.hp < 0:
            self.hp = 0
            self.alive = False
            return -1

        return self.hp

    def power_up(self):
        self.hp += 20
        self.stats.attack += 10
        self.stats.defence -= 5
        self.design = smella
        self.name = f"{self.name} (ULTRA)"
        self.powered = True
