def get_final_floor(instructions):
	return instructions.count('(') - instructions.count(')')

def get_first_basement(instructions):
	floor = 0
	for i, char in enumerate(instructions, 1):
		if char == '(':
			floor += 1
		elif char == ')':
			floor -= 1
		if floor == -1:
			return i

assert get_final_floor('(())') == get_final_floor('()()') == 0
assert get_final_floor('(((') == get_final_floor('(()(()(') == 3
assert get_final_floor('))(((((') == 3
assert get_final_floor('())') == get_final_floor('))(') == -1
assert get_final_floor(')))') == get_final_floor(')())())') == -3
assert get_first_basement(')') == 1
assert get_first_basement('()())') == 5

instructions = open('1.txt').read()
print('Final floor:', get_final_floor(instructions))
print('First instruction that sends to basement:', get_first_basement(instructions))