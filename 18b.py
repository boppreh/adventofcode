import sys
sys.path.append('D:/projects/matrix')
from matrix import Matrix

step = lambda m: m.indexmap(lambda pos, c: (c, sum(m.neighbors(*pos))) in [(True, 2), (True, 3), (False, 3)])

original = Matrix([[c == '#' for c in line.strip()] for line in open('18.txt') if line])

m = original
for i in range(100):
	m = step(m)
print('Number of lights on after 100 steps:', sum(m))

m = original
m[0, 0] = m[0, -1] = m[-1, 0] = m[-1, -1] = True
for i in range(100):
	m = step(m)
	m[0, 0] = m[0, -1] = m[-1, 0] = m[-1, -1] = True
print('Number of lights on after 100 steps with stuck lights:', sum(m))