def parse(text):
	return [[int(c == '#') for c in line] for line in text.split('\n')]

def neighbors(x, y, matrix):
	return sum(sum(line[max(0, x-1):x+2]) for line in matrix[max(0, y-1):y+2]) - matrix[y][x]

def next_state(c, x, y, matrix):
	n_neighbors = neighbors(x, y, matrix)
	return int(n_neighbors == 3 or (n_neighbors == 2 and c))

def step(matrix):
	return [[next_state(c, x, y, matrix) for x, c in enumerate(line)] for y, line in enumerate(matrix)]

def p(matrix):
	print('\n'.join(''.join(map(str, line)) for line in matrix) + '\n')


matrix = parse(open('18.txt').read())
for i in range(100):
	matrix = step(matrix)
print('Total on:', sum(sum(line) for line in matrix))


matrix = parse(open('18.txt').read())
for i in range(100):
	matrix = step(matrix)
	matrix[0][0] = matrix[99][0] = matrix[0][99] = matrix[99][99] = 1
print('Total on with stuck lights:', sum(sum(line) for line in matrix))