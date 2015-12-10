import re

def look_and_say(string):
	result = []
	for match, number in re.findall(r'((\d)\2*)', string):
		result.append('{}{}'.format(len(match), number))
	return ''.join(result)

assert look_and_say('1') == '11'
assert look_and_say('11') == '21'
assert look_and_say('21') == '1211'
assert look_and_say('1211') == '111221'
assert look_and_say('111221') == '312211'

string = '1113222113'

for i in range(40):
	string = look_and_say(string)
print('Length after 40 "look and say"', len(string))

for i in range(10):
	string = look_and_say(string)
print('Length after 50 "look and say"', len(string))