from matrix import InputMatrix
import terminal

def shell_exit():
	exit()

def shell_matrix(arg):
	return InputMatrix(arg)

def shell_view():
	print(terminal.m)