import data

# TODO: when game engine evolves to a class, have these functions also be passed a reference to fight engine. to send events to it.
# async functions maybe? or generators for potential multi hit moves. for stuff out of scope to still happen between.

def simple_damage(attacker, opponent, damage):
    # takes a number of damage as a input, multiplied with attacker's strength stat.
    opponent.decrease_hp(damage * attacker.stats.attack)

def multiple_damage(attacker, opponent, damage, multiplier):
    #essentialy makes a move "hit multiple times"
    opponent.decrease_hp((damage * attacker.stats.attack) * multiplier)

def super_damage(attacker, opponenet, damage, boost, hurted):
    #takes health from the attacker and boosts the strength stats for this move
    attacker.decrease_hp(hurted)
    opponenet.decrease_hp(damage * (boost * attacker.stats.attack))

punch = data.DefaultAttack("punch", (lambda p1, p2: simple_damage(p1, p2, 10))) 
schlap = data.DefaultAttack("schlap", (lambda p1, p2: simple_damage(p1, p2, 13)))
two_piece = data.DefaultAttack("two piece", (lambda p1, p2: multiple_damage(p1, p2, 8, 2)))
one_piece = data.DefaultAttack("one piece", (lambda p1, p2: super_damage(p1, p2, 20, 2, 10)))

basic = [punch, schlap, two_piece, one_piece] 

# seems like this could just be a regular list
# u had it in the data class i think saying it would be a dict, i found it, its in fighters, u said the move sets would be a dict, ooooo, isee, tbh tho its better this way, 
# cuz when it has more than just 4 itll be eaier to choose which ones to print, like when i have 6 moves and the player only can have 4, i can use the numbers to easily call the moves, right?
# yeah but they would be called in the same with with a list. other than the list starting at 0 instead of 1 but that wouldn't be an issue. just basic[n-1]
# I'm not sure I understand but I'll roll with it.
# I dunno I didn't make any data class for something like this. 
# the moves dict in the fighter class is a dict so that they can be referenced by their name by the player input which would be a string

# if your indexing a dict with accending integers it's basically just a list with extra step


# work with what you're doing now because if it ends up being just like a list, changing it to be that will be incredibly easy.
# if I'm just not understanding though, then what your doing will be clearer to me when you're done. so in the end I guess it don't matter