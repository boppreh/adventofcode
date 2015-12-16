import re
from functools import reduce

def totalize(ingredients, amounts, calories_fn=lambda c: True):
	*totals, calories = [sum(i*a for i, a in zip(props, amounts)) for props in zip(*ingredients)]
	return int(calories_fn(calories)) and reduce(lambda a, b: max(0, a) * max(0, b), totals, 1)

def parse_ingredients(text):
	return [[int(i) for i in re.findall('(-?\d+)', line)] for line in text.split('\n') if line]

def combinations(n, total=100, start=[]):
	if n == 1:
		yield start + [total]
	else:
		for i in range(total+1):
			yield from combinations(n-1, total-i, start=start+[i])

def best_combination(ingredients, total=100, calories_fn=lambda c: True):
	return max(combinations(len(ingredients), total),
			   key=lambda a: totalize(ingredients, a, calories_fn))

test_ingredients = parse_ingredients("""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""")
assert best_combination(test_ingredients) == [44, 56]
assert totalize(test_ingredients, [44, 56]) == 62842880


ingredients = parse_ingredients(open('15.txt').read())
print('Best possible score:', totalize(ingredients, best_combination(ingredients)))

print('Best possible score with 500 calories:', totalize(ingredients, best_combination(ingredients, calories_fn=lambda c: c == 500)))