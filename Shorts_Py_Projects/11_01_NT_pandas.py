import pandas as pd

"""
Determine which film received the highest rating of 5.0.
"""


films = pd.merge(pd.read_csv('datasets/movies.csv'), pd.read_csv('datasets/ratings.csv'), on='movieId', how='left')

the_best_movie = films\
    .loc[films.rating == 5.0]\
    .groupby(['movieId', 'title'])\
    .count()\
    .filter(items=['movieId', 'title', 'rating'])\
    .sort_values('rating', ascending=False)

print(the_best_movie.iloc[:1])


