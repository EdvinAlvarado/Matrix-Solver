### Main terminal
from terminal_command import *
from matrix import InputMatrix

# lookups the command and triggers it.
def command_lookup(arg):
	if arg == "exit":
		shell_exit()
	elif arg[:6] == "matrix":
		global m
		m = shell_matrix(arg[7:])
		print(m)
	elif arg == "view":
		shell_view(m)
	elif arg[:4] == "test":
		shell_test(arg[5:])
	elif arg[:5] == "rowop":
		rowop(arg[6:])
	elif arg[:7] == "rowmult":
		rowmult(arg[8:])
	MatrixChecker(m)

# Main Loop
counter = 1 
while True:
	args = input("[%i] "  % counter)
	if args == "":
		continue
	else:
		command_lookup(args)
	counter += 1






