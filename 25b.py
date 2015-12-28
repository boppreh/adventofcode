import re
from itertools import *
import itertools

def multiply(l):
	r = 1
	for i in l: r *= i
	return r

ROW = 2947
COL = 3029
ROW = 6
COL = 6
SEED = 20151125
MULT = 252533
DIV = 33554393
step = lambda p: (p * MULT) % DIV

matrix = []
for i in range(ROW+1):
	matrix.append([])
	for j in range(COL+1):
		matrix[-1].append(0)

matrix[0][0] = SEED
for i in range(ROW):
	for j in range(COL):
		if i == j == 0: continue
		if j == 0:
			matrix[i][j] = step(matrix[0][i])
		else:
			matrix[i][j] = step(matrix[i+1][j+1])

print matrix