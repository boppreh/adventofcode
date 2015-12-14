import re
from math import ceil
from itertools import cycle
from collections import Counter

pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
def make_reindeer(line):
	name, *rest = pattern.match(line).groups(1)
	speed, run_time, rest_time = map(int, rest)
	return cycle([speed] * run_time + [0] * rest_time)

reindeers = [make_reindeer(line) for line in open('14.txt')]
distances = [0] * len(reindeers)
for time in range(2503):
	for i, reindeer in enumerate(reindeers):
		distances[i] += next(reindeer)
print('Max distance:', max(distances))

reindeers = [make_reindeer(line) for line in open('14.txt')]
distances = [0] * len(reindeers)
points = [0] * len(reindeers)
for time in range(2503):
	for i, reindeer in enumerate(reindeers):
		distances[i] += next(reindeer)
	for i, reindeer in enumerate(reindeers):
		if distances[i] == max(distances):
			points[i] += 1
print('Most points:', max(points))