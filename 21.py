from itertools import combinations
import re
from math import ceil

def hits_to_kill(attacker, defender):
	damage = max(1, attacker['attack'] - defender['defense'])
	return ceil(defender['hp'] / damage)

def wins(attacker, defender):
	return hits_to_kill(attacker, defender) <= hits_to_kill(defender, attacker)

def equip(hp, weapons, armors, rings):
	cost, attack, defense = map(sum, zip(*(weapons + armors + rings)))
	return {'hp': hp, 'attack': attack, 'defense': defense}, cost

assert wins({'hp': 8, 'attack': 5, 'defense': 5}, {'hp': 12, 'attack': 7, 'defense': 2})
assert not wins({'hp': 8, 'attack': 5, 'defense': 5}, {'hp': 13, 'attack': 7, 'defense': 2})

boss = {{'Hit Points': 'hp', 'Damage': 'attack', 'Armor': 'defense'}[attribute]: int(value)
		for attribute, value in re.findall(r'([\w ]+): (\d+)', open('21.txt').read())}

store = {
	'weapons': [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)],
	'armor': [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)],
	'rings': [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
}

up_to_combinations = lambda name, start, end: (c for i in range(start, end+1) for c in combinations(store[name], i))

def costs(boss, condition):
	for rings in up_to_combinations('rings', 0, 2):
		for armors in up_to_combinations('armor', 0, 1):
			for weapon in store['weapons']:
				you, cost = equip(100, (weapon,), armors, rings)
				if condition(wins(you, boss)):
					yield cost

print('Minimum cost to win:', min(costs(boss, lambda result: result)))
print('Maximum cost to lose:', max(costs(boss, lambda result: not result)))