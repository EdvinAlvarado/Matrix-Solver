# Main terminal
from terminal_command import *
from matrix import InputMatrix
# import numpy as np

# try to modulairze this.
# m = InputMatrix("data.txt")
# rowsize = len(m)
# colsize = len(m[0])

# working on seeing how to move this out of here without it crashing
# because of circular imports.


# lookups the right command and triggers it.
def command_lookup(arg):
	if arg == "exit":
		shell_exit()
	if arg[:5] == "matrix":
		global m
		m = shell_matrix(arg[6:])
		print(m)
	if arg == "view":
		shell_view(m)


while True:
	args = input("> ")
	if args == "":
		continue
	else:
		command_lookup(args)






