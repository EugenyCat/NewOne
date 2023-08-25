import numpy as np


"""
Create a numpy array with elements from N to 0. For example, for N = 10 it would be array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
"""
def create_np_array(n:int):
    return np.arange(n-1, -1, -1)


print(create_np_array(10))