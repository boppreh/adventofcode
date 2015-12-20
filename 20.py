import math

sieve = [True] * 100000
for i in range(2, int(math.sqrt(len(sieve)))):
	for j in range(2, int(len(sieve)/i)):
		sieve[i * j] = False
prime_numbers = [i for i, v in enumerate(sieve) if v and i]

def gifts(n):
	if n == 1: return 10
	if n == 2: return 30
	total = 0
	self_counted = False
	for p in prime_numbers[1:int(math.sqrt(n))+1]:
		while n % p == 0:
			if n == p:
				self_counted = True
			total += 10 * p
			p *= p
	return total + 10 + (0 if self_counted else 10 * n)

assert gifts(1) == 10
assert gifts(2) == 30, gifts(2)
assert gifts(3) == 40
assert gifts(4) == 70
assert gifts(5) == 60
assert gifts(6) == 120, gifts(6)
assert gifts(7) == 80
assert gifts(8) == 150
assert gifts(9) == 130

goal = 36000000

highly_composite = {1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180}
while todo:
	n = todo.pop(0)
	for p in prime_numbers:
		highly_composite.add(n * p)