def parse(text):
	return [[int(c == '#') for c in line.strip()] for line in text if line]

def neighbors(x, y, matrix):
	return sum(sum(line[max(0, x-1):x+2]) for line in matrix[max(0, y-1):y+2]) - matrix[y][x]

def next_state(c, x, y, matrix):
	n_neighbors = neighbors(x, y, matrix)
	return int(n_neighbors == 3 or (n_neighbors == 2 and c))

def step(matrix):
	return [[next_state(c, x, y, matrix) for x, c in enumerate(line)] for y, line in enumerate(matrix)]

def total_after_steps(matrix, n_steps, is_stuck=False):
	if is_stuck:
		matrix[0][0] = matrix[-1][0] = matrix[0][-1] = matrix[-1][-1] = 1

	for i in range(n_steps):
		matrix = step(matrix)
		if is_stuck:
			matrix[0][0] = matrix[-1][0] = matrix[0][-1] = matrix[-1][-1] = 1
	
	return sum(sum(line) for line in matrix)

def p(matrix):
	print('\n'.join(''.join(map(str, line)) for line in matrix) + '\n')

assert total_after_steps(parse("""
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".split()), 4) == 4

parsed = parse(open('18.txt'))
assert len(parsed) == 100 and all(len(line) == 100 for line in parsed)

print('Total on:', total_after_steps(parsed, 100))

assert total_after_steps(parse("""
##.#.#
...##.
#....#
..#...
#.#..#
####.#
""".split()), 5, True) == 17

print('Total on with stuck lights:', total_after_steps(parsed, 100, True))