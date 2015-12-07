import re

def eval(variable):
	value = raw_eval(variable)
	values[variable] = value
	return value

def raw_eval(variable):
	if variable in values:
		return values[variable]
	if variable.isdigit():
		return int(variable)

	instruction = instructions[variable]

	if 'NOT' in instruction:
		_, value = instruction.split(' ')
		return 2**16-1 - eval(value)
	elif ' ' not in instruction:
		return eval(instruction)
	else:
		left, op_name, right = instruction.split(' ')
		op = binops = {
			'RSHIFT': lambda a, b: a >> b,
			'LSHIFT': lambda a, b: (a << b) % 2**16,
			'AND': lambda a, b: a & b,
			'OR': lambda a, b: a | b,
		}[op_name]
		return op(eval(left), eval(right))

instructions = {}
values = {}
for line in open('7.txt'):
	instruction, variable = line.strip().split(' -> ')
	instructions[variable] = instruction

a_value = eval('a')
print('Value of "a":', a_value)

values.clear()
instructions['b'] = str(a_value)
print('New value of "a":', eval('a'))