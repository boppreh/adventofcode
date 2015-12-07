import re

signals = {}
def eval(variable):
	if variable in signals:
		return signals[variable]
	return signals.setdefault(variable, raw_eval(variable))

def raw_eval(variable):
	if variable.isdigit():
		return int(variable)

	parts = instructions[variable].split()

	if len(parts) == 1:
		return eval(parts[0])
	elif len(parts) == 2:
		assert parts[0] == 'NOT'
		return 2**16-1 - eval(parts[1])
	else:
		left, op_name, right = parts
		return {
			'RSHIFT': lambda a, b: a >> b,
			'LSHIFT': lambda a, b: (a << b) % 2**16,
			'AND': lambda a, b: a & b,
			'OR': lambda a, b: a | b,
		}[op_name](eval(left), eval(right))

instructions = {}
for line in open('7.txt'):
	instruction, variable = line.strip().split(' -> ')
	instructions[variable] = instruction

a_value = eval('a')
print('Value of "a":', a_value)

signals.clear()
instructions['b'] = str(a_value)
print('New value of "a":', eval('a'))