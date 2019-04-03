### Main terminal
from terminal_command import *
# from matrix import InputMatrix

# lookups the command and triggers it.
def command_lookup(arg):
	if arg == "exit":
		shell_exit()
	elif arg[:6] == "matrix":
		global m
		global rowsize
		global colsize
		m = shell_matrix(arg[7:])
		rowsize = len(m)
		colsize = len(m[0])
		print(m)
		MatrixChecker(m)
	elif arg == "view":
		shell_view(m)
		MatrixChecker(m)
	# elif arg[:4] == "test":
	# 	shell_test(arg[5:])
	elif arg[:5] == "rowop":
		rowop(arg[6:], m)
		shell_view(m)
		MatrixChecker(m)
	elif arg[:7] == "rowmult":
		rowmult(arg[8:], m)
		shell_view(m)
		MatrixChecker(m)
	else:
		print("Unknown Command")
	print("\n")


# Main Loop
counter = 1
while True:
	args = input("[%i] " % counter)
	counter += 1
	if args == "":
		print("\n")
		continue
	else:
		command_lookup(args)
