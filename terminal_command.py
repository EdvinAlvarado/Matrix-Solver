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