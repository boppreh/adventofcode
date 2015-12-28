from itertools import combinations

def is_partionable(weights, goal, n_partitions=2):
	for n in range(1, len(weights)-1):
		for comb in combinations(weights, n):
			if sum(comb) == goal and (n_partitions == 2 or is_partionable([w for w in weights if w not in comb], goal, n_partitions-1)):
				return True

#weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
weights = [int(line.strip()) for line in open('24.txt')]
goal = sum(weights) / 4.0
for n in range(1, len(weights)-2):
	results = []
	for comb in combinations(weights, n):
		if sum(comb) != goal or not is_partionable([w for w in weights if w not in comb], goal, 3): continue
		results.append(1)
		for w in comb: results[-1] *= w
		print(comb, results[-1])

	if results:
		print('Minimum quantum entanglement with minimum size:', min(results))
		exit()