### Command Lists
from matrix import InputMatrix
import numpy as np

def shell_exit():
	exit()

def shell_matrix(arg):
	return np.array(InputMatrix(arg))

def shell_view(arg):
	print(arg)

def shell_test(arg):
	print(arg)

def rowop(arg):
	lst = arg.split(" ", 2)
	try:
		rowchanged = lst[0]
		rowoperator = lst[1]
		n = lst[2]
	except IndexError:
		print("missing input.")
	return m[rowoperator] += n * m[rowchanged]

def rowmult(arg):
	lst = arg.split(" ", 1)
	try:
		rowchanged = lst[0]
		n = lst[1]
	except IndexError:
		print("missing input.")
	return m[rowoperator] = m[rowoperator] * n

def MatrixChecker(matrix):
	print("COMING SOON")
# Probably amke it a True or False, so in every loop it verify if the matrix has been solved. once solved it would automatically yell solved.