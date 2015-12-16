import re
from itertools import combinations_with_replacement

def totalize(ingredients, amounts):
	if sum(amounts) != 100: return 0
	total = 1
	for props in zip(*ingredients):
		total *= max(0, sum(i*a for i, a in zip(props, amounts)))
	return total

def parse_ingredients(text):
	return [[int(i) for i in re.findall('(-?\d+)', line)][:-1] for line in text.split('\n') if line]

def best_combination(ingredients):
	combinations = combinations_with_replacement(range(101), len(ingredients))
	key = lambda c: totalize(ingredients, c)
	return max(combinations, key=key)

assert totalize(parse_ingredients("""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""), [44, 56]) == 62842880

print('Best possible score:', best_combination(parse_ingredients(open('15.txt').read())))