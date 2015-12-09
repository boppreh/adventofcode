import time
text = open('7.txt').read().strip().replace('RSHIFT', '>>').replace('LSHIFT', '<<').replace('OR', '|').replace('AND', '&').replace('NOT', '2**16-1-')
lines = [' a '] + [' {} '.format(line.strip()) for line in text.split('\n')]

while len(lines) > 1:
	src, dst = lines.pop().split('->')
	print(repr(dst), repr(src))
	if dst.strip() == 'g' and dst.upper() == dst.lower():
		print(eval(src))
		print(src)
		exit()
	value, replacement = ' {} '.format(dst.strip()), ' ( {} ) '.format(src)
	for i, line in enumerate(lines):
		lines[i] = line.replace(value, replacement)