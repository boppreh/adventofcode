rules_str, m = open('19.txt').read().strip().split('\n\n')
rules = [line.split(' => ') for line in rules_str.split('\n')]

possibles = set()
for i in range(len(m)):
	for left, right in rules:
		if m[i:].startswith(left):
			possibles.add(m[:i] + right + m[i+len(left):])
print('Molecules one step away:', len(possibles))


stack = [(m, 0)]
while stack:
	m, steps = stack.pop()
	if m == 'e':
		print('Steps to manufacture molecule:', steps)
		break
	for i in range(len(m)):
		for left, right in rules:
			if m[i:].startswith(right):
				stack.append((m[:i] + left + m[i+len(right):], steps + 1))