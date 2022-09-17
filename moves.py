import random
from typing import Iterator
from typing import TYPE_CHECKING

from data import Action, ActionState

if TYPE_CHECKING:
    from fighters import Fighter
    from engine import BattleEngine


def test_move(attacker: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    opponent = engine.get_opponent(attacker)

    engine.add_text(f"{attacker.name} is charging an attack!")
    yield ActionState.PAUSE

    engine.add_text(f"{attacker.name} struck")
    yield ActionState.CONTINUE
    engine.add_text(f"{attacker.name} struck again!")

    yield ActionState.END


def simple_damage(damage, attacker: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    opponent = engine.get_opponent(attacker)

    # takes a number of damage as an input, multiplied with attacker's strength stat.
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield ActionState.END


def multi_hit(damage, chance, max_hits, damp, attacker: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    opponent = engine.get_opponent(attacker)

    hits = 0
    while True:
        hits += 1
        opponent.decrease_hp((damage * (damp ** hits)) * attacker.stats.attack)
        if hits > 1:
            engine.add_text(f"Hit {hits} times!" + "!" * hits)
        if (chance < random.random()) or hits >= max_hits:
            break
        else:
            yield ActionState.CONTINUE


def charge_move(damage, turns, attacker: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    opponent = engine.get_opponent(attacker)

    engine.add_text(f"{attacker.name} is charging an attack!")
    yield ActionState.PAUSE
    for x in range(turns - 1):
        engine.add_text(f"{attacker.name} is still charging an attack!")
        yield ActionState.PAUSE

    engine.add_text(f"{attacker.name} Struck!")
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield ActionState.END


def recoil_hit(damage, recoil, attacker: 'Fighter', engine: 'BattleEngine') -> Iterator[ActionState]:
    opponent = engine.get_opponent(attacker)

    # takes health from the attacker and boosts the strength stats for this action
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield ActionState.CONTINUE

    engine.add_text(f"{attacker.name} was hurt by recoil")
    attacker.decrease_hp(recoil)
    yield ActionState.END


# TODO: add a lang table or sum to convert id to localized name. so they don't have to be fully lowercase.
punch = Action("punch", lambda *args: simple_damage(12, *args))
multi = Action("multi", lambda *args: multi_hit(10, 1, 5, 0.8, *args))
two_piece = Action("two piece", lambda *args: charge_move(18, 1, *args))
one_piece = Action("one piece", lambda *args: recoil_hit(20, 10, *args))

test = Action("test", test_move)

taekwondo = []
basic = [punch, multi, two_piece, one_piece]
