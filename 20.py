def visit(houses, presents, elf_range):
	for elf in range(1, len(houses)):
		for i in elf_range(elf):
			houses[i] += presents * elf

def first_house(houses, goal):
	return next(i for i, presents in enumerate(houses) if presents >= goal)


N = int(1e6)

houses = [0] * N
visit(houses, 10, lambda elf: range(elf, N, elf))

assert houses[1:10] == [10, 30, 40, 70, 60, 120, 80, 150, 130]

print('First house with at least 36000000 presents:', first_house(houses, 36000000))

houses = [0] * N
visit(houses, 11, lambda elf: range(elf, min(N, 51 * elf), elf))
print('First house with at least 36000000 presents (lazy elves):', first_house(houses, 36000000))