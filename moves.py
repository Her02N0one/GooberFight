import random
from typing import Iterator
from typing import TYPE_CHECKING

from data import Action, ActionState

if TYPE_CHECKING:
    from fighters import Fighter
    from engine import BattleEngine


def test_move(self: 'Fighter', opponent: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    engine.add_text(f"{self.name} is charging an attack!")
    yield ActionState.PAUSE

    engine.add_text(f"{self.name} struck")

    yield ActionState.CONTINUE

    engine.add_text(f"{self.name} struck again!")

    yield ActionState.END


def simple_damage(damage,
                  self: 'Fighter', opponent: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    # takes a number of damage as an input, multiplied with attacker's strength stat.
    opponent.decrease_hp(damage * self.stats.attack)
    yield ActionState.END


def multi_hit(damage, chance, max_hits, damp,
              self: 'Fighter', opponent: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    hits = 0
    while True:
        hits += 1
        opponent.decrease_hp((damage * (damp ** hits)) * self.stats.attack)
        if hits > 1:
            engine.add_text(f"Hit {hits} times!" + "!" * hits)
        if (chance < random.random()) or hits >= max_hits:
            break
        else:
            yield ActionState.CONTINUE


def charge_move(damage, turns,
                self: 'Fighter', opponent: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    engine.add_text(f"{self.name} is charging an attack!")
    yield ActionState.PAUSE
    for x in range(turns - 1):
        engine.add_text(f"{self.name} is still charging an attack!")
        yield ActionState.PAUSE

    engine.add_text(f"{self.name} Struck!")
    opponent.decrease_hp(damage * self.stats.attack)
    yield ActionState.END


def recoil_hit(damage, recoil,
               self: 'Fighter', opponent: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    # takes health from the attacker and boosts the strength stats for this action_generator
    opponent.decrease_hp(damage * self.stats.attack)
    yield ActionState.CONTINUE

    engine.add_text(f"{self.name} was hurt by recoil")
    self.decrease_hp(recoil)
    yield ActionState.END


# TODO: add a lang table or sum to convert id to localized name. so they don't have to be fully lowercase.
# with present tense verb form as well.
punch = Action("punch", lambda *args: simple_damage(12, *args))
schlap = Action("multi", lambda *args: charge_move(18, 1, *args))
two_piece = Action("two piece", lambda *args: multi_hit(10, 0.9, 2, 0.8, *args))
one_piece = Action("one piece", lambda *args: recoil_hit(20, 10, *args))

straight_hands = Action("straight hands", lambda *args: multi_hit(5, 1, 4, 1, *args))

test = Action("test", test_move)


boxing = [straight_hands]
basic = [punch, schlap, two_piece, one_piece]
