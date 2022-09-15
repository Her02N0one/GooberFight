import random
from functools import partial

import data

WAIT_FOR_OPPONENT = 0
SKIP_OPPONENTS_TURN = 1


# TODO: Find solution on how to let engine know wheather or not opponent can strike between moves.
# skip turn flag on fighter class maybe? 
# I try to avoid using flags when I can but this seems like the only option. 

def simple_damage(damage, attacker, opponent, engine):
    # takes a number of damage as a input, multiplied with attacker's strength stat.
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield WAIT_FOR_OPPONENT


def multi_hit(damage, chance, max, damp, attacker, opponent, engine):
    hits = 0
    while True:
        hits += 1
        opponent.decrease_hp((damage * (damp ** hits)) * attacker.stats.attack)
        if hits > 1:
            engine.text_queue.append(f"Hit {hits} times!" + "!" * hits)
        if (chance < random.random()) or hits >= max:
            break
        else:
            yield SKIP_OPPONENTS_TURN
    yield WAIT_FOR_OPPONENT


def charge_move(damage, turns, attacker, opponent, engine):
    engine.text_queue.append(f"{attacker.name} is charging an attack!")
    yield WAIT_FOR_OPPONENT
    for x in range(turns - 1):
        engine.text_queue.append(f"{attacker.name} is still charging an attack!")
        yield WAIT_FOR_OPPONENT

    engine.text_queue.append(f"{attacker.name} Struck!")
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield WAIT_FOR_OPPONENT


def recoil_hit(damage, recoil, attacker, opponent, engine):
    # takes health from the attacker and boosts the strength stats for this move
    opponent.decrease_hp(damage * attacker.stats.attack)
    yield SKIP_OPPONENTS_TURN

    engine.text_queue.append(f"{attacker.name} was hurt by recoil")
    attacker.decrease_hp(recoil)
    yield WAIT_FOR_OPPONENT


# TODO: add a lang table or sum to convert id to localized name. so they don't have to be fully lowercase.
punch = data.DefaultAttack("punch", partial(simple_damage, 6))
schlap = data.DefaultAttack("multi", partial(multi_hit, 10, 1, 5, 0.8))
two_piece = data.DefaultAttack("two piece", partial(charge_move, 18, 1))
one_piece = data.DefaultAttack("one piece", partial(recoil_hit, 20, 10))

taekwondo = []
basic = [punch, schlap, two_piece, one_piece]
