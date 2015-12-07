import re

def signal(variable, instructions):
	while True:
		for line in instructions:
			line = line.replace('RSHIFT', '>>').replace('LSHIFT', '<<').replace('OR', '|').replace('AND', '&').replace('NOT', '2**16-1-')
			line = re.sub(r'(.+) -> (.+)', r'\2 = \1', line)
			line = re.sub(r'([a-z]+)', r'_\1', line)
			try:
				exec(line, locals())
				return eval('_' + variable)
			except NameError:
				continue

instructions = list(open('7.txt'))
print('Value of "a":', signal('a', instructions))
print('New value of "a":', signal('a', instructions + [str(signal('a', instructions)) + ' -> b']))