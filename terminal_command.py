### Command Lists
from matrix import InputMatrix
import numpy as np

def shell_exit():
	exit()

def shell_matrix(arg):
	return np.array(InputMatrix(arg))

def shell_view(arg):
	print(arg)

# def shell_test(arg):
# 	print(arg)

def rowop(arg, matrix, rowsize):
	lst = arg.split(" ", 2)
	try:
		rowchanged = int(lst[0])
		rowoperator = int(lst[1])
		n = int(lst[2])
	except IndexError:
		print("Too little or many variables.")
	except ValueError:
		print("Wrong variables.")

	try:
		matrix[rowchanged] += n * matrix[rowoperator]
	except IndexError:
		print("Rows outside matrix.")

def rowmult(arg, matrix, rowsize):
	lst = arg.split(" ", 1)
	try:
		rowchanged = int(lst[0])
		n = int(lst[1])
	except IndexError:
		print("Too little or many variables.")
	except ValueError:
		print("Wrong variables.")

	try:
		matrix[rowchanged] = matrix[rowchanged] * n
	except IndexError:
		print("Rows outside matrix.")

# Next Project would be to create a matrix checker that could work with infinite size matrixes. Probably by taking the shape of the matrix and then repeating a pattern.
def MatrixChecker(matrix):
	i = np.identity(matrix.shape[0])
	A = matrix[:, :len(matrix)]
	test_matrix = (A == i)
	if np.prod(test_matrix.shape) == test_matrix.sum():
		print("###CORRECT CONSTANTS###")
	else:
		print("###INCORRECT CONSTANTS###")

