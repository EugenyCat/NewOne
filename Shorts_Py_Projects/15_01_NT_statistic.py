import pandas as pd
import statistics
from scipy.stats import  ttest_ind


"""
From the file hw_25000.csv, take 20 people with a height of 170 to 180 centimeters.
Is it possible to state that the difference between the average weight of people in the original hw_25000.csv file 
and the average weight of people in the entire dataset is statistically significant?
"""

orig = pd.read_csv('datasets/hw_25000.csv')
orig['Height(Centimetres)'] = orig[orig.columns[1]] * 2.54
people_170_180 = orig[(orig['Height(Centimetres)']  >= 170) & (orig['Height(Centimetres)']  <= 180)].iloc[70:90]
alfa = 0.05
#print(orig.head())
#print(len(people_170_180))

print(ttest_ind(orig[orig.columns[2]], people_170_180[people_170_180.columns[2]]))

#print(statistics.mean(orig[orig.columns[2]]))
#print(statistics.mean(people_170_180[people_170_180.columns[2]]))