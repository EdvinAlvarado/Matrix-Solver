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

def MatrixChecker(matrix):
	if matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[0][1] == 0 and matrix[1][0] == 0:
		print("###CORRECT CONSTANTS###")
	else:
		print("###INCORRECT CONSTANTS###")

# Probably amke it a True or False, so in every loop it verify if the matrix has been solved. once solved it would automatically yell solved.