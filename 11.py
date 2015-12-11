import string
import re

lowercase = string.ascii_lowercase
triples = [''.join(lowercase[i:i+3]) for i in range(len(lowercase)-2)]

def basic_requirement(password):
    return len(password) == 8 and password.lower() == password

def first_requirement(password):
    return any(triple in password for triple in triples)

def second_requirement(password):
    return 'i' not in password and 'o' not in password and 'l' not in password

def third_requirement(password):
    return len(re.findall(r'(\w)\1', password)) >= 2


def is_valid(password):
    return basic_requirement(password) and first_requirement(password) and second_requirement(password) and third_requirement(password)

def increment(password):
    assert 0 < len(password) <= 8

    if len(password) == 1:
        return chr(ord(password) + 1)

    for letter in 'iol':
        if letter in password:
            first, second = password.rsplit(letter, 1)
            return increment(first + increment(letter) + 'a' * len(second))

    if password.endswith('z'):
        return increment(password[:-1]) + 'a'
    return password[:-1] + increment(password[-1])

def next_valid(password):
    while True:
        password = increment(password)
        if is_valid(password):
            return password

assert first_requirement('hijklmmn')
assert not second_requirement('hijklmmn')
assert third_requirement('abbceffg')
assert not first_requirement('abbceffg')
assert not third_requirement('abbcegjk')
assert next_valid('abcdefgh') == 'abcdffaa'
assert next_valid('ghijklmn') == 'ghjaabcc'

print('passwording')
password = 'hepxcrrq'
print(next_valid(password))
print(next_valid(next_valid(password)))
