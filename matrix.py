def InputMatrix(txt):
	f = open(txt, "r")
	m = []
	row = 0
	for line in f.readlines():
		m.append([])
		for i in line.split():
			try:
				m[row].append(float(i))
			except ValueError:
				pass
		row += 1
	f.close()
	return m

def MatrixPrinter(matrix):
	i = 0
	for row in matrix:
		print("%s %i" %(row, i))
		i += 1