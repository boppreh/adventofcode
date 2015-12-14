from itertools import permutations
from collections import defaultdict
import re

class Seating(object):
	def __init__(self, text, default_value=0):
		pattern = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)')
		self.pairs = defaultdict(lambda: default_value)
		self.people = set()

		for line in text.split('\n'):
			left, direction_str, amount_str, right = pattern.match(line).groups(1)
			direction = {'gain': 1, 'lose': -1}[direction_str]
			amount = int(amount_str)
			self.pairs[(left, right)] = direction * amount
			self.people.add(left)
			self.people.add(right)

	def total_happiness(self, ordering):
		total = 0
		for i in range(0, len(ordering) - 1):
			left, right = ordering[i:i+2]
			total += self.pairs[(left, right)]
			total += self.pairs[(right, left)]
		total += self.pairs[(ordering[0], ordering[-1])]
		total += self.pairs[(ordering[-1], ordering[0])]
		return total

	@property
	def max_happiness(self):
		return max(map(self.total_happiness, permutations(self.people)))

test_seating = Seating("""Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""")

assert test_seating.total_happiness(['David', 'Alice', 'Bob', 'Carol']) == 41 + 46 - 2 + 54 + 83 - 7 + 60 + 55
assert test_seating.max_happiness == 330

seating = Seating(open('13.txt').read())
print('Max happiness:', seating.max_happiness)
seating.people.add('Me')
print('Max happiness with me:', seating.max_happiness)