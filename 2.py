from itertools import starmap

def paper(l, w, h):
	area = 2*l*w + 2*w*h + 2*h*l
	slack = min(l*w, w*h, h*l)
	return area + slack

def ribbon(l, w, h):
	s1, s2, _ = sorted([l, w, h])
	volume = l * w * h
	return s1 * 2 + s2 * 2 + volume

assert paper(2, 3, 4) == 58
assert paper(1, 1, 10) == 43
assert ribbon(2, 3, 4) == 34
assert ribbon(1, 1, 10) == 14

sizes = []
for line in open('2.txt'):
	l, w, h = map(int, line.split('x'))
	sizes.append((l, w, h))
print('Total paper required:', sum(starmap(paper, sizes)))
print('Total ribbon required:', sum(starmap(ribbon, sizes)))