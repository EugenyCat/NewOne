import pandas as pd

"""
Calculate the total consumption of the Baltic countries (Estonia, Latvia and Lithuania) 
of categories 4, 12 and 21 from 2005 to 2010. Do not calculate negative quantity values.
"""

power = pd.read_csv('datasets/power.csv')

condition = "country in ['Estonia', 'Latvia', 'Lithuania'] and category in [4, 12, 21] and year >= 2005 and year <= 2010 and quantity > 0"
consumption = power\
    .query(condition)\
    .groupby(['country'])\
    .sum()\
    .filter(items=['country', 'quantity'])\
    .sort_values('quantity', ascending=False)

print(consumption.head())