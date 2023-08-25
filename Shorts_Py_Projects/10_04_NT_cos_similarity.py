import numpy as np


"""
There is a matrix of purchases in the online store. Column A is the user’s ID. Other columns are the number of purchases of categories of goods by this user - users_stats.

The site is visited by another visitor - next_user_stats.

Find the most similar user: consider the cosine similarity between this user and all users in the user_stats array
"""


users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])


# cos = a*b/ |a| * |b|
def soc_similarity(matrix:np, finder:np):
    return (np.dot(matrix, finder)/(np.linalg.norm(matrix, axis=1)*np.linalg.norm(finder, axis=0))).max()


print(soc_similarity(users_stats, next_user_stats))