import numpy as np


"""
Create a diagonal matrix with elements from N to 0. Calculate the sum of its values on the diagonal.
"""

def create_np_diagonal(n:int):
    return np.diag(np.arange(n, -1, -1))

print(create_np_diagonal(10))

print(create_np_diagonal(10).sum())