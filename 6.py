import re

pattern = '(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'
commands = {
	'turn on': lambda i: True,
	'turn off': lambda i: False,
	'toggle': lambda i: int(not i)
}
commands2 = {
	'turn on': lambda i: i+1,
	'turn off': lambda i: i-1,
	'toggle': lambda i: i+2
}

def count_lights(instructions, commands=commands):
	matrix = [[0 for i in range(1000)] for j in range(1000)]

	for line in instructions:
		command_name, *pos = re.match(pattern, line).groups(1)
		x_start, y_start, x_end, y_end = map(int, pos)
		command = commands[command_name]
		for x in range(x_start, x_end+1):
			for y in range(y_start, y_end+1):
				matrix[y][x] = max(0, command(matrix[y][x]))

	return sum(sum(line) for line in matrix)

assert count_lights(['turn on 0,0 through 999,999']) == 1000 * 1000
assert count_lights(['toggle 0,0 through 999,0']) == 1000
assert count_lights(['turn off 499,499 through 500,500']) == 0
assert count_lights(['turn on 0,0 through 0,0'], commands2) == 1
assert count_lights(['toggle 0,0 through 999,999'], commands2) == 2000000

print('Lights on:', count_lights(open('6.txt')))
print('Lights on (new translation):', count_lights(open('6.txt'), commands2))