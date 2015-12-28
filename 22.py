from itertools import combinations_with_replacement

def battle(player, boss, spell_list):
	shield = 0
	poison = 0
	recharge = 0
	used_mana = 0
	turn = player
	while True:
		if shield:
			player['armor'] = 7
			shield -= 1
		else:
			player['armor'] = 0

		if poison:
			boss['hp'] -= 3
			if boss['hp'] <= 0: return (True, used_mana)
			poison -= 1			

		if recharge:
			player['mana'] += 101
			recharge -= 1

		if turn == player:
			try:
				spell = next(spell_list)
			except StopIteration:
				return (False, used_mana)

			if spell == 'magic missile':
				boss['hp'] -= 4
				cost = 53
			elif spell == 'drain':
				boss['hp'] -= 2
				player['hp'] += 2
				cost = 73
			elif spell == 'shield':
				if shield: return (False, used_mana)
				shield = 6
				cost = 113
			elif spell == 'poison':
				if poison: return (False, used_mana)
				poison = 6
				cost = 173
			elif spell == 'recharge':
				if recharge: return (False, used_mana)
				recharge = 5
				cost = 229


			player['mana'] -= cost
			if player['mana'] < 0: return (False, used_mana)
			used_mana += cost
			turn = boss

			if boss['hp'] <= 0: return (True, used_mana)

		elif turn == boss:
			player['hp'] -= max(1, boss['damage'] - player['armor'])
			if player['hp'] <= 0: return (False, used_mana)
			turn = player


assert battle({'hp': 10, 'mana': 250}, {'hp': 13, 'damage': 8}, iter(['poison', 'magic missile'])) == (True, 226)
assert battle({'hp': 10, 'mana': 250}, {'hp': 14, 'damage': 8}, iter(['recharge', 'shield', 'drain', 'poison', 'magic missile'])) == (True, 641)

spell_list = ['recharge', 'shield', 'drain', 'poison', 'magic missile']
min_mana = float('inf')
for turns in range(40):
	for spells in combinations_with_replacement(spell_list, turns):
		result, mana = battle({'hp': 50, 'mana': 500}, {'hp': 58, 'damage': 9}, iter(spells))
		if result and mana < min_mana:
			min_mana = mana
			print(min_mana)
print('Minimum mana to win battle:', min_mana)