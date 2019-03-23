# from matrix import InputMatrix
from terminal_command import shell_matrix
import numpy as np


m = shell_matrix("data.txt")

i = np.identity(m.shape[0])
m_main = m[:, :len(m)]
print(i)
print(m_main)
print(len(m))

testmatrix = m_main == i
print(sum(testmatrix.shape))
print(testmatrix.sum())

if sum(testmatrix.shape) == testmatrix.sum():
	print("###CORRECT CONSTANTS###")
else:
	print("###INCORRECT CONSTANTS###")