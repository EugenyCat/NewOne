import pandas as pd
import re

"""
We need to check if it’s true that the average rating gets lower with the year of the film’s release grows.
"""

def production_year(row):
    year = 1900
    row_year = re.findall('\d{4}', row)

    if len(row_year) > 0 and int(row_year[0]) in years:
        year = int(row_year[0])
    return year


years = set(range(1950, 2011))

movies = pd.merge(pd.read_csv('datasets/movies.csv'), pd.read_csv('datasets/ratings.csv'), how='left', on='movieId')

movies['year'] = movies['title'].apply(production_year)
movies = movies.groupby(['year'], as_index=False)['rating'].mean().sort_values('year')
print(movies.head())
