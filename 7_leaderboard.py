oprint=print;lines = [s.strip() for s in open('7.txt').readlines()];text = open('7.txt').read()
import os;from os import path;import pathlib;from pathlib import Path;import re;from re import *;from itertools import *;import math;from math import *;from random import *;from requests import *;import requests
def join(l, s=''): return s.join(map(str, l))

out = []
import string
for l in string.ascii_lowercase:
	out.append('unsigned short {} = 0;'.format(l))

for l in string.ascii_lowercase:
	for l2 in string.ascii_lowercase:
		out.append('unsigned short {}{} = 0;'.format(l, l2))

for line in lines:
	left, right = line.split('->')
	left = left.replace('RSHIFT', '>>').replace('LSHIFT', '<<').replace('AND', ' & ').replace('OR', ' | ').replace('NOT', '~')
	out.append('{} = {};'.format(right, left))


print(sub(r'([a-z]+)', r'_\1', '\n'.join(out)).replace('_unsigned', 'unsigned').replace('_short', 'short'))