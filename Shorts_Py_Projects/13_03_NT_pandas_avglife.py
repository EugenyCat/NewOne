import pandas as pd


"""
Use the file with movie ratings ratings.csv. 
Calculate the average lifetime of users who have posted more than 100 ratings. 
Lifetime is the difference between the maximum and minimum values of the timestamp column for a given userId value.
"""


ratings = pd.read_csv('datasets/ratings.csv').groupby('userId', as_index=False).agg({'movieId':'count', 'timestamp': ['max', 'min' ]})

ratings = ratings.loc[ratings['movieId']['count'] >= 100]

ratings['avg life'] = ratings['timestamp']['max']-ratings['timestamp']['min']

print(ratings)
