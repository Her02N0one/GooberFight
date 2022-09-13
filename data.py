from dataclasses import dataclass

@dataclass
class DefaultStats:
    health: float
    defence: float
    speed: float
    attack: float

@dataclass
class PerFightStats: # will be reset to defaults after every fight
    modifiable_stats: DefaultStats
    hp: float
    battle_conditions: int # flags for conditions, probably. unused so far
    

@dataclass
class DefaultAttack:
    name: str
    move: callable

class Fighter:
    move_limit = 4
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.match_stats = PerFightStats(stats, stats.health, 0)
        self.moves = dict()
        self.alive = True

    def get_health_percent(self):
        return self.match_stats.hp/self.stats.health
    
    def start_match(self):
        # reset any stats that were temporarily changed when match starts
        self.match_stats = PerFightStats(self.stats, self.stats.health, 0)
        self.alive = True

    def add_move(self, move: DefaultAttack):
        if (len(self.moves)+1) < self.move_limit:
            self.moves[move.name] = move
            
    
    def decrease_hp(self, amount):
        if (self.match_stats.hp - self.match_stats.hp) < 0:
            self.alive = False
            return -1
        self.match_stats.hp -= amount

def simple_damage(attacker: Fighter, opponent: Fighter, damage):
    opponent.decrease_hp(damage * attacker.stats.attack)

punch = DefaultAttack("punch", (lambda p1, p2: simple_damage(p1, p2, 10)))


