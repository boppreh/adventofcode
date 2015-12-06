from re import search

def is_nice(string):
	has_vowels = search('((a|e|i|o|u).*?){3,}', string)
	has_twice = search(r'.*?(.)\1.*?', string)
	has_forbidden = search('(ab)|(cd)|(pq)|(xy)', string)
	return bool(has_vowels and has_twice and not has_forbidden)

def is_nice2(string):
	has_pair = search(r'(..).*?\1', string)
	has_sandwich = search(r'(.).\1', string)
	return bool(has_pair and has_sandwich)

assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert not is_nice('jchzalrnumimnmhp')
assert not is_nice('haegwjzuvuyypxyu')
assert not is_nice('dvszwmarrgswjxmb')
assert is_nice2('qjhvhtzxzqqjkmpb')
assert is_nice2('xxyxx')
assert not is_nice2('uurcxstgmygtbstg')
assert not is_nice2('ieodomkazucvgmuy')

print('Number of nice strings:', sum(map(is_nice, open('5.txt'))))
print('Number of nice2 strings:', sum(map(is_nice2, open('5.txt'))))