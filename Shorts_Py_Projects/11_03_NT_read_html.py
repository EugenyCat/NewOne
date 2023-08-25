import pandas as pd

"""
Select a page of any site with tabular data. Import tables to pandas DataFrame.
"""


web_tables = pd.read_html('https://fortrader.org/quotes')
print(web_tables[0].head())