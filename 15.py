import re

def totalize(ingredients, amounts, required_calories=None):
	if sum(amounts) != 100: return 0
	calories = sum(a*c for a, (*_, c) in zip(amounts, ingredients))
	if required_calories and calories != required_calories: return 0

	total = 1
	for props in list(zip(*ingredients))[:-1]:
		total *= max(0, sum(i*a for i, a in zip(props, amounts)))
	return total

def parse_ingredients(text):
	return [[int(i) for i in re.findall('(-?\d+)', line)] for line in text.split('\n') if line]

def combinations(n, total=100, start=[]):
	if n == 1:
		yield start + [total]
		return
	for i in range(total+1):
		yield from combinations(n-1, total-i, start=start+[i])

def best_combination(ingredients, total=100, calories=None):
	return max(combinations(len(ingredients), total),
			   key=lambda c: totalize(ingredients, c, calories))

test_ingredients = parse_ingredients("""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""")
assert best_combination(test_ingredients) == [44, 56]
assert totalize(test_ingredients, [44, 56]) == 62842880


ingredients = parse_ingredients(open('15.txt').read())
print('Best possible score:', totalize(ingredients, best_combination(ingredients)))

print('Best possible score with 500 calories:', totalize(ingredients, best_combination(ingredients, calories=500)))