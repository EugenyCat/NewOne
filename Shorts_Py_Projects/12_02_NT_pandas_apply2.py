import pandas as pd

"""
You need to write a geo-classifier, which each row will be able to show a geographical location of a particular region. 
if the search query contains the name of the city of the region, the column 'region' writes the name of that region. 
If the search query does not contain a city name, then put 'undefined'.
"""

geo_data = {

'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}


def define_region(row):
    global geo_data
    req_class = 'undefined'
    for reg in geo_data.keys():
        if row in geo_data.get(reg):
            req_class = reg
            break
    return req_class

keywords = pd.read_csv('datasets/keywords.csv')

keywords['region'] = keywords['keyword'].apply(define_region)

print(keywords.sort_values('region', ascending=False).head())