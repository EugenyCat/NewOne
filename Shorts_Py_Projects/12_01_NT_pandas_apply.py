from urllib import parse
import pandas as pd


"""
Write a function that classifies movies according to the rules:

rating 2 and below - low rating;
rating 4 and below - average rating;
rating 4.5 and 5 - high rating.

Write the result in the class column.
"""


def to_class(row):
    film_class = None
    if row <= 2.0:
        film_class = 'low rating'
    elif row <= 4.0:
        film_class = 'average rating'
    elif row <= 5.0:
        film_class = 'high rating'
    else:
        film_class = 'some error'
    return  film_class


movies = pd.merge(pd.read_csv('datasets/movies.csv'), pd.read_csv('datasets/ratings.csv'), on='movieId')

movies = movies.groupby(['title', 'movieId'], as_index=False).agg({'rating' : 'mean'})

movies['class'] = movies['rating'].apply(to_class)

print(movies.head())
