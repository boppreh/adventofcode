import re
from itertools import permutations

def best_path(pairs_distances, metric_function):
	cities = set(sum(pairs_distances, ()))
	def path_cost(path):
		cost = 0
		for i in range(1, len(path)):
			try:
				cost += pairs_distances[(path[i-1], path[i])]
			except KeyError:
				cost += pairs_distances[(path[i], path[i-1])]
		return cost

	return metric_function(map(path_cost, permutations(cities)))
	

test_distances = {('London', 'Dublin'): 464, ('London', 'Belfast'): 518, ('Dublin', 'Belfast'): 141}
assert best_path(test_distances, min) == 605

matches = [re.match(r'(\w+) to (\w+) = (\d+)', line).groups(1)
		   for line in open('9.txt')]
distances = {(origin, destination): int(distance)
			 for origin, destination, distance in matches}
print('Shortest distance:', best_path(distances, min))

assert best_path(test_distances, max) == 982
print('Longest distance:', best_path(distances, max))
