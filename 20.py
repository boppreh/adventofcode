def visit(houses, elf_range, presents):
	for elf in range(1, len(houses)):
		for i in elf_range(elf):
			if i >= len(houses): break
			houses[i] += presents * elf

def first_house(houses, goal):
	for i, presents in enumerate(houses):
		if presents >= goal:
			return i


N = int(1e6)

houses = [0] * N
visit(houses, lambda elf: range(elf, N, elf), 10)

assert houses[1:10] == [10, 30, 40, 70, 60, 120, 80, 150, 130]

print('First house with at least 36000000 presents:', first_house(houses, 36000000))

houses = [0] * N
visit(houses, lambda elf: range(elf, 51 * elf, elf), 11)
print('First house with at least 36000000 presents (lazy elves):', first_house(houses, 36000000))