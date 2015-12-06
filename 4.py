from hashlib import md5
from itertools import count

def test(secret, nonce, zero_count):
	content = '{}{}'.format(secret, nonce).encode('utf-8')
	hash = md5(content).hexdigest()
	return hash.startswith('0' * zero_count)

def mine(secret, zero_count=5):
	for i in count(1):
		if test(secret, i, zero_count):
			return i

assert mine('abcdef') == 609043
assert mine('pqrstuv') == 1048970

secret = 'yzbqklnj'
print('My first nonce with 5 zeroes:', mine(secret))
print('My first nonce with 6 zeroes:', mine(secret, 6))