import re

info = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3, 
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}
comparisons = {
	'cats': lambda a, b: a > b,
	'trees': lambda a, b: a > b,
	'pomeranians': lambda a, b: a < b,
	'goldfish': lambda a, b: a < b,
}

for line in open('16.txt'):
	props = {k: int(v) for k, v in re.findall(r'(\w+): (\d+)', line)}
	for description, comp in [('first', {}), ('second', comparisons)]:
		if all(comp.get(i, lambda a, b: a==b)(props[i], info[i]) for i in props):
			print('{} matches {} description'.format(line.strip(), description))