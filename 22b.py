from copy import deepcopy

SUDDEN_DEATH = True

def turn(state, spell, on_invalid, on_win, on_lose, on_continue):
	state = deepcopy(state)

	def damage(name, amount, on_dead):
		state[name]['hp'] -= amount
		if state[name]['hp'] <= 0:
			on_dead(state)
			return True

	def use_mana(cost):
		state['player']['mana'] -= cost
		if state['player']['mana'] < 0:
			on_lose(state)
			return True
		state['used_mana'] += cost

	def cast_effect(name, turns):
		if state['effects'][name]:
			on_invalid(state)
			return True
		else:
			state['effects'][name] = turns

	def test_effect(name):
		if state['effects'][name]:
			state['effects'][name] -= 1
			return True

	def apply_all_effects():
		if test_effect('shield'): state['player']['armor'] = 7
		else: state['player']['armor'] = 0

		if test_effect('poison') and damage('boss', 3, on_win): return True
		if test_effect('recharge'): state['player']['mana'] += 101

	if SUDDEN_DEATH and damage('player', 1, on_lose): return

	if apply_all_effects(): return

	if spell == 'magic missile':
		if use_mana(53): return
		if damage('boss', 4, on_win): return
	elif spell == 'drain':
		if use_mana(73): return
		if damage('boss', 2, on_win): return
		state['player']['hp'] += 2
	elif spell == 'shield':
		if use_mana(113): return
		if cast_effect('shield', 6): return
	elif spell == 'poison':
		if use_mana(173): return
		if cast_effect('poison', 6): return
	elif spell == 'recharge':
		if use_mana(229): return
		if cast_effect('recharge', 5): return

	if apply_all_effects(): return

	attack = max(1, state['boss']['damage'] - state['player']['armor'])
	if not damage('player', attack, on_lose):
		on_continue(state)

def battle(state, max_turns, spell_fn, on_win, on_lose):
	if max_turns <= 0: return
	def on_turn(spell):
		turn(state, spell,
			lambda s: None,
			on_win,
			on_lose,
			lambda s: battle(s, max_turns-1, spell_fn, on_win, on_lose))
	spell_fn(state, on_turn)

spell_list = ['recharge', 'shield', 'drain', 'poison', 'magic missile']
state = {'player': {'hp': 50, 'mana': 500}, 'boss': {'hp': 58, 'damage': 9}, 'effects': {'shield': 0, 'poison': 0, 'recharge': 0}, 'used_mana': 0}
min_mana = float('inf')
def on_win(state):
	global min_mana
	if state['used_mana'] < min_mana:
		min_mana = state['used_mana']
		print(min_mana)
battle(state, 100, lambda s, on_turn: [on_turn(spell) for spell in spell_list if s['used_mana'] < min_mana], on_win, lambda s: None)
print('Minimum mana to win battle:', min_mana)