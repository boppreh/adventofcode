from itertools import combinations

sizes = [int(s) for s in open('17.txt')]

by_size = {n: sum(1 for c in combinations(sizes, n) if sum(c) == 150)
		   for n in range(1, len(sizes)+1)}
print('Total combinations:', sum(by_size.values()))
print('Minimum combinations:', next(v for k, v in sorted(by_size.items()) if v))