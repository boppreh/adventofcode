def interpret(lines, registers={'a': 0, 'b': 0}):
	registers = dict(registers)
	lines = list(lines)
	instruction_pointer = 0
	while instruction_pointer < len(lines):
		op, rest = lines[instruction_pointer].strip().split(' ', 1)
		if op == 'hlf':
			registers[rest] /= 2
		elif op == 'tpl':
			registers[rest] *= 3
		elif op == 'inc':
			registers[rest] += 1
		elif op == 'jmp':
			instruction_pointer += int(rest)
			continue
		elif op == 'jie':
			r, offset = rest.split(', ')
			if registers[r] % 2 == 0:
				instruction_pointer += int(offset)
				continue
		elif op == 'jio':
			r, offset = rest.split(', ')
			if registers[r] == 1:
				instruction_pointer += int(offset)
				continue
		instruction_pointer += 1
	return registers


assert interpret('inc a\njio a, +2\ntpl a\ninc a'.split('\n'))['a'] == 2

print(interpret(open('23.txt')))
print(interpret(open('23.txt'), registers={'a': 1, 'b': 0}))