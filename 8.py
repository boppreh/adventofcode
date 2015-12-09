import re

def count_memory(text):
	iterator = iter(text)
	total = 0
	assert next(iterator) == '"'
	for c in iterator:
		if c == '\\':
			c = next(iterator)
			if c == '\\':
				total += 1
			elif c == '"':
				total += 1
			else:
				assert c == 'x'
				assert '0' <= next(iterator) <= 'f'
				assert '0' <= next(iterator) <= 'f'
				total += 1
		elif c == '"':
			break
		else:
			total += 1
	assert all(c.isspace() for c in iterator)
	return total

def count_memory(text):
	return len(eval(text))

def count_code(text):
	return len(text) + text.count('"') + text.count('\\') + 2

assert count_memory('""') == 0
assert count_memory('"abc"') == 3
assert count_memory(r'"aaa\"aaa"') == 7
assert count_memory(r'"\x27"') == 1

print('Total memory:', sum(len(line.strip()) - count_memory(line) for line in open('8.txt')))

assert count_code('""') == 6
assert count_code('"abc"') == 9
assert count_code(r'"aaa\"aaa"') == 16
assert count_code(r'"\x27"') == 11

def count_difference(text):
	text = text.strip()
	return count_code(text) - len(text)

assert count_difference('""') == 4
assert count_difference('"abc"') == 4
assert count_difference(r'"aaa\"aaa"') == 6
assert count_difference(r'"\x27"') == 5

print('Total code:', sum(map(count_difference, open('8.txt'))))