import numpy as np


"""
Solve the equation system:
4x + 2y + z = 4
x + 3y = 12
5y + 4z = -3
"""


coefficients = np.array([4, 2, 1, 1, 3, 0, 0, 5, 4]).reshape((3, 3))
right = np.array([4, 12, -3])


xyz = np.linalg.solve(coefficients, right)
print(xyz)
print(np.dot(coefficients, xyz))


check = np.allclose(np.dot(coefficients, xyz), right)
print(check)