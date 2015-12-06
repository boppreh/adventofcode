def visited(instructions):
	x, y = 0, 0
	visited = {(x, y)}
	for char in instructions:
		if char == '>':
			x += 1
		elif char == '<':
			x -= 1
		elif char == '^':
			y -= 1
		elif char == 'v':
			y += 1
		visited.add((x, y))

	return visited

def visited_with_robo(instructions):
	return visited(instructions[::2]) | visited(instructions[1::2])

assert len(visited('>')) == 2
assert len(visited('^>v<')) == 4
assert len(visited('^v^v^v^v^v')) == 2
assert len(visited_with_robo('^v')) == 3
assert len(visited_with_robo('^>v<')) == 3
assert len(visited_with_robo('^v^v^v^v^v')) == 11

instructions = open('3.txt').read()
print('Houses visited:', len(visited(instructions)))
print('Houses visited with robo:', len(visited_with_robo(instructions)))