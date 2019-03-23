# Matrix-Solver
Solves a system of equations of any size that can create a nxn matrix with [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination). the operations can be done through terminal. There's two [operations](https://en.wikipedia.org/wiki/Gaussian_elimination#Row_operations) that can be done:

+ **rowop** - addition or subtraction of one row scalar to another. 

+ **rowmult** - mutiply a row by a nonzero scalar. if you do multiply by zero a warning is going to appear and you'll have to start from the beginning.


The matrix needs to be a proper [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix) for the constants to be correct. This works for any size matrix.

This was also created in a form of terminal interface. So the skeleton of this can be used for any terminal interface program.

## More Refernces
http://mathworld.wolfram.com/GaussianElimination.html